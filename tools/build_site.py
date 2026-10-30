"""Build the MV Boys Volleyball fundraising site (Scoreboard design) into index.html."""
from pathlib import Path

from fragments import *  # noqa: F401,F403

OUT = Path(__file__).resolve().parent.parent
FONTS = "family=Orbitron:wght@700;900&family=Roboto+Condensed:wght@400;700"


def site():
    css = """
body{font-family:'Roboto Condensed',sans-serif;background:#1a1a1a;color:#f2f2f2}
h1,h2,h3{font-family:Orbitron,sans-serif;text-transform:uppercase;margin:0 0 .5em;letter-spacing:.04em}
h2{color:#ffcf3f;font-size:1.4rem}
.wrap{max-width:1100px;margin:auto;padding:48px 16px}
.board{max-width:1100px;margin:24px auto;background:#050505;border:10px solid #333;border-radius:14px;padding:24px 16px;box-shadow:inset 0 0 40px #000,0 10px 40px #000a}
.board-top{display:flex;align-items:center;justify-content:center;gap:16px;text-align:center}.board-top img{width:110px;flex:none}@media (max-width:600px){.board-top img{width:64px}}
.board h1{font-size:clamp(1.2rem,3.5vw,2.2rem);color:#fff}
.score{display:grid;grid-template-columns:1fr auto 1fr;gap:16px;align-items:center;margin:24px 0;text-align:center}
.score label{display:block;font-family:Orbitron;font-size:.8rem;color:#C8102E;letter-spacing:.2em}
.led{font-family:Orbitron;font-weight:900;font-size:clamp(2rem,7vw,4.5rem);color:#ff2a44;text-shadow:0 0 12px #ff2a44,0 0 30px #C8102E;background:#120004;padding:8px 16px;border-radius:8px;display:inline-block}
.led.amber{color:#ffcf3f;text-shadow:0 0 12px #ffcf3f;background:#140f00}
.vs{font-family:Orbitron;font-size:1.2rem;opacity:.6}
.periods{display:flex;justify-content:center;gap:28px;font-family:Orbitron;font-size:.8rem;flex-wrap:wrap}.periods b{display:block;font-size:1.6rem;color:#ffcf3f}
.progress-track{height:14px;background:#222;border:2px solid #444;margin:8px 0}.progress-fill{height:100%;background:repeating-linear-gradient(90deg,#ff2a44 0 10px,#C8102E 10px 14px)}.progress-nums,.progress-meta{display:none}
.nav{display:flex;justify-content:center;gap:4px;flex-wrap:wrap;margin-top:18px}.nav a{font-family:Orbitron;font-size:.7rem;padding:8px 12px;background:#222;text-decoration:none;border-radius:4px}.nav a:hover{background:#C8102E}
.qr{align-items:center;flex-wrap:nowrap}.qr-mascot{flex:1 1 140px;min-width:0;max-width:220px;width:100%;height:auto}.donate{display:grid;grid-template-columns:1fr 1fr;gap:32px;align-items:start}
.amounts{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin:16px 0}.amounts-btn{font-family:Orbitron;text-align:center;background:#C8102E;padding:14px 0;text-decoration:none;border-radius:6px;border-bottom:4px solid #7a0a1c}
.qr-card{background:#0a0a0a;padding:12px;border:2px solid #333;border-radius:8px}
.uses{list-style:none;padding:0}.uses li{display:flex;gap:14px;padding:12px;background:#222;margin-bottom:8px;border-radius:6px}.uses p{margin:0;opacity:.7;font-size:.9rem}
.coaches{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:16px}.coaches-card{background:#222;border-radius:8px;overflow:hidden;display:flex}.coaches-photo{flex:none;background:#C8102E;padding:16px;display:grid;place-items:center}.coaches-photo img{width:54px}.coaches-body{padding:14px}.coaches-role{color:#ffcf3f;font-size:.85rem}.coaches-body p{font-size:.85rem;opacity:.7;margin:.4em 0 0}
.sched{list-style:none;padding:0;display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:10px}
.sched li{display:flex;gap:12px;background:#050505;border:2px solid #333;border-radius:8px;padding:12px}.sched li.home{border-color:#C8102E}
.sched-date{font-family:Orbitron;color:#ffcf3f;text-align:center;min-width:50px}.sched-date span{display:block;font-size:.7rem}.sched-date b{font-size:1.5rem}.sched-info{display:flex;flex-direction:column}.sched-info span{font-size:.8rem;opacity:.6}
.gallery{display:grid;grid-template-columns:repeat(3,1fr);gap:10px}.gallery figure{border:4px solid #333;border-radius:6px;overflow:hidden}.gallery img{aspect-ratio:4/3;object-fit:cover}.gallery figcaption{font-family:Orbitron;font-size:.65rem;padding:6px;background:#050505}.gallery .featured{grid-column:1/-1}.gallery .featured img{aspect-ratio:3/2;object-position:center 55%}
.tiers{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:10px;margin-bottom:20px}.tiers-card{background:#222;border-radius:8px;padding:14px;border-top:4px solid #ffcf3f}.tiers-amt{font-family:Orbitron;color:#ff2a44}.tiers-card p{font-size:.85rem;opacity:.8}
.sponsors{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:8px}.sponsors img{border-radius:6px}
.footer{display:flex;gap:16px;max-width:1100px;margin:auto;padding:24px 16px;align-items:center;border-top:2px solid #333}.footer p{margin:.2em 0}
.fund-error{text-align:center;color:#ffcf3f;font-size:.85rem}
.wall{list-style:none;padding:0;display:grid;grid-template-columns:repeat(auto-fill,minmax(180px,1fr));gap:8px}.wall li{background:#222;border-left:4px solid #C8102E;border-radius:6px;padding:10px 12px;display:flex;justify-content:space-between;gap:8px}.wall-amt{font-family:Orbitron;color:#ffcf3f;font-size:.85rem}
@media(max-width:760px){.donate{grid-template-columns:1fr}.gallery{grid-template-columns:1fr}.score{grid-template-columns:1fr}.vs{display:none}}
"""
    body = f"""
<section class="board" id="donate">
 <div class="board-top"><img src="{LOGO}" alt="Monte Vista logo"><h1>Monte Vista High Mustangs Volleyball<br>{SEASON} Fundraiser</h1><img src="{BALL}" alt=""></div>
 <div class="score"><div><label>RAISED</label><span class="led" data-fund="raised">{RAISED:,}</span></div><div class="vs">OF</div><div><label>GOAL</label><span class="led amber" data-fund="goal">{GOAL:,}</span></div></div>
 {progress()}
 <div class="periods"><div>DONORS<b data-fund="donors">{DONORS}</b></div><div>FUNDED<b><span data-fund="pct">{PCT}</span>%</b></div><div>SET<b>1</b></div></div>
 <p class="fund-error" data-fund="error" hidden>Fundraiser totals could not be loaded. Check donations.yml.</p>
 {nav(items=("Sponsors","Coaches","Photos","Schedule","Supporters"))}
</section>
<section class="wrap"><div class="donate"><div><h2>PICK YOUR DONATION</h2>{amounts()}{uses()}</div><div><h2>Scan to give</h2>{qr_pair()}</div></div></section>
<section class="wrap" id="sponsors"><h2>Sponsors</h2>{tiers()}{sponsors()}</section>
<section class="wrap" id="coaches"><h2>Coaching staff</h2>{coaches()}</section>
<section class="wrap" id="photos"><h2>Team Photos</h2>{photos()}</section>
<section class="wrap" id="schedule"><h2>Match schedule</h2>{schedule_list()}</section>
<section class="wrap" id="supporters" data-fund="wall-section" hidden><h2>Supporter wall</h2><p class="fine">Thank you to everyone backing the Mustangs.</p><ul class="wall" data-fund="wall"></ul></section>
{footer()}
<script src="assets/js-yaml.min.js"></script>
<script src="assets/fundraiser.js"></script>
"""
    return css, body


if __name__ == "__main__":
    css, body = site()
    html = page(f"{TEAM} Fundraiser", FONTS, css, body)
    (OUT / "index.html").write_text(html)
    print("built index.html")
