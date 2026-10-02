# Design: Werte von neoteq.de

Ausgelesen am 2026-10-02 aus www.neoteq.de (`/de/`, `/en/`, `/de/pitchdeck`, `/en/pitchdeck`, `/de/impressum`, `/en/imprint`).
Quellen: die CSS-Dateien von neoteq.de und die im Browser berechneten Styles (headless Chrome, 1440 / 1100 / 390 px).

- `typo3conf/ext/base/Resources/Public/Css/app.css` (Tailwind-Build, Hauptquelle)
- `typo3conf/ext/base/Resources/Public/Css/styles.css` (Overrides, u. a. Abstände im Header)
- `typo3temp/assets/css/7015c8c4ac5ff815b57530b221005fc6.css` (TYPO3-Standard, nicht relevant)

Unser `assets/style.css` übernimmt diese Regeln 1:1. Abweichungen stehen ganz unten.

## Farben

| Rolle | Wert | Wo auf neoteq.de |
|---|---|---|
| Text, Logo, Buttons, Menü-Knopf | `#343a40` (rgb 52 58 64) | Desktop überall |
| Hintergrund | `#ffffff` | Desktop, Header |
| Petrol | `#0f3737` (rgb 15 55 55) | Footer-Box; mobil Seiten- und Header-Hintergrund |
| Türkis | `#2aced1` (rgb 42 206 209) | Footer-Links, Social-Icons; mobil Text, Logo, Buttons |
| Hellgrau | `#f0f0f0` | Menü-Overlay `hsla(0,0%,94%,.25)` mit `blur(15px)`, mobile Karten |
| Zweites Farbthema | `#46140a` / `#ff5722` | Braun/Orange, siehe „Mobil“ |
| Grautöne Tailwind | `#9ca3af`, `#e5e7eb` | nur Reset/Platzhalter, sichtbar nicht verwendet |
| Markierung | Hintergrund `#0f3737`, Text `#2aced1` | `::selection` |

Hinweis: Die Mail-Farben (`#0d3b3e`, `#3ddbd0`, `#eef3f3`) weichen leicht von der Website ab.
Die Seiten verwenden jetzt die Website-Werte (`#0f3737`, `#2aced1`).

## Schrift

Poppins, eigene Dateien von neoteq.de. Wir laden sie **direkt von dort** (CORS `*`, keine Cookies):

- `https://www.neoteq.de/typo3conf/ext/base/Resources/Public/Fonts/NTQ-Poppins-Black.woff2` → Gewicht 900
- `https://www.neoteq.de/typo3conf/ext/base/Resources/Public/Fonts/NTQ-Poppins-Medium.woff2` → Gewicht 500 **und** 400

Gewicht 700 (Footer-Links) hat keine eigene Datei. Der Browser nimmt Black, wie auf neoteq.de.

| Element | Desktop | Mobil (≤ 786 px) |
|---|---|---|
| Fließtext `body` | 36 px / 42 px, 500 | 21 px / 28 px |
| Überschrift `h2` (Unterseiten) | 36 px / 33 px, 900, Versalien, −0,4 px | 20 px / 18 px, −0,2 px |
| `h1` (nur Startseite) | 80 px / 72 px, 900, Versalien | 40 px / 36 px |
| Dachzeile `.text-dachzeile` | 30 px / 45 px, 400, Versalien | 21 px / 31,5 px |
| Kleintext `.text-body2` | 16 px / 24 px | 16 px / 24 px |
| Button | 16 px / 24 px, 500, Versalien | Zeilenhöhe 1, zentriert |
| Menüpunkte `.text-nav` | 60 px / 90 px, 900, Versalien | 40 px / 60 px |
| Footer-Links | 16 px / 24 px, 700, Versalien | gleich, untereinander |

Mobil gilt `hyphens: auto` für `main`.

## Raster und Abstände

- `.container`: 12 Spalten, `gap` 33 px, Innenabstand 33 px links/rechts, ab 1366 px `max-width: 1366px` zentriert, `margin-bottom: 10rem`.
  Mobil: `gap` 10 px, Innenabstand 22 px, `margin-bottom: 5rem`.
- Header fest oben (`position: fixed`), Innenabstand 25 px 33 px (mobil 25 px 22 px), Höhe 110,5 px (mobil 92,8 px).
- `main`: `margin-top: 200px` (mobil 92 px).
- Textblock `.mask_text .bodytext`: `margin-top: 160px`, `padding-left: 33%`, also Text ab x = 499 px bei 1440 px Breite.
  Bis 1200 px: `margin-top: 80px`, `padding-left: 0`.
- Überschrift `margin-bottom: 25px` (≤ 1200 px: 22 px), Dachzeile `margin-bottom: 35px`.
- Abstand Text → Button 33 px (mobil 28 px), aus `.mask_text_teaser`.

## Rundungen

| Element | Radius |
|---|---|
| Buttons | 24 px |
| Menü-Knopf | 20 px |
| Footer-Box | 16 px |

## Buttons

`.btn`: 1 px Rahmen in Textfarbe, transparent, Radius 24 px, Innenabstand 11 px 16 px (im Header 10 px 16 px), Versalien.
`.btn.arrow`: beim Hover wächst `padding-left` auf 48 px, von links schiebt sich der Pfeil `Icons/arrow.svg` (24 × 16) herein, 0,3 s.
Mobil steht der Pfeil immer da. `.btn.upload` funktioniert genauso mit `Icons/upload.svg` (32 × 24, `padding-left` 58 px).
Beim Hover färbt neoteq.de Elemente mit `.hover-effect` zufällig türkis oder orange. Wir nehmen fest Türkis.

## Header

- Links: Logo `Images/logo.svg`, 130 px breit (mobil 92 px). Es wird als CSS-Maske eingesetzt und damit eingefärbt (`#343a40`, mobil `#2aced1`).
- Rechts, Abstand jeweils 15 px: Button „Pitchdeck hochladen“ / „Upload your Pitchdeck“ (mobil ausgeblendet), Sprachknopf
  (nur die andere Sprache; mobil 12 px, Innenabstand 8 px 16 px), Menü-Knopf 85 × 40 (mobil 63 × 30) mit zwei Strichen 24 × 1 px.
- Menü offen: Overlay über die ganze Höhe, Hellgrau mit Unschärfe. Links bzw. mittig Mission, Portfolio, Team, NEOJOBS.
  Darunter die Logos Friday's Fifteen, neobib und founders dinner, unten die Footer-Links (nur Desktop) und Social-Icons (dunkel, 36 px).
  Der Menü-Knopf wird dabei zum X auf grauem Grund (mobil: türkiser Rahmen und türkises X). Mobil steht oben links „Upload Pitchdeck“.

## Footer

Box in Petrol, Radius 16 px, Innenabstand 30 px, `margin-bottom: 30px`, Breite wie der Container (1366 px).
Bis 1200 px: `margin: 0 20px`, `padding-bottom: 20px`.
Links: Investor Login · Investoren Informationen (EN: Investor information) · Datenschutz (Privacy Policy) · Impressum (Imprint),
Abstand 29 px, türkis. Rechts: X, Instagram, LinkedIn, TikTok (`Icons/*_blue.svg`, Eigengröße 40 bzw. 37 px, Abstand 7 px).
Mobil liegt alles zentriert untereinander, mit 37 px Abstand zu den Icons.

## Mobil (≤ 786 px)

neoteq.de würfelt beim Laden zwischen zwei Farbthemen (`app.js`, `Math.random()`):
**Petrol/Türkis** (`hover-color-one`: Hintergrund `#0f3737`, Text/Logo `#2aced1`) oder **Braun/Orange** (`hover-color-two`: `#46140a` / `#ff5722`).
Die Newsletter-Seiten nutzen fest Petrol/Türkis. Weiße Footer-Box gibt es mobil nicht, sie verschmilzt mit dem Hintergrund.

## Was wir bewusst anders machen

| Punkt | neoteq.de | Newsletter-Seiten | Grund |
|---|---|---|---|
| Logo-Datei | von neoteq.de | **dieselbe Datei**, byte-gleich kopiert nach `assets/logo.svg` (SHA-256 `1505c7a7…1426`) | neoteq.de liefert das Logo ohne CORS-Header. Als CSS-Maske (zum Einfärben) muss es deshalb von der eigenen Domain kommen. |
| Schrift, Icons, Pfeil, Favicon | lokal | direkt von www.neoteq.de geladen | dieselben Dateien, CORS erlaubt |
| CSS | `app.css` von neoteq.de | eigenes `style.css` mit den übernommenen Regeln | unabhängig von Umbauten an neoteq.de; nur die nötigen Regeln |
| Newsletter-Feld im Footer | iFrame von `forms.cloudworx.agency` | entfällt | Drittanbieter; auf der Newsletter-Seite selbst unnötig |
| Cookie-Banner | `cloud.ccm19.de` | entfällt | keine Cookies, nichts einzuwilligen |
| Mobiles Farbthema | zufällig | fest Petrol/Türkis | einheitlich mit den Mails |
| Hover-Farbe Desktop | zufällig Türkis/Orange | fest Türkis | wie oben |
| Seitenübergänge (barba.js), Video-Header | vorhanden | entfällt | nicht gebraucht |
| X-Link | `twitter.com/i/flow/login?redirect…` | `x.com/neoteqvc` | gleiches Profil, direkter Link |

## Vergleich

Screenshots nebeneinander (links neoteq.de/de/impressum, rechts `/bestaetigen/`) in `docs/vergleich/`.
Pixelvergleich der Header-Streifen: 0 abweichende Pixel bei 1440, 1100 und 390 px.
Die Elementpositionen im geöffneten Menü und im Footer stimmen auf den Pixel.
