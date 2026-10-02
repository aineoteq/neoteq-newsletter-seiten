# Phase 2: Cloudflare Pages mit Function (Skizze, noch nicht gebaut)

## Ablauf

```
Mail-Link  ──GET──▶  newsletter.neoteq.de/bestaetigen/?token=…   (statische Seite, tut nichts)
Klick      ──POST──▶ newsletter.neoteq.de/api/bestaetigen  {token}
                       │  Cloudflare Pages Function
                       │  + Header X-Webhook-Secret: <aus Cloudflare-Secret>
                       ▼
                     Langdock-Webhook „Bestätigung“  (bzw. „Abmeldung“)
```

- Der Browser sieht weder das Secret noch die Langdock-Webhook-URL. Er spricht nur mit `/api/…` auf derselben Domain.
- Nur `POST` löst etwas aus. Ein Scanner, der den Mail-Link per `GET` öffnet, bekommt nur die statische Seite.
- In `assets/app.js` wird `modus` von `"demo"` auf `"live"` gestellt. Der Client-Teil dafür ist schon drin, aber noch ungetestet.

## Function (Skizze)

Datei später: `functions/api/[aktion].js`. Sie liegt bewusst noch nicht im Repo, sonst würde Cloudflare sie mit ausrollen.

```js
// Umgebungsvariablen (in Cloudflare als „Secret“ angelegt, nie im Repo):
//   WEBHOOK_SECRET, LANGDOCK_URL_BESTAETIGEN, LANGDOCK_URL_ABMELDEN
export async function onRequestPost({ request, env, params }) {
  const ziel = {
    bestaetigen: env.LANGDOCK_URL_BESTAETIGEN,
    abmelden: env.LANGDOCK_URL_ABMELDEN,
  }[params.aktion];
  if (!ziel) return new Response(null, { status: 404 });

  // Nur Aufrufe von der eigenen Seite annehmen.
  const origin = request.headers.get("Origin");
  if (origin !== new URL(request.url).origin) return new Response(null, { status: 403 });

  let token;
  try { ({ token } = await request.json()); } catch { return new Response(null, { status: 400 }); }
  if (typeof token !== "string" || !/^[A-Za-z0-9_-]{16,256}$/.test(token)) {
    return new Response(null, { status: 400 });
  }

  const antwort = await fetch(ziel, {
    method: "POST",
    headers: { "Content-Type": "application/json", "X-Webhook-Secret": env.WEBHOOK_SECRET },
    body: JSON.stringify({ token }),
  });

  // Statuscodes, die die Seite versteht: 200 Erfolg, 410 abgelaufen, 400/404 ungültig, sonst Fehler.
  const status = [200, 400, 404, 410].includes(antwort.status) ? antwort.status : 502;
  return new Response(null, { status, headers: { "Cache-Control": "no-store" } });
}
```

## Offene Frage an den Langdock-Workflow

Damit „Link abgelaufen“ und „ungültig“ angezeigt werden können, muss der Webhook **synchron** ein Ergebnis zurückgeben
(z. B. HTTP 410 für abgelaufen). Antwortet Langdock nur mit „angenommen“ und arbeitet im Hintergrund weiter, kann die Seite
nur „Erfolg“ oder „Fehler“ zeigen. Vor dem Bau prüfen. Falls nicht synchron, liegt die Alternative darin, Ablaufdatum
und Signatur im Token selbst zu codieren und in der Function zu prüfen. Dafür bräuchte die Function einen eigenen Signaturschlüssel.

Außerdem den Format-Check oben (`16–256` Zeichen, `A–Z a–z 0–9 _ -`) an das echte Token-Format anpassen.

## Was du anlegen musst

1. **Cloudflare-Konto** (kostenloser Plan reicht), mit einer Firmen-Mailadresse statt einer persönlichen und mit 2FA.
2. **Workers & Pages → Pages → Mit Git verbinden** → GitHub-Organisation `aineoteq` autorisieren, Repo `neoteq-newsletter-seiten`.
   Build-Befehl: leer, Ausgabeverzeichnis: `/`. Ergebnis: `neoteq-newsletter-seiten.pages.dev`.
3. **Umgebungsvariablen** (Settings → Variables and Secrets, Typ *Secret*, für Production):
   `WEBHOOK_SECRET`, `LANGDOCK_URL_BESTAETIGEN`, `LANGDOCK_URL_ABMELDEN`.
4. **Eigene Domain:** Im Pages-Projekt unter *Custom domains* `newsletter.neoteq.de` hinzufügen.
   Danach beim DNS-Anbieter von neoteq.de einen Eintrag anlegen:
   `newsletter  CNAME  neoteq-newsletter-seiten.pages.dev`
   Die Nameserver von neoteq.de müssen dafür **nicht** zu Cloudflare umziehen, ein CNAME für die Subdomain reicht.
   Das TLS-Zertifikat stellt Cloudflare automatisch aus.
5. **Datenschutzerklärung** auf neoteq.de um Cloudflare als Hoster bzw. Auftragsverarbeiter ergänzen
   (Cloudflare-DPA wird im Dashboard akzeptiert).
6. **Links in den Mails** auf `https://newsletter.neoteq.de/bestaetigen/?token=…` bzw. `/abmelden/?token=…` umstellen
   (englisch: `/en/…`).
7. Danach GitHub Pages für dieses Repo abschalten, damit nur noch eine Adresse existiert.
