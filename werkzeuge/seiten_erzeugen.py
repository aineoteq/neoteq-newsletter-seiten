"""Erzeugt die HTML-Seiten aus einer Vorlage und den Texten unten.

Texte hier ändern, dann `python3 werkzeuge/seiten_erzeugen.py` ausführen
und die erzeugten index.html-Dateien mit einchecken.
"""

from html import escape
from pathlib import Path

WURZEL = Path(__file__).resolve().parent.parent

GEMEINSAM = {
    "de": {
        "lang": "de",
        "impressum": ("Impressum", "https://neoteq.de/de/impressum"),
        "datenschutz": ("Datenschutz", "https://neoteq.de/de/datenschutz"),
        "start": "https://neoteq.de/de/",
        "andere_sprache": "English",
        "andere_lang": "en",
        "noscript": "Für diese Seite brauchst du JavaScript. Bitte aktiviere es und lade die Seite neu.",
        "logo_alt": "neoteq – zur Startseite",
        "nochmal": "Noch einmal versuchen",
        "zur_website": "Zu neoteq.de",
        "ungueltig_titel": "Dieser Link ist unvollständig",
        "ungueltig_text": "Öffne den Link bitte direkt aus der E-Mail. Falls das nicht hilft, kopiere die komplette Adresse in deinen Browser.",
        "fehler_titel": "Das hat nicht geklappt",
        "fehler_text": "Bitte versuche es in ein paar Minuten noch einmal.",
    },
    "en": {
        "lang": "en",
        "impressum": ("Imprint", "https://neoteq.de/en/imprint"),
        "datenschutz": ("Privacy policy", "https://neoteq.de/en/privacy-policy"),
        "start": "https://neoteq.de/en/",
        "andere_sprache": "Deutsch",
        "andere_lang": "de",
        "noscript": "This page needs JavaScript. Please enable it and reload the page.",
        "logo_alt": "neoteq – home",
        "nochmal": "Try again",
        "zur_website": "Go to neoteq.de",
        "ungueltig_titel": "This link is incomplete",
        "ungueltig_text": "Please open the link directly from the email. If that doesn’t help, copy the full address into your browser.",
        "fehler_titel": "Something went wrong",
        "fehler_text": "Please try again in a few minutes.",
    },
}

SEITEN = {
    "bestaetigen": {
        "de": {
            "pfad": "bestaetigen",
            "titel": "Anmeldung bestätigen",
            "dachzeile": "Newsletter",
            "h1": "Bitte bestätige deine Anmeldung",
            "text": [
                "Ein Klick noch, dann bekommst du den neoteq-Newsletter.",
            ],
            "leise": "Du hast dich nicht angemeldet? Dann schließ diese Seite einfach. Ohne Bestätigung schicken wir dir nichts.",
            "button": "Anmeldung bestätigen",
            "laeuft": "Einen Moment …",
            "erfolg_titel": "Danke, du bist dabei",
            "erfolg_text": "Deine Anmeldung ist bestätigt. Abmelden kannst du dich jederzeit über den Link am Ende jeder Ausgabe.",
            "abgelaufen_titel": "Dieser Link ist abgelaufen",
            "abgelaufen_text": "Melde dich bitte noch einmal an. Du bekommst dann eine neue Mail mit einem frischen Bestätigungslink.",
        },
        "en": {
            "pfad": "bestaetigen",
            "titel": "Confirm subscription",
            "dachzeile": "Newsletter",
            "h1": "Please confirm your subscription",
            "text": [
                "One more click and you’ll receive the neoteq newsletter.",
            ],
            "leise": "Didn’t sign up? Just close this page. We won’t send you anything without your confirmation.",
            "button": "Confirm subscription",
            "laeuft": "One moment …",
            "erfolg_titel": "Thanks, you’re in",
            "erfolg_text": "Your subscription is confirmed. You can unsubscribe at any time using the link at the end of every issue.",
            "abgelaufen_titel": "This link has expired",
            "abgelaufen_text": "Please sign up again. You’ll then receive a new email with a fresh confirmation link.",
        },
    },
    "abmelden": {
        "de": {
            "pfad": "abmelden",
            "titel": "Newsletter abmelden",
            "dachzeile": "Newsletter",
            "h1": "Newsletter abmelden",
            "text": [
                "Schade, dass du gehst. Nach dem Klick bekommst du keinen neoteq-Newsletter mehr.",
            ],
            "leise": None,
            "button": "Abmelden",
            "laeuft": "Einen Moment …",
            "erfolg_titel": "Du bist abgemeldet",
            "erfolg_text": "Wir schicken dir keinen Newsletter mehr. War das ein Versehen? Du kannst dich jederzeit wieder anmelden.",
            "abgelaufen_titel": "Dieser Link gilt nicht mehr",
            "abgelaufen_text": "Nutze bitte den Abmeldelink aus der neuesten Newsletter-Ausgabe.",
        },
        "en": {
            "pfad": "abmelden",
            "titel": "Unsubscribe",
            "dachzeile": "Newsletter",
            "h1": "Unsubscribe from the newsletter",
            "text": [
                "Sorry to see you go. After this click you won’t receive the neoteq newsletter anymore.",
            ],
            "leise": None,
            "button": "Unsubscribe",
            "laeuft": "One moment …",
            "erfolg_titel": "You’re unsubscribed",
            "erfolg_text": "We won’t send you the newsletter anymore. Changed your mind? You can sign up again at any time.",
            "abgelaufen_titel": "This link is no longer valid",
            "abgelaufen_text": "Please use the unsubscribe link from the latest newsletter issue.",
        },
    },
}

VORLAGE = """<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="Content-Security-Policy" content="default-src 'none'; script-src 'self'; style-src 'self'; font-src 'self'; img-src 'self'; connect-src 'self'; base-uri 'none'; form-action 'none'">
<meta name="referrer" content="no-referrer">
<meta name="robots" content="noindex, nofollow">
<title>{titel} · neoteq</title>
<link rel="icon" href="{assets}/favicon.svg" type="image/svg+xml">
<link rel="preload" href="{assets}/fonts/Poppins-Black.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{assets}/style.css">
<script src="{assets}/app.js" defer></script>
</head>
<body>
<header class="kopf">
  <div class="kopf-innen">
    <a class="logo" href="{start}"><img src="{assets}/logo-weiss.svg" alt="{logo_alt}" width="131" height="61"></a>
    <a class="sprache" href="{andere_href}" hreflang="{andere_lang}" lang="{andere_lang}" data-sprache>{andere_sprache}</a>
  </div>
</header>
<main data-aktion="{aktion}">
  <div class="karte">
    <section data-zustand="start" tabindex="-1">
      <p class="dachzeile">{dachzeile}</p>
      <h1>{h1}</h1>
{text}
      <button type="button" class="btn" data-ausloesen data-laeuft="{laeuft}">{button}</button>
      <noscript><p class="hinweis-fehler">{noscript}</p></noscript>
{leise}
    </section>
    <section class="zustand" data-zustand="erfolg" tabindex="-1" role="status" hidden>
      <p class="dachzeile">{dachzeile}</p>
      <h1>{erfolg_titel}</h1>
      <p>{erfolg_text}</p>
      <a class="btn btn-zweit" href="{start}">{zur_website}</a>
    </section>
    <section class="zustand" data-zustand="abgelaufen" tabindex="-1" role="alert" hidden>
      <p class="dachzeile">{dachzeile}</p>
      <h1>{abgelaufen_titel}</h1>
      <p>{abgelaufen_text}</p>
      <a class="btn btn-zweit" href="{start}">{zur_website}</a>
    </section>
    <section class="zustand" data-zustand="ungueltig" tabindex="-1" role="alert" hidden>
      <p class="dachzeile">{dachzeile}</p>
      <h1>{ungueltig_titel}</h1>
      <p>{ungueltig_text}</p>
    </section>
    <section class="zustand" data-zustand="fehler" tabindex="-1" role="alert" hidden>
      <p class="dachzeile">{dachzeile}</p>
      <h1>{fehler_titel}</h1>
      <p>{fehler_text}</p>
      <button type="button" class="btn" data-nochmal>{nochmal}</button>
    </section>
  </div>
</main>
<footer class="fuss">
  <div class="fuss-innen">
    <span>© neoteq ventures management GmbH</span>
    <nav>
      <a href="{impressum_href}">{impressum}</a>
      <a href="{datenschutz_href}">{datenschutz}</a>
    </nav>
  </div>
</footer>
</body>
</html>
"""


def erzeuge(aktion: str, sprache: str) -> None:
    g = GEMEINSAM[sprache]
    s = SEITEN[aktion][sprache]
    tiefe = 1 if sprache == "de" else 2
    ordner = WURZEL / s["pfad"] if sprache == "de" else WURZEL / "en" / s["pfad"]
    andere = SEITEN[aktion][g["andere_lang"]]["pfad"]
    andere_href = ("../" + andere + "/") if sprache == "en" else ("../en/" + andere + "/")

    werte = {k: escape(v) for k, v in {**g, **s}.items() if isinstance(v, str)}
    werte.update(
        aktion=aktion,
        assets="/".join([".."] * tiefe) + "/assets",
        andere_href=andere_href,
        impressum=escape(g["impressum"][0]),
        impressum_href=g["impressum"][1],
        datenschutz=escape(g["datenschutz"][0]),
        datenschutz_href=g["datenschutz"][1],
        text="\n".join(f"      <p>{escape(t)}</p>" for t in s["text"]),
        leise=f'      <p class="leise">{escape(s["leise"])}</p>' if s["leise"] else "",
    )
    ordner.mkdir(parents=True, exist_ok=True)
    (ordner / "index.html").write_text(VORLAGE.format(**werte), encoding="utf-8")
    print("geschrieben:", (ordner / "index.html").relative_to(WURZEL))


if __name__ == "__main__":
    for aktion in SEITEN:
        for sprache in ("de", "en"):
            erzeuge(aktion, sprache)
