// Cloudflare Pages Function behind the treasurer page (POST /api/treasurer).
// It checks the PIN, then reads or rewrites donations.yml in the GitHub repo.
// The commit triggers a Cloudflare redeploy, which updates the public site.
//
// Secrets (Cloudflare Pages > Settings > Variables and Secrets):
//   TREASURER_PIN  the PIN the treasurer types in
//   GITHUB_TOKEN   fine-grained token with Contents read/write on this repo
// Optional: GITHUB_REPO (owner/name) and GITHUB_BRANCH. The branch defaults
// to the one Cloudflare is deploying, so a save lands where it is served.

const FILE = 'donations.yml';
const DEFAULT_REPO = 'testag569-hub/mvboyvolleyball';
const DEFAULT_BRANCH = 'claude/project-thread-oi8s8i';

const HEADER = `# MV Boys Volleyball fundraiser
#
# To update: use the treasurer page, or click the pencil icon on GitHub,
# make your change, and click "Commit changes". The site adds up the total
# raised, the number of donors and the percent of the goal for you.
#
# Lines starting with # are notes. The site ignores them.
`;

const json = (body, status = 200) =>
  new Response(JSON.stringify(body), {
    status,
    headers: { 'content-type': 'application/json', 'cache-control': 'no-store', 'x-robots-tag': 'noindex' },
  });

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

// Compare without returning early, so timing does not leak the PIN.
function same(a, b) {
  a = String(a); b = String(b);
  let diff = a.length ^ b.length;
  for (let i = 0; i < Math.max(a.length, b.length); i++) diff |= (a.charCodeAt(i) || 0) ^ (b.charCodeAt(i) || 0);
  return diff === 0;
}

const toB64 = (text) => {
  const bytes = new TextEncoder().encode(text);
  let bin = '';
  for (let i = 0; i < bytes.length; i += 0x8000) bin += String.fromCharCode(...bytes.subarray(i, i + 0x8000));
  return btoa(bin);
};
const fromB64 = (b64) => new TextDecoder().decode(Uint8Array.from(atob(b64.replace(/\s/g, '')), (c) => c.charCodeAt(0)));

// Plain words stay bare; anything YAML could misread gets double quotes.
function str(v) {
  const s = String(v).trim();
  const risky = !/^[A-Za-z0-9][A-Za-z0-9 .,'&()/!-]*$/.test(s) ||
    /^(y|yes|n|no|true|false|on|off|null|~)$/i.test(s) || /^[0-9.,-]+$/.test(s) || / #/.test(s);
  return risky ? JSON.stringify(s) : s;
}

const clean = (v, max) => String(v == null ? '' : v).replace(/[\u0000-\u001f]/g, ' ').trim().slice(0, max);

function toYaml(d) {
  const yn = (v) => (v ? 'yes' : 'no');
  let out = HEADER + `
# The fundraising goal in dollars.
goal: ${d.goal}

# Show donor names on the Supporter wall (yes or no).
show_supporter_wall: ${yn(d.show_supporter_wall)}

# Show how much each person gave on the Supporter wall (yes or no).
show_amounts: ${yn(d.show_amounts)}

# One donor per entry. To add a donor, copy an entry (from "- name:"
# down to the blank line) and change it. Keep the same spaces at the
# start of each line.
#   anonymous: yes   counts the money but shows "Anonymous" on the wall.
#   method, date     are optional notes for you.
# Money with no name to list (cash at a match, a bake sale) can be its
# own entry, for example  name: Bake sale  with  anonymous: yes.
`;
  if (!d.donations.length) return out + 'donations: []\n';
  out += 'donations:\n';
  out += d.donations.map((x) => {
    let e = `  - name: ${str(x.name)}\n    amount: ${x.amount}\n`;
    if (x.method) e += `    method: ${str(x.method)}\n`;
    if (x.date) e += `    date: ${str(x.date)}\n`;
    if (x.anonymous) e += '    anonymous: yes\n';
    return e;
  }).join('\n');
  return out;
}

function validate(data) {
  if (!data || typeof data !== 'object') throw new Error('Nothing to save.');
  const goal = Number(data.goal);
  if (!(goal > 0 && goal < 10000000)) throw new Error('The goal must be a dollar amount above 0.');
  if (!Array.isArray(data.donations) || data.donations.length > 2000) throw new Error('The donor list is not valid.');
  const donations = data.donations.map((x, i) => {
    const name = clean(x && x.name, 80);
    const amount = Math.round(Number(String(x && x.amount).replace(/[$,\s]/g, '')) * 100) / 100;
    if (!name) throw new Error(`Donation ${i + 1} needs a name (use "Anonymous" or "Bake sale" if there isn't one).`);
    if (!(amount > 0 && amount < 1000000)) throw new Error(`Donation ${i + 1} (${name}) needs an amount above 0.`);
    const date = clean(x.date, 10);
    if (date && !/^\d{4}-\d{2}-\d{2}$/.test(date)) throw new Error(`Donation ${i + 1} (${name}) has a date that is not valid.`);
    return { name, amount, method: clean(x.method, 40), date, anonymous: !!x.anonymous };
  });
  return { goal: Math.round(goal), show_supporter_wall: !!data.show_supporter_wall, show_amounts: !!data.show_amounts, donations };
}

async function github(env, path, init = {}) {
  const repo = env.GITHUB_REPO || DEFAULT_REPO;
  const res = await fetch(`https://api.github.com/repos/${repo}/${path}`, {
    ...init,
    headers: {
      authorization: `Bearer ${env.GITHUB_TOKEN}`,
      accept: 'application/vnd.github+json',
      'user-agent': 'mv-volleyball-treasurer',
      'x-github-api-version': '2022-11-28',
      ...(init.body ? { 'content-type': 'application/json' } : {}),
    },
  });
  const body = await res.json().catch(() => ({}));
  return { status: res.status, body };
}

export async function onRequestPost({ request, env }) {
  if (!env.TREASURER_PIN || !env.GITHUB_TOKEN) {
    return json({ error: 'The treasurer page is not set up yet. Add TREASURER_PIN and GITHUB_TOKEN in Cloudflare, then redeploy.' }, 503);
  }
  let req;
  try { req = await request.json(); } catch { return json({ error: 'Bad request.' }, 400); }

  if (!same(req.pin || '', env.TREASURER_PIN)) {
    await sleep(1500); // slows down guessing; a 4-digit PIN is still weak
    return json({ error: 'Wrong PIN.' }, 401);
  }

  const branch = env.GITHUB_BRANCH || env.CF_PAGES_BRANCH || DEFAULT_BRANCH;
  const where = `contents/${FILE}?ref=${encodeURIComponent(branch)}`;

  if (req.action === 'load') {
    const r = await github(env, where);
    if (r.status !== 200) return json({ error: `Could not read ${FILE} from GitHub (${r.status}). Check the GITHUB_TOKEN.` }, 502);
    return json({ yaml: fromB64(r.body.content), sha: r.body.sha, branch });
  }

  if (req.action === 'save') {
    let data;
    try { data = validate(req.data); } catch (e) { return json({ error: e.message }, 400); }
    const r = await github(env, `contents/${FILE}`, {
      method: 'PUT',
      body: JSON.stringify({
        message: `Update donations from the treasurer page (${data.donations.length} entries)`,
        content: toB64(toYaml(data)),
        sha: req.sha,
        branch,
      }),
    });
    if (r.status === 409 || r.status === 422) {
      return json({ error: 'Someone else changed the donations since you opened this page. Reload and enter your change again.' }, 409);
    }
    if (r.status !== 200 && r.status !== 201) return json({ error: `GitHub refused the save (${r.status}). Check the GITHUB_TOKEN.` }, 502);
    return json({ ok: true, sha: r.body.content && r.body.content.sha, commit: r.body.commit && r.body.commit.html_url });
  }

  return json({ error: 'Unknown action.' }, 400);
}
