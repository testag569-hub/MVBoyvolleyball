// =====================================================================
//  MV BOYS VOLLEYBALL FUNDRAISER: DONATIONS AND GOAL
// =====================================================================
//
//  This is the only file you need to edit to update the fundraiser.
//  The website adds everything up for you: the total raised, the
//  number of donors and the percent of the goal.
//
//  HOW TO EDIT ON GITHUB
//    1. Open this file on github.com and click the pencil icon (Edit).
//    2. Change the goal, or add a line to the donations list.
//    3. Click "Commit changes". The site updates on its next deploy.
//
//  RULES THAT KEEP THE PAGE WORKING
//    - Copy an existing donation line and change it. Keep the { } and
//      the comma at the end of the line.
//    - Words go in "quotes". Amounts are plain numbers: 50 or 1250.50,
//      with no $ sign and no commas.
//    - Lines that start with // are notes. The website ignores them.
// =====================================================================

window.FUNDRAISER = {

  // The fundraising goal in dollars.
  goal: 15000,

  // Show each donor's name on the "Supporter wall" section of the page.
  // Set to false to hide the wall.
  showSupporterWall: true,

  // Also show how much each person gave on the supporter wall.
  showAmounts: false,

  // Money that came in without a name to list (cash at a match, a
  // bake sale, and so on). It counts toward the total and the donor
  // count but does not appear on the supporter wall.
  otherDonations: {
    amount: 0,
    donors: 0,
  },

  // One line per donation.
  //   name:      who gave (shown on the supporter wall)
  //   amount:    dollars
  //   method:    "Venmo", "Zelle", "Check", "Cash" or anything you like
  //   date:      optional, for your own records, like "2026-10-26"
  //   anonymous: optional. Put  anonymous: true  to count the money
  //              but show "Anonymous" instead of the name.
  //
  // The same person giving twice counts as one donor if the name is
  // spelled the same way both times.
  //
  // SAMPLE DONATIONS BELOW: replace them with the real ones.
  donations: [
    { name: "The Rivera Family",   amount: 250,  method: "Venmo", date: "2026-10-01" },
    { name: "Danville Pizza Co.",  amount: 1000, method: "Check", date: "2026-10-03" },
    { name: "Jordan Lee",          amount: 50,   method: "Zelle", date: "2026-10-05" },
    { name: "Coach's Corner",      amount: 500,  method: "Check", date: "2026-10-08" },
    { name: "Sam Patel",           amount: 100,  method: "Venmo", date: "2026-10-12", anonymous: true },
    { name: "The Nguyen Family",   amount: 100,  method: "Zelle", date: "2026-10-15" },
    { name: "Alex Kim",            amount: 25,   method: "Cash",  date: "2026-10-20" },
  ],

};
