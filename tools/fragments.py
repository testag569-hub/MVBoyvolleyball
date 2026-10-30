"""HTML building blocks for the site's sections, styled by the CSS in build_site.py."""
from content import *  # noqa: F401,F403


def progress(cls="progress"):
    return f"""
<div class="{cls}" role="img" aria-label="{money(RAISED)} raised of {money(GOAL)} goal" data-fund="label">
  <div class="{cls}-nums"><strong data-fund="raised-money">{money(RAISED)}</strong> raised of <span data-fund="goal-money">{money(GOAL)}</span> goal</div>
  <div class="{cls}-track"><div class="{cls}-fill" style="width:{PCT}%" data-fund="bar"></div></div>
  <div class="{cls}-meta"><span data-fund="pct">{PCT}</span>% funded · <span data-fund="donors">{DONORS}</span> donors</div>
</div>"""


def amounts(cls="amounts"):
    btns = "".join(f'<a class="{cls}-btn" href="#donate">{money(a)}</a>' for a in AMOUNTS)
    return f'<div class="{cls}">{btns}<a class="{cls}-btn" href="#donate">Other</a></div>'


def qr_pair(cls="qr"):
    return f"""
<div class="{cls}">
  <figure class="{cls}-card">
    <img src="{QR_VENMO}" alt="Venmo QR code (placeholder)">
    <figcaption><strong>Venmo</strong><span>{VENMO}</span></figcaption>
  </figure>
</div>
<p class="{cls}-note">Please add “MV Boys Volleyball” and your name in the payment note.</p>"""


def uses(cls="uses"):
    items = "".join(
        f'<li><span class="{cls}-pct">{p}%</span><div><strong>{t}</strong><p>{d}</p></div></li>' for t, d, p in USES
    )
    return f'<ul class="{cls}">{items}</ul>'


def tiers(cls="tiers"):
    cards = "".join(
        f'<div class="{cls}-card {cls}-{n.split()[0].lower()}"><h3>{n}</h3><div class="{cls}-amt">{money(a)}+</div><p>{d}</p></div>'
        for n, a, d in TIERS
    )
    return f'<div class="{cls}">{cards}</div>'


def sponsors(cls="sponsors", count=8):
    logos = "".join(f'<img src="{s}" alt="Sponsor logo placeholder">' for s in SPONSORS[:count])
    return f'<div class="{cls}">{logos}</div>'


def photos(cls="gallery", count=6, start=0):
    pics = "".join(
        f'<figure><img src="{PHOTOS[(start+i) % 6]}" alt="{PHOTO_ALTS[(start+i) % 6]}"><figcaption>{PHOTO_ALTS[(start+i) % 6]}</figcaption></figure>'
        for i in range(count)
    )
    return f'<div class="{cls}">{pics}</div>'


def coaches(cls="coaches"):
    cards = "".join(
        f'<article class="{cls}-card"><div class="{cls}-photo"><img src="{LOGO}" alt=""></div>'
        f'<div class="{cls}-body"><h3>{n}</h3><div class="{cls}-role">{r}</div><p>{b}</p></div></article>'
        for n, r, b in COACHES
    )
    return f'<div class="{cls}">{cards}</div>'


def roster_cards(cls="roster"):
    cards = "".join(
        f'<div class="{cls}-card"><div class="{cls}-num">{n}</div><div class="{cls}-name">{name}</div>'
        f'<div class="{cls}-pos">{POS_NAMES[p]} · {g}</div></div>'
        for n, name, p, g in PLAYERS
    )
    return f'<div class="{cls}">{cards}</div>'


def roster_table(cls="roster-table"):
    rows = "".join(f"<tr><td>{n}</td><td>{name}</td><td>{POS_NAMES[p]}</td><td>{g}</td></tr>" for n, name, p, g in PLAYERS)
    return f'<div class="table-wrap"><table class="{cls}"><thead><tr><th>#</th><th>Name</th><th>Position</th><th>Year</th></tr></thead><tbody>{rows}</tbody></table></div>'


def schedule_table(cls="schedule"):
    rows = "".join(
        f'<tr class="{h.lower()}"><td>{d}</td><td>{dow}</td><td>{o}</td><td><span class="tag tag-{h.lower()}">{h}</span></td><td>{t}</td></tr>'
        for d, dow, o, h, t in SCHEDULE
    )
    return (f'<div class="table-wrap"><table class="{cls}"><thead><tr><th>Date</th><th>Day</th><th>Opponent</th><th>Site</th><th>Time</th></tr></thead>'
            f'<tbody>{rows}</tbody></table></div><p class="fine">Sample schedule. Real dates coming soon.</p>')


def schedule_list(cls="sched"):
    items = "".join(
        f'<li class="{h.lower()}"><div class="{cls}-date"><span>{d.split()[0]}</span><b>{d.split()[1]}</b></div>'
        f'<div class="{cls}-info"><strong>{"vs." if h == "Home" else "@" if h == "Away" else ""} {o}</strong><span>{dow} · {t} · {h}</span></div></li>'
        for d, dow, o, h, t in SCHEDULE
    )
    return f'<ul class="{cls}">{items}</ul><p class="fine">Sample schedule. Real dates coming soon.</p>'


def nav(cls="nav", items=("Donate", "Team", "Coaches", "Schedule", "Photos", "Sponsors")):
    links = "".join(f'<a href="#{i.lower()}">{i}</a>' for i in items)
    return f'<nav class="{cls}">{links}</nav>'


def footer(cls="footer"):
    return f"""
<footer class="{cls}">
  <img src="{LOGO}" alt="" width="48" height="55">
  <div>
    <strong>{TEAM}</strong>
    <p>Monte Vista High School · Danville, CA · <a href="{OFFICIAL}">Official team page</a></p>
    <p class="fine">Donations support the team through the program's booster account. Placeholder content shown.</p>
  </div>
</footer>"""


BASE_CSS = """
*,*::before,*::after{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;-webkit-font-smoothing:antialiased}
img{max-width:100%;display:block}
a{color:inherit}
figure{margin:0}
.table-wrap{overflow-x:auto}
table{border-collapse:collapse;width:100%}
.fine{font-size:.8rem;opacity:.7}
.qr{display:flex;gap:16px;flex-wrap:wrap}
.qr-card{flex:1 1 140px;max-width:220px;text-align:center}
.qr-card figcaption{display:flex;flex-direction:column;margin-top:8px;font-size:.9rem}
.qr-card figcaption span{opacity:.75;word-break:break-all}
.qr-note{font-size:.85rem;opacity:.75}
"""


def page(title, fonts, css, body):
    font_link = (f'<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
                 f'<link href="https://fonts.googleapis.com/css2?{fonts}&display=swap" rel="stylesheet">') if fonts else ""
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<link rel="icon" href="{LOGO}">
{font_link}
<style>{BASE_CSS}{css}</style>
</head>
<body>
{body}
</body>
</html>
"""
