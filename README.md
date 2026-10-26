# Monte Vista Boys Volleyball Fundraising Site

The fundraising site for MV Boys Volleyball. Open `index.html` to view it.

It has a donate section with Venmo and Zelle QR codes, sponsor levels and logos, photos, coaches, the roster and the schedule.

## Updating donations and the goal

Edit `donations.yml`. It holds the goal and a short entry per donor. The page adds it all up when it loads (total raised, number of donors, percent funded) and lists donor names on the supporter wall. No rebuild is needed.

On GitHub: open `donations.yml`, click the pencil icon, copy a donor entry and change it, then click **Commit changes**. The notes at the top of the file explain each setting. If a typo breaks the file, the scoreboard shows a short notice instead of crashing.

## Treasurer page

`treasurer-k7m2x9/` is an unlinked page where the treasurer types a PIN, adds or fixes donations and presses **Save**. `functions/api/treasurer.js` (a Cloudflare Pages Function) checks the PIN and commits the new `donations.yml` to GitHub, which redeploys the site in about a minute.

It needs two secrets in Cloudflare Pages (Settings > Variables and Secrets): `TREASURER_PIN` and `GITHUB_TOKEN` (a fine-grained token with Contents read and write on this repo only). A 4-digit PIN is light protection, so keep the link private.

## Placeholders to replace

- `assets/mv-logo.svg`: stand-in Mustangs crest. Replace with the official Monte Vista logo.
- `assets/photos/photo-1.svg` … `photo-6.svg`: illustrated volleyball scenes. Replace with team photos.
- `assets/qr-venmo.svg`, `assets/qr-zelle.svg`: sample codes that do not scan. Replace with the real QR codes.
- `assets/sponsors/*.svg`: sponsor logo slots.
- Names, schedule and payment handles live in `tools/content.py`.
- `donations.yml` starts with sample donors. Replace them with the real ones.

## Rebuilding

```sh
python3 tools/build_assets.py   # regenerates the placeholder images
python3 tools/build_site.py     # regenerates index.html
```

The page loads `donations.yml` over the web, so open the site through a web server (or the Cloudflare preview), not by double-clicking `index.html`.
