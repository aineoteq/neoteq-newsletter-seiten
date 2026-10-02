"""Erzeugt die HTML-Seiten aus einer Vorlage und den Texten unten.

Texte hier ändern, dann `python3 werkzeuge/seiten_erzeugen.py` ausführen
und die erzeugten index.html-Dateien mit einchecken.
Header, Menü und Footer entsprechen neoteq.de (siehe DESIGN.md).
"""

from html import escape
from pathlib import Path

WURZEL = Path(__file__).resolve().parent.parent
NTQ = "https://www.neoteq.de"
NTQ_ASSETS = NTQ + "/typo3conf/ext/base/Resources/Public"

SOCIAL = [
    ("X", "https://x.com/neoteqvc", "x"),
    ("Instagram", "https://www.instagram.com/neoteqvc/", "instagram"),
    ("LinkedIn", "https://www.linkedin.com/company/neoteq-ventures/", "linkedIn"),
    ("TikTok", "https://www.tiktok.com/@neoteqvc", "tiktok"),
]

GEMEINSAM = {
    "de": {
        "lang": "de",
        "start": NTQ + "/de/",
        "pitchdeck": ("Pitchdeck hochladen", NTQ + "/de/pitchdeck"),
        "pitchdeck_mobil": "Upload Pitchdeck",
        "hauptnavigation": [
            ("Mission", NTQ + "/de/mission"),
            ("Portfolio", NTQ + "/de/portfolio"),
            ("Team", NTQ + "/de/team"),
            ("NEOJOBS", "https://neoteq.notion.site/neojobs-9f00a0fec73f4dd89166f2f126d01c3a?pvs=4"),
        ],
        "fussnavigation": [
            ("Investor Login", "https://auth.fundrbird.com/7dd2e6fe-0953-4e62-9725-ea4834524c69"),
            ("Investoren Informationen", NTQ + "/de/investoren-informationen"),
            ("Datenschutz", NTQ + "/de/datenschutz"),
            ("Impressum", NTQ + "/de/impressum"),
        ],
        "projekte": [NTQ + "/de/neobib", NTQ + "/de/founders-dinner"],
        "andere_sprache": "EN",
        "andere_lang": "en",
        "menue": "Menü",
        "noscript": "Für diese Seite brauchst du JavaScript. Bitte aktiviere es und lade die Seite neu.",
        "logo_alt": "neoteq ventures – zur Startseite",
        "nochmal": "Noch einmal versuchen",
        "zur_website": "Zu neoteq.de",
        "ungueltig_titel": "Dieser Link ist unvollständig",
        "ungueltig_text": "Öffne den Link bitte direkt aus der E-Mail. Falls das nicht hilft, kopiere die komplette Adresse in deinen Browser.",
        "fehler_titel": "Das hat nicht geklappt",
        "fehler_text": "Bitte versuche es in ein paar Minuten noch einmal.",
    },
    "en": {
        "lang": "en",
        "start": NTQ + "/en/",
        "pitchdeck": ("Upload your Pitchdeck", NTQ + "/en/pitchdeck"),
        "pitchdeck_mobil": "Upload Pitchdeck",
        "hauptnavigation": [
            ("Mission", NTQ + "/en/mission"),
            ("Portfolio", NTQ + "/en/portfolio"),
            ("Team", NTQ + "/en/team"),
            ("NEOJOBS", "https://neoteq.notion.site/neojobs-9f00a0fec73f4dd89166f2f126d01c3a?pvs=4"),
        ],
        "fussnavigation": [
            ("Investor Login", "https://auth.fundrbird.com/7dd2e6fe-0953-4e62-9725-ea4834524c69"),
            ("Investor information", NTQ + "/en/investor-information"),
            ("Privacy Policy", NTQ + "/en/privacy-policy"),
            ("Imprint", NTQ + "/en/imprint"),
        ],
        "projekte": [NTQ + "/en/neobib", NTQ + "/en/founders-dinner"],
        "andere_sprache": "DE",
        "andere_lang": "de",
        "menue": "Menu",
        "noscript": "This page needs JavaScript. Please enable it and reload the page.",
        "logo_alt": "neoteq ventures – home",
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
            "titel": "Anmeldung bestätigen",
            "dachzeile": "Newsletter",
            "h1": "Bitte bestätige deine Anmeldung",
            "text": "Ein Klick noch, dann bekommst du den neoteq-Newsletter.",
            "leise": "Du hast dich nicht angemeldet? Dann schließ diese Seite einfach. Ohne Bestätigung schicken wir dir nichts.",
            "button": "Anmeldung bestätigen",
            "laeuft": "Einen Moment …",
            "erfolg_titel": "Danke, du bist dabei",
            "erfolg_text": "Deine Anmeldung ist bestätigt. Abmelden kannst du dich jederzeit über den Link am Ende jeder Ausgabe.",
            "abgelaufen_titel": "Dieser Link ist abgelaufen",
            "abgelaufen_text": "Melde dich bitte noch einmal an. Du bekommst dann eine neue Mail mit einem frischen Bestätigungslink.",
        },
        "en": {
            "titel": "Confirm subscription",
            "dachzeile": "Newsletter",
            "h1": "Please confirm your subscription",
            "text": "One more click and you’ll receive the neoteq newsletter.",
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
            "titel": "Abmeldung bestätigen",
            "dachzeile": "Newsletter",
            "h1": "Bitte bestätige deine Abmeldung",
            "text": "Ein Klick noch, dann kommt kein neoteq-Newsletter mehr.",
            "leise": "Doch nicht abmelden? Dann schließ diese Seite einfach. Ohne Bestätigung bleibt alles, wie es ist.",
            "button": "Abmeldung bestätigen",
            "laeuft": "Einen Moment …",
            "erfolg_titel": "Du bist abgemeldet",
            "erfolg_text": "Wir schicken dir keinen Newsletter mehr. War das ein Versehen? Du kannst dich jederzeit wieder anmelden.",
            "abgelaufen_titel": "Dieser Link gilt nicht mehr",
            "abgelaufen_text": "Nutze bitte den Abmeldelink aus der neuesten Newsletter-Ausgabe.",
        },
        "en": {
            "titel": "Confirm unsubscribe",
            "dachzeile": "Newsletter",
            "h1": "Please confirm your unsubscribe",
            "text": "One more click and the neoteq newsletter stops.",
            "leise": "Changed your mind? Just close this page. Without your confirmation, nothing changes.",
            "button": "Confirm unsubscribe",
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
<meta http-equiv="Content-Security-Policy" content="default-src 'none'; script-src 'self'; style-src 'self'; font-src https://www.neoteq.de; img-src 'self' https://www.neoteq.de; connect-src 'self'; base-uri 'none'; form-action 'none'">
<meta name="referrer" content="no-referrer">
<meta name="robots" content="noindex, nofollow">
<title>{titel}: Neoteq</title>
<link rel="icon" href="{ntq_assets}/Icons/favicon.svg" type="image/svg+xml">
<link rel="preload" href="{ntq_assets}/Fonts/NTQ-Poppins-Black.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{ntq_assets}/Fonts/NTQ-Poppins-Medium.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{assets}/style.css">
<script src="{assets}/app.js" defer></script>
</head>
<body>
<header>
  <div class="container">
    <a id="logo" href="{start}">
      <div class="logo_mask"><img src="{assets}/logo.svg" alt="{logo_alt}" width="130" height="61"></div>
    </a>
    <div class="kopf-rechts">
      <a class="btn upload" href="{pitchdeck_href}">{pitchdeck}</a>
      <div id="language_menu"><a class="btn" href="{andere_href}" hreflang="{andere_lang}" lang="{andere_lang}" data-sprache>{andere_sprache}</a></div>
      <nav aria-label="{menue}">
        <button type="button" class="nav_trigger" aria-expanded="false" aria-controls="menue" aria-label="{menue}"><span></span><span></span></button>
        <div class="nav_content" id="menue">
          <div class="container">
            <a class="btn nur-mobil" href="{pitchdeck_href}">{pitchdeck_mobil}</a>
            <ul class="main_nav">
{hauptnavigation}
            </ul>
            <div class="nav_content_inner">
              <div class="headerVideo_logos">
                <div class="flex">
                  <a href="https://calendly.com/c/FFCQWVOYDTTXZ4CQ?month=2023-10"><img src="{ntq_assets}/Images/FF_dark.svg" alt="Friday's Fifteen"></a>
                  <a href="{neobib}"><img src="{ntq_assets}/Images/neobib_logo_dark.svg" alt="neobib"></a>
                  <a href="{foundersdinner}"><img class="h-14" src="{ntq_assets}/Images/foundersdinner_dark.svg" alt="founders dinner"></a>
                </div>
              </div>
              <div class="nav_content_bottom">
                <div class="nav_content_navigation">
                  <ul>
{fussnavigation}
                  </ul>
                </div>
                <div class="nav_socialMediaIcons">
{social_dunkel}
                </div>
              </div>
            </div>
          </div>
        </div>
      </nav>
    </div>
  </div>
</header>
<main data-aktion="{aktion}">
  <div class="container">
    <div class="col-span-12">
      <div class="inhalt">
        <section data-zustand="start" tabindex="-1">
          <span class="dachzeile">{dachzeile}</span>
          <h1>{h1}</h1>
          <p>{text}</p>
          <button type="button" class="btn arrow" data-ausloesen data-laeuft="{laeuft}">{button}</button>
          <noscript><p class="leise">{noscript}</p></noscript>
{leise}
        </section>
        <section class="zustand" data-zustand="erfolg" tabindex="-1" role="status" hidden>
          <span class="dachzeile">{dachzeile}</span>
          <h1>{erfolg_titel}</h1>
          <p>{erfolg_text}</p>
          <a class="btn arrow" href="{start}">{zur_website}</a>
        </section>
        <section class="zustand" data-zustand="abgelaufen" tabindex="-1" role="alert" hidden>
          <span class="dachzeile">{dachzeile}</span>
          <h1>{abgelaufen_titel}</h1>
          <p>{abgelaufen_text}</p>
          <a class="btn arrow" href="{start}">{zur_website}</a>
        </section>
        <section class="zustand" data-zustand="ungueltig" tabindex="-1" role="alert" hidden>
          <span class="dachzeile">{dachzeile}</span>
          <h1>{ungueltig_titel}</h1>
          <p>{ungueltig_text}</p>
        </section>
        <section class="zustand" data-zustand="fehler" tabindex="-1" role="alert" hidden>
          <span class="dachzeile">{dachzeile}</span>
          <h1>{fehler_titel}</h1>
          <p>{fehler_text}</p>
          <button type="button" class="btn arrow" data-nochmal>{nochmal}</button>
        </section>
      </div>
    </div>
  </div>
</main>
<footer>
  <div class="container">
    <div class="col-span-12">
      <div class="footer_navigation">
        <ul>
{fussnavigation}
        </ul>
      </div>
      <div class="footer_socialmedia">
{social_blau}
      </div>
    </div>
  </div>
</footer>
</body>
</html>
"""


def liste(eintraege, klasse="", einrueckung=12):
    attr = f' class="{klasse}"' if klasse else ""
    return "\n".join(
        " " * einrueckung + f'<li><a href="{escape(url)}"{attr}>{escape(text)}</a></li>'
        for text, url in eintraege
    )


def social(variante, einrueckung):
    return "\n".join(
        " " * einrueckung
        + f'<a href="{url}"><img src="{NTQ_ASSETS}/Icons/{datei}_{variante}.svg" alt="{name}"></a>'
        for name, url, datei in SOCIAL
    )


def erzeuge(aktion: str, sprache: str) -> None:
    g = GEMEINSAM[sprache]
    s = SEITEN[aktion][sprache]
    ordner = WURZEL / aktion if sprache == "de" else WURZEL / "en" / aktion
    andere_href = ("../../" if sprache == "en" else "../en/") + aktion + "/"

    werte = {k: escape(v) for k, v in {**g, **s}.items() if isinstance(v, str)}
    werte.update(
        aktion=aktion,
        assets=("../" if sprache == "de" else "../../") + "assets",
        ntq_assets=NTQ_ASSETS,
        andere_href=andere_href,
        pitchdeck=escape(g["pitchdeck"][0]),
        pitchdeck_href=g["pitchdeck"][1],
        neobib=g["projekte"][0],
        foundersdinner=g["projekte"][1],
        hauptnavigation=liste(g["hauptnavigation"], "text-nav", 14),
        fussnavigation=liste(g["fussnavigation"], einrueckung=10),
        social_dunkel=social("dark", 18),
        social_blau=social("blue", 8),
        leise=f'          <p class="leise">{escape(s["leise"])}</p>' if s["leise"] else "",
    )
    ordner.mkdir(parents=True, exist_ok=True)
    (ordner / "index.html").write_text(VORLAGE.format(**werte), encoding="utf-8")
    print("geschrieben:", (ordner / "index.html").relative_to(WURZEL))


if __name__ == "__main__":
    for aktion in SEITEN:
        for sprache in ("de", "en"):
            erzeuge(aktion, sprache)
