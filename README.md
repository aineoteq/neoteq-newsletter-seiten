# neoteq Newsletter-Seiten

Zwei kleine Seiten für den neoteq-Newsletter, auf Deutsch und Englisch:

| Seite | Deutsch | Englisch |
|---|---|---|
| Anmeldung bestätigen (Double-Opt-in) | `/bestaetigen/?token=…` | `/en/bestaetigen/?token=…` |
| Abmelden | `/abmelden/?token=…` | `/en/abmelden/?token=…` |

Der Link aus der Mail öffnet nur die Seite. **Erst der Klick auf den Button löst die Aktion aus.**
So bestätigen Mail-Scanner, die Links vorab aufrufen, keine Anmeldung und melden niemanden ab.

Zustände: Start, Erfolg, Fehler (mit „Noch einmal versuchen"), Link abgelaufen, Link unvollständig (kein Token).

## Stand: Phase 1 – Demo

`assets/app.js` steht auf `modus: "demo"`. Der Klick ruft nichts auf und zeigt nach kurzer Pause den Erfolgszustand.
Zum Ansehen der anderen Zustände im Demo-Modus `&zustand=fehler`, `&zustand=abgelaufen` oder `&zustand=ungueltig` anhängen
(wirkt erst beim Klick). Ohne `token` erscheint direkt „Link unvollständig".

Veröffentlicht über GitHub Pages aus `main`, Wurzelverzeichnis.

## Datenschutz

- Keine Cookies, kein localStorage, kein Tracking, kein Cookie-Banner, keine Drittanbieter.
- Schrift, Icons und Favicon kommen direkt von www.neoteq.de (setzt dort keine Cookies). Das Logo liegt byte-gleich im Repo, siehe DESIGN.md.
- Content-Security-Policy erlaubt nur die eigene Adresse und www.neoteq.de (Schrift, Bilder).
- `referrer: no-referrer`, damit der Token beim Klick auf Impressum oder Datenschutz nicht an neoteq.de weitergegeben wird.
- `noindex`, die Seiten sollen nicht in Suchmaschinen landen.
- Hinweis: GitHub Pages (Phase 1) bzw. Cloudflare (Phase 2) protokollieren als Hoster IP-Adressen. Für den Livebetrieb gehört der Hoster in die Datenschutzerklärung.

## Design

Header, Menü, Footer, Typo und Abstände sind von neoteq.de übernommen. Werte, Quellen und Abweichungen: [DESIGN.md](DESIGN.md),
Screenshots nebeneinander: [docs/vergleich/](docs/vergleich/).

## Texte ändern

Texte stehen in `werkzeuge/seiten_erzeugen.py`. Danach:

```sh
python3 werkzeuge/seiten_erzeugen.py
```

und die erzeugten `index.html`-Dateien mit einchecken.

## Secrets

Im Repo liegt kein Secret und es darf auch keins hinein. Das Webhook-Secret kommt in Phase 2 ausschließlich
als verschlüsselte Umgebungsvariable in Cloudflare – siehe [docs/phase-2-cloudflare.md](docs/phase-2-cloudflare.md).
