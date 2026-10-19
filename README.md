# Monte Vista Boys Volleyball Fundraising Site

The fundraising site for MV Boys Volleyball. Open `index.html` to view it.

It has a donate section with Venmo and Zelle QR codes, sponsor levels and logos, photos, coaches, the roster and the schedule.

## Placeholders to replace

- `assets/mv-logo.svg`: stand-in Mustangs crest. Replace with the official Monte Vista logo.
- `assets/photos/photo-1.svg` … `photo-6.svg`: illustrated volleyball scenes. Replace with team photos.
- `assets/qr-venmo.svg`, `assets/qr-zelle.svg`: sample codes that do not scan. Replace with the real QR codes.
- `assets/sponsors/*.svg`: sponsor logo slots.
- Names, schedule, fundraising goal and payment handles live in `tools/content.py`.

## Rebuilding

```sh
python3 tools/build_assets.py   # regenerates the placeholder images
python3 tools/build_site.py     # regenerates index.html
```
