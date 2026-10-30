"""Placeholder content for the fundraising site.

Edit the values here (names, schedule, payment handles) and rerun
build_site.py to update index.html. Donations and the goal live in
donations.yml instead, which needs no rebuild.
"""

A = "assets"

TEAM = "Monte Vista Boys Volleyball"
SHORT = "MV Boys Volleyball"
SEASON = "2027 Season"
TAGLINE = "Help the Mustangs serve up a winning season."

# The live goal and donations are in donations.yml at the top of the repo; the
# page reads that file when it loads. These numbers only show if it fails to load.
GOAL = 15000
RAISED = 6250
PCT = round(RAISED / GOAL * 100)
DONORS = 48

VENMO = "@MV-Boys-Volleyball"

USES = [
    ("Tournament fees", "Entry into invitationals and travel tournaments.", 35),
    ("Uniforms & gear", "Jerseys, warmups and knee pads for every player.", 25),
    ("Equipment", "New match balls, ball carts and training tools.", 20),
    ("Travel", "Bus rides and meals for away tournaments.", 20),
]

TIERS = [
    ("Gold", 1000, "Large logo on site and banner at home matches, plus a team-signed ball."),
    ("Silver", 500, "Medium logo on site and a shout-out at home matches."),
    ("Bronze", 250, "Logo on the sponsor wall of this site."),
    ("Mustang Family", 100, "Name listed on the supporter wall."),
]

AMOUNTS = [25, 50, 100, 250, 500]

COACHES = [
    ("Maile Farrales", "Head Coach", "Leads the varsity program. Bio coming soon."),
    ("Coach Name", "Assistant Coach", "Works with hitters and blockers. Bio coming soon."),
    ("Coach Name", "JV Head Coach", "Develops the next wave of Mustangs. Bio coming soon."),
]

POSITIONS = ["OH", "MB", "S", "OPP", "L", "DS", "OH", "MB", "OH", "S", "MB", "OPP", "L", "OH"]
GRADES = ["Sr", "Sr", "Jr", "Sr", "Jr", "So", "Jr", "Sr", "So", "Jr", "Jr", "So", "Sr", "Fr"]
NUMBERS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15]
PLAYERS = [(n, "Player Name", p, g) for n, p, g in zip(NUMBERS, POSITIONS, GRADES)]
POS_NAMES = {"OH": "Outside Hitter", "MB": "Middle Blocker", "S": "Setter", "OPP": "Opposite",
             "L": "Libero", "DS": "Defensive Specialist"}

# Sample schedule only; replace with the real one.
SCHEDULE = [
    ("Feb 23", "Tue", "Granada", "Home", "6:00 PM"),
    ("Feb 25", "Thu", "Foothill", "Away", "6:00 PM"),
    ("Mar 2", "Tue", "Dublin", "Home", "6:00 PM"),
    ("Mar 6", "Sat", "Spring Invitational", "Tournament", "8:00 AM"),
    ("Mar 9", "Tue", "San Ramon Valley", "Away", "6:00 PM"),
    ("Mar 11", "Thu", "Cal High", "Home", "6:00 PM"),
    ("Mar 16", "Tue", "Dougherty Valley", "Away", "6:00 PM"),
    ("Mar 18", "Thu", "De La Salle", "Home", "6:00 PM"),
    ("Mar 23", "Tue", "Amador Valley", "Away", "6:00 PM"),
    ("Apr 13", "Tue", "Livermore", "Home", "6:00 PM"),
    ("Apr 15", "Thu", "Senior Night vs. Granada", "Home", "6:00 PM"),
]

PHOTOS = [f"{A}/photos/photo-{i}.svg" for i in range(1, 7)]
PHOTO_ALTS = ["Spike at the net", "Team huddle", "Block at the net", "Serve receive", "Senior night", "Tournament day"]
SPONSORS = [f"{A}/sponsors/sponsor-{i}.svg" for i in range(1, 9)]
LOGO = f"{A}/mv-logo.svg"
BALL = f"{A}/volleyball.svg"
QR_VENMO = f"{A}/qr-venmo.svg"
OFFICIAL = "https://mvhs.srvusd.net/Athletics/Team-Sports/Spring-Sports/Volleyball-Boys/index.html"


def money(n):
    return f"${n:,}"
