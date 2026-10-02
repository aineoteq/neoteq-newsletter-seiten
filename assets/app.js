// neoteq Newsletter-Seiten: Bestätigen und Abmelden.
// Der Link aus der Mail öffnet nur die Seite. Erst der Klick auf den Button
// löst die Aktion aus, damit Mail-Scanner, die Links aufrufen, nichts bestätigen.

(function () {
  "use strict";

  var KONFIG = {
    // "demo": kein Aufruf, der Klick zeigt nach kurzer Pause den Erfolgszustand.
    // "live": POST an den eigenen Endpunkt (Phase 2, Cloudflare Pages Function).
    modus: "demo",
    endpunkte: {
      bestaetigen: "/api/bestaetigen",
      abmelden: "/api/abmelden"
    }
  };

  // Menü wie auf neoteq.de: Knopf öffnet und schließt das Overlay, Escape schließt.
  var menueKnopf = document.querySelector(".nav_trigger");
  if (menueKnopf) {
    var setzeMenue = function (offen) {
      document.body.classList.toggle("nav_active", offen);
      menueKnopf.setAttribute("aria-expanded", offen ? "true" : "false");
    };
    menueKnopf.addEventListener("click", function () {
      setzeMenue(!document.body.classList.contains("nav_active"));
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && document.body.classList.contains("nav_active")) {
        setzeMenue(false);
        menueKnopf.focus();
      }
    });
  }

  var main = document.querySelector("main[data-aktion]");
  if (!main) return;

  var aktion = main.getAttribute("data-aktion");
  var params = new URLSearchParams(window.location.search);
  var token = (params.get("token") || "").trim();
  var button = main.querySelector("[data-ausloesen]");
  var buttonText = button ? button.textContent : "";

  function zeige(name) {
    var ziel = null;
    main.querySelectorAll("[data-zustand]").forEach(function (el) {
      var passt = el.getAttribute("data-zustand") === name;
      el.hidden = !passt;
      if (passt) ziel = el;
    });
    // Screenreader und Tastatur landen beim neuen Zustand.
    if (ziel && name !== "start") ziel.focus();
  }

  // Sprachumschalter behält den Token.
  var sprache = document.querySelector("[data-sprache]");
  if (sprache && window.location.search) {
    sprache.setAttribute("href", sprache.getAttribute("href") + window.location.search);
  }

  if (!token) {
    zeige("ungueltig");
    return;
  }

  // Nur im Demo-Modus: ?zustand=fehler|abgelaufen|ungueltig zum Ansehen der anderen Zustände.
  var vorschau = KONFIG.modus === "demo" ? params.get("zustand") : null;

  function ausfuehren() {
    if (KONFIG.modus === "demo") {
      return new Promise(function (fertig) {
        setTimeout(function () {
          fertig(vorschau || "erfolg");
        }, 600);
      });
    }
    return fetch(KONFIG.endpunkte[aktion], {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ token: token }),
      credentials: "omit",
      cache: "no-store"
    }).then(function (antwort) {
      if (antwort.ok) return "erfolg";
      if (antwort.status === 410) return "abgelaufen";
      if (antwort.status === 400 || antwort.status === 404) return "ungueltig";
      return "fehler";
    }, function () {
      return "fehler";
    });
  }

  function klick() {
    button.disabled = true;
    button.textContent = button.getAttribute("data-laeuft") || buttonText;
    ausfuehren().then(function (ergebnis) {
      button.disabled = false;
      button.textContent = buttonText;
      zeige(ergebnis);
    });
  }

  if (button) button.addEventListener("click", klick);

  main.querySelectorAll("[data-nochmal]").forEach(function (el) {
    el.addEventListener("click", function () {
      vorschau = null;
      zeige("start");
      button.focus();
    });
  });

  zeige("start");
})();
