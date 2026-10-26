// Fills in the scoreboard (raised, goal, donors, percent) and the supporter
// wall from donations.yml. If that file is missing or has a typo, the
// build-time numbers stay and a short notice appears on the scoreboard.
(function () {
  var cfg = {};
  var all = function (k) { return document.querySelectorAll('[data-fund="' + k + '"]'); };
  var set = function (k, v) { all(k).forEach(function (el) { el.textContent = v; }); };
  var num = function (v) { var n = parseFloat(String(v == null ? '' : v).replace(/[$,\s]/g, '')); return isFinite(n) ? n : 0; };
  var fmt = function (n) { return Math.round(n).toLocaleString('en-US'); };
  var yes = function (v) { return v === true || /^\s*(y|yes|x|true|1)\s*$/i.test(String(v == null ? '' : v)); };
  var no = function (v) { return v === false || /^\s*(n|no|false|0)\s*$/i.test(String(v == null ? '' : v)); };
  var fail = function () { all('error').forEach(function (el) { el.hidden = false; }); };

  function render(goal, list) {
    var raised = 0, names = {}, extra = 0;
    list.forEach(function (d) {
      raised += num(d.amount);
      var key = String(d.name || '').trim().toLowerCase();
      if (key) names[key] = 1; else extra += 1;
    });
    var donors = Object.keys(names).length + extra, pct = Math.round(raised / goal * 100);

    set('raised', fmt(raised)); set('goal', fmt(goal));
    set('raised-money', '$' + fmt(raised)); set('goal-money', '$' + fmt(goal));
    set('donors', donors); set('pct', pct);
    all('bar').forEach(function (el) { el.style.width = Math.min(pct, 100) + '%'; });
    all('label').forEach(function (el) { el.setAttribute('aria-label', '$' + fmt(raised) + ' raised of $' + fmt(goal) + ' goal'); });

    var wall = document.querySelector('[data-fund="wall"]');
    if (!wall) return;
    wall.textContent = '';
    var show = !no(cfg.show_supporter_wall) && list.length > 0;
    all('wall-section').forEach(function (el) { el.hidden = !show; });
    if (!show) return;
    list.forEach(function (d) {
      var li = document.createElement('li'), who = document.createElement('span');
      who.textContent = yes(d.anonymous) || !String(d.name || '').trim() ? 'Anonymous' : String(d.name).trim();
      li.appendChild(who);
      if (yes(cfg.show_amounts)) { var amt = document.createElement('span'); amt.className = 'wall-amt'; amt.textContent = '$' + fmt(num(d.amount)); li.appendChild(amt); }
      wall.appendChild(li);
    });
  }

  function load(text) {
    cfg = window.jsyaml.load(text) || {};
    var goal = num(cfg.goal);
    if (!goal) throw new Error('donations.yml has no goal');
    var list = (Array.isArray(cfg.donations) ? cfg.donations : []).filter(function (d) { return d && typeof d === 'object'; });
    render(goal, list);
  }

  if (!window.fetch || !window.jsyaml) return fail();
  fetch('donations.yml', { cache: 'no-cache' })
    .then(function (r) { if (!r.ok) throw new Error('donations.yml returned ' + r.status); return r.text(); })
    .then(load)
    .catch(function (e) { console.error('Could not read donations.yml:', e); fail(); });
})();
