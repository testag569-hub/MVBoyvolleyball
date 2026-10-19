"""Generate placeholder SVG assets: team logo, volleyball photos, donation QR codes.

Every file here is a stand-in. Replace assets/mv-logo.svg with the official
Monte Vista logo, assets/photos/*.svg with real team photos, and
assets/qr-*.svg with the real Zelle / Venmo QR codes.
"""
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "assets"
RED, BLACK, WHITE = "#C8102E", "#111111", "#FFFFFF"


def write(name, svg):
    path = ROOT / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(svg.strip() + "\n")


LOGO = f"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 230" role="img" aria-label="Monte Vista Mustangs logo (placeholder)">
  <path d="M100 6 L190 36 V120 C190 172 150 206 100 224 C50 206 10 172 10 120 V36 Z" fill="{BLACK}"/>
  <path d="M100 18 L178 44 V120 C178 164 144 194 100 210 C56 194 22 164 22 120 V44 Z" fill="{RED}"/>
  <path d="M100 30 L166 52 V118 C166 156 138 182 100 196 C62 182 34 156 34 118 V52 Z" fill="{WHITE}"/>
  <text x="100" y="128" text-anchor="middle" font-family="Georgia, 'Times New Roman', serif" font-weight="700" font-size="72" fill="{BLACK}" letter-spacing="-4">MV</text>
  <rect x="34" y="142" width="132" height="26" fill="{BLACK}"/>
  <text x="100" y="161" text-anchor="middle" font-family="Arial Black, Arial, sans-serif" font-weight="900" font-size="15" fill="{WHITE}" letter-spacing="3">MUSTANGS</text>
  <text x="100" y="186" text-anchor="middle" font-family="Arial, sans-serif" font-weight="700" font-size="10" fill="{RED}" letter-spacing="2">BOYS VOLLEYBALL</text>
</svg>
"""


def ball(cx, cy, r, extra=""):
    # A volleyball: white sphere with three curved panel seams.
    return f"""
  <g {extra}>
    <circle cx="{cx}" cy="{cy}" r="{r}" fill="#fafafa" stroke="#222" stroke-width="{r*0.06:.1f}"/>
    <path d="M{cx} {cy-r} C{cx+r*0.55} {cy-r*0.4} {cx+r*0.5} {cy+r*0.3} {cx+r*0.15} {cy+r*0.98}" fill="none" stroke="#222" stroke-width="{r*0.05:.1f}"/>
    <path d="M{cx-r*0.95} {cy-r*0.3} C{cx-r*0.35} {cy-r*0.05} {cx+r*0.3} {cy-r*0.1} {cx+r*0.92} {cy-r*0.4}" fill="none" stroke="#222" stroke-width="{r*0.05:.1f}"/>
    <path d="M{cx-r*0.75} {cy+r*0.65} C{cx-r*0.4} {cy+r*0.1} {cx+r*0.05} {cy-r*0.25} {cx+r*0.5} {cy-r*0.15}" fill="none" stroke="#222" stroke-width="{r*0.05:.1f}"/>
    <path d="M{cx} {cy-r} C{cx+r*0.55} {cy-r*0.4} {cx+r*0.5} {cy+r*0.3} {cx+r*0.15} {cy+r*0.98} L{cx+r*0.6} {cy+r*0.78} C{cx+r*0.9} {cy+r*0.2} {cx+r*0.8} {cy-r*0.5} {cx} {cy-r} Z" fill="{RED}" opacity="0.9"/>
    <path d="M{cx-r*0.95} {cy-r*0.3} C{cx-r*0.35} {cy-r*0.05} {cx+r*0.3} {cy-r*0.1} {cx+r*0.92} {cy-r*0.4} L{cx+r*0.6} {cy-r*0.8} C{cx} {cy-r*0.6} {cx-r*0.6} {cy-r*0.7} {cx-r*0.95} {cy-r*0.3} Z" fill="{BLACK}" opacity="0.85"/>
  </g>"""


def player(x, y, s, pose, color):
    # Very simple athlete silhouette; pose is "spike", "block" or "dig".
    head = f'<circle cx="{x}" cy="{y}" r="{11*s}" fill="{color}"/>'
    if pose == "spike":
        body = (f'<path d="M{x} {y+12*s} L{x-6*s} {y+60*s} L{x-24*s} {y+100*s} M{x-6*s} {y+60*s} L{x+14*s} {y+98*s} '
                f'M{x} {y+20*s} L{x+30*s} {y-24*s} M{x} {y+22*s} L{x-30*s} {y+2*s}" stroke="{color}" stroke-width="{12*s}" stroke-linecap="round" fill="none"/>')
    elif pose == "block":
        body = (f'<path d="M{x} {y+12*s} L{x} {y+62*s} L{x-12*s} {y+108*s} M{x} {y+62*s} L{x+12*s} {y+108*s} '
                f'M{x-4*s} {y+18*s} L{x-12*s} {y-34*s} M{x+4*s} {y+18*s} L{x+12*s} {y-34*s}" stroke="{color}" stroke-width="{12*s}" stroke-linecap="round" fill="none"/>')
    else:
        body = (f'<path d="M{x} {y+12*s} L{x-14*s} {y+50*s} L{x-40*s} {y+64*s} L{x-40*s} {y+92*s} M{x-14*s} {y+50*s} L{x+20*s} {y+70*s} L{x+24*s} {y+94*s} '
                f'M{x} {y+20*s} L{x+34*s} {y+40*s}" stroke="{color}" stroke-width="{12*s}" stroke-linecap="round" fill="none"/>')
    return head + body


def photo(seed, title):
    rnd = random.Random(seed)
    w, h = 1200, 800
    bg = rnd.choice([("#2a0a10", "#7a0f1f"), ("#0d0d0d", "#3a3a3a"), ("#3b0b14", "#c8102e"), ("#151515", "#5a1420")])
    floor = rnd.choice(["#b8865b", "#c99a6b", "#a9744c"])
    poses = ["spike", "block", "dig"]
    figures = "".join(
        player(rnd.randint(180, 1020), rnd.randint(330, 420), rnd.uniform(1.4, 1.9), rnd.choice(poses), rnd.choice([RED, BLACK, "#f4f4f4"]))
        for _ in range(rnd.randint(2, 4))
    )
    lights = "".join(
        f'<circle cx="{x}" cy="40" r="22" fill="#fff" opacity="0.18"/><circle cx="{x}" cy="40" r="8" fill="#fff" opacity="0.6"/>'
        for x in range(100, w, 200)
    )
    return f"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" preserveAspectRatio="xMidYMid slice" role="img" aria-label="{title} (placeholder photo)">
  <defs>
    <linearGradient id="g{seed}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{bg[0]}"/><stop offset="1" stop-color="{bg[1]}"/></linearGradient>
    <linearGradient id="f{seed}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{floor}"/><stop offset="1" stop-color="#6b4528"/></linearGradient>
  </defs>
  <rect width="{w}" height="{h}" fill="url(#g{seed})"/>
  {lights}
  <rect y="560" width="{w}" height="240" fill="url(#f{seed})"/>
  <path d="M0 640 H{w}" stroke="#fff" stroke-width="5" opacity="0.6"/>
  <rect x="{w/2-5}" y="250" width="10" height="330" fill="#ddd"/>
  <rect x="80" y="300" width="{w-160}" height="110" fill="none" stroke="#eee" stroke-width="3" opacity="0.5"/>
  <path d="M80 300 H{w-80}" stroke="#fff" stroke-width="10"/>
  {"".join(f'<path d="M{x} 300 V410" stroke="#eee" stroke-width="1.5" opacity="0.4"/>' for x in range(100, w - 80, 22))}
  {"".join(f'<path d="M80 {y} H{w-80}" stroke="#eee" stroke-width="1.5" opacity="0.4"/>' for y in range(322, 410, 22))}
  {figures}
  {ball(rnd.randint(300, 900), rnd.randint(120, 220), 46)}
  <rect x="24" y="{h-64}" width="260" height="40" rx="6" fill="#000" opacity="0.55"/>
  <text x="40" y="{h-37}" font-family="Arial, sans-serif" font-size="20" fill="#fff">Photo placeholder</text>
</svg>
"""


def qr(seed, label, color):
    # Looks like a QR code but encodes nothing, so it can't send money anywhere by mistake.
    rnd = random.Random(seed)
    n, cell = 25, 8
    cells = []
    finder = lambda r, c: (r < 7 and c < 7) or (r < 7 and c >= n - 7) or (r >= n - 7 and c < 7)
    for r in range(n):
        for c in range(n):
            if not finder(r, c) and rnd.random() < 0.48:
                cells.append(f'<rect x="{16+c*cell}" y="{16+r*cell}" width="{cell}" height="{cell}"/>')
    def eye(x, y):
        return (f'<rect x="{x}" y="{y}" width="56" height="56" fill="#111"/><rect x="{x+8}" y="{y+8}" width="40" height="40" fill="#fff"/>'
                f'<rect x="{x+16}" y="{y+16}" width="24" height="24" fill="#111"/>')
    size = 16 * 2 + n * cell
    return f"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {size} {size+34}" role="img" aria-label="{label} QR code placeholder">
  <rect width="{size}" height="{size+34}" rx="12" fill="#fff"/>
  <g fill="#111">{''.join(cells)}</g>
  {eye(16, 16)}{eye(16+(n-7)*cell, 16)}{eye(16, 16+(n-7)*cell)}
  <rect x="{size/2-44}" y="{size/2-14}" width="88" height="28" rx="6" fill="{color}"/>
  <text x="{size/2}" y="{size/2+5}" text-anchor="middle" font-family="Arial, sans-serif" font-weight="700" font-size="14" fill="#fff">{label}</text>
  <text x="{size/2}" y="{size+22}" text-anchor="middle" font-family="Arial, sans-serif" font-size="12" fill="#c8102e" font-weight="700">SAMPLE · NOT A REAL CODE</text>
</svg>
"""


SPONSOR_SHAPES = [
    lambda name: f'<circle cx="40" cy="40" r="26" fill="#ccc"/><text x="80" y="48" font-size="22" font-family="Arial Black, Arial" fill="#888">{name}</text>',
    lambda name: f'<rect x="14" y="16" width="48" height="48" rx="10" fill="#ccc"/><text x="80" y="48" font-size="22" font-family="Georgia, serif" font-weight="700" fill="#888">{name}</text>',
    lambda name: f'<path d="M14 64 L40 14 L66 64 Z" fill="#ccc"/><text x="80" y="48" font-size="22" font-family="Arial, sans-serif" font-weight="700" fill="#888">{name}</text>',
]


def sponsor(i):
    name = f"Your Logo {i}"
    shape = SPONSOR_SHAPES[i % len(SPONSOR_SHAPES)](name)
    return f"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 80" role="img" aria-label="Sponsor logo placeholder {i}">
  <rect width="300" height="80" fill="#f3f3f3"/>
  {shape}
</svg>
"""


if __name__ == "__main__":
    write("mv-logo.svg", LOGO)
    write("volleyball.svg", f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">{ball(50, 50, 46)}</svg>')
    titles = ["Spike at the net", "Team huddle", "Block at the net", "Serve receive", "Senior night", "Tournament day"]
    for i, t in enumerate(titles, 1):
        write(f"photos/photo-{i}.svg", photo(i * 7, t))
    write("qr-venmo.svg", qr(11, "VENMO", "#008CFF"))
    write("qr-zelle.svg", qr(23, "ZELLE", "#6D1ED4"))
    for i in range(1, 9):
        write(f"sponsors/sponsor-{i}.svg", sponsor(i))
