# Poly installieren — 2 Minuten, ganz ohne Technikwissen

Poly ist ein Kurzbefehl fürs iPhone: Du stellst eine Frage, und zwei KIs kümmern sich gleichzeitig darum — ChatGPT und Claude — in einem von elf Modi. Die Antwort landet auf deinem Bildschirm und in deiner Zwischenablage.

## Vor der Installation (einmalig)

1. **Ein iPhone mit iOS 18 oder neuer.** Das ist das offizielle Minimum für die Aktion „Ask Claude“, auf der Poly aufbaut (Anthropic schreibt in der eigenen Dokumentation „iOS 18 and later“). Davon unabhängig führt Apple unter iOS 26 iPhone 11 und neuer sowie SE der 2. Generation und neuer als unterstützte Geräte. Poly selbst braucht kein Apple Intelligence — nur iOS 18+. Auf dem iPad ist der Betrieb unter iPadOS 18+/26 zu erwarten, wurde aber nicht im Alltag erprobt. Der Begleiter **Poly Compress** braucht ausdrücklich Apple-Intelligence-Hardware: einen Chip der A17-Pro-/M-Reihe oder neuer (iPhone 15 Pro/Pro Max, alle 16/16e und neuer, iPad mit M1+ oder das mini mit A17 Pro).
2. **Die Apps ChatGPT und Claude**, aus dem App Store installiert und in beiden angemeldet. Kostenlose Konten reichen: Das kostenlose Claude nutzt Sonnet 5.5, dasselbe Modell wie das bezahlte Abo, und die Aktion „Ask Claude“ nutzt das in der Claude-App gewählte Modell.

## Installieren (ein Tipp)

1. Bring die Datei **`dist/de/Poly.shortcut`** auf beliebigem Weg auf dein iPhone: AirDrop, WhatsApp/Telegram, E-Mail, ein USB-Stick — egal wie.
2. Tippe auf die Datei. Shortcuts öffnet sich mit einer „Poly“-Karte — tippe auf **„Kurzbefehl hinzufügen“**. Fertig, Poly ist installiert.
   - Kam die Datei in einem Messenger an, tippe sie zuerst dort an, wähle „Teilen“/„Öffnen in…“ und dann Shortcuts.
3. **Erster Lauf:** Der Kurzbefehl fragt nach Berechtigungen — „ChatGPT-Aktionen erlauben?“ → Erlauben; „…Text an Claude senden?“ → **Immer erlauben**; „…in die Zwischenablage kopieren?“ → **Immer erlauben**. Das passiert nur ein einziges Mal.

## Symbol auf dem Home-Bildschirm (30 Sekunden, optional)

1. Öffne Shortcuts → lege den Finger länger auf die Poly-Kachel → erscheint kein Menü, tippe auf „···“ auf der Kachel → tippe oben auf den Namen **Poly ⌄** → **„Zum Home-Bildschirm hinzufügen“**.
2. Du willst das gestaltete Symbol? Tippe auf die Miniatur → Tab „Bild“ → „Foto/Datei auswählen“ → wähle `assets/poly.jpg` (schick sie zusammen mit dem Kurzbefehl aufs Handy).
3. Tippe auf **Hinzufügen**. Das Poly-Symbol erscheint auf deinem Home-Bildschirm — ein Tipp genügt zum Start. Per Stimme: „Hey Siri, Poly“.

## So benutzt du es

Symbol antippen → „Was möchtest du Poly fragen?“ → Frage eintippen → „Fertig“ → Modus wählen. Das Menü hat zwei Ebenen: oben fünf gängige Modi, alles Weitere steckt in **📂 Mehr…** (nichts ist entfernt — ein seltener Modus kostet nur einen zusätzlichen Tipp). In „Mehr…“ liegt auch **ℹ️ Was ist Poly** — eine kostenlose Erklärung aller Modi direkt auf dem Gerät. Ratlos bei der Modusauswahl? Öffne sie — sie verbraucht keine einzige Nachricht.

**Hauptmenü (gängige Modi):**

| Modus | Was passiert | Kosten |
|---|---|---|
| **⚖️ Kritik · 2✉** | ChatGPT antwortet, Claude prüft nach und liefert eine verbesserte Endfassung. Dein Alltagswerkzeug. | 2 Nachrichten |
| **🩺 Berater · 1✉** | Claude prüft DEINEN fertigen Text, ohne ihn umzuschreiben: ein Urteil in einer Zeile, der stärkste Einwand zuerst, was du gegenprüfen solltest. Der günstigste Modus. | 1 Nachricht |
| **👀 Nebeneinander · 2✉** | Beide antworten unabhängig; die Antworten stehen nebeneinander. | 2 Nachrichten |
| **🔀 Synthese · 3✉** | Beide antworten blind, dann wird daraus ein Ergebnis aus „Anker + Ergänzung“ gebaut. Du wirst gefragt, wer verankert: Claude (Fakten/Struktur) oder ChatGPT (Ton/Kreativität). Für alles, was zählt. | 3 Nachrichten |
| **🧭 Auto · +1✉** | Unsicher, welcher Modus passt? ChatGPT wählt einen für dich aus (+1 Nachricht), dann startet Poly mit derselben Frage neu, damit du den empfohlenen Modus nehmen kannst. | 1 Nachricht + der Modus |

**📂 Mehr… (seltenere Modi + kostenlose Hilfe):**

| Modus | Was passiert | Kosten |
|---|---|---|
| **⚔️ Entscheidung · 3✉** | Ein schneller Blick (ChatGPT) trifft auf einen vorsichtigen (Claude), dann legt ein Schiedsrichter erste Schritte und Risiken dar. Für Entscheidungen. | 3 Nachrichten |
| **🗺 Streitkarte · 3✉** | Beide antworten blind, danach wird kartiert: wo sie übereinstimmen, wo sie auseinandergehen, blinde Flecken, was zu prüfen ist. Kein erzwungenes Fazit — du entscheidest. | 3 Nachrichten |
| **🥊 Debatte · 4✉** | Ein Entwurf, ein Gegner auf der Suche nach Schwachstellen, eine Überarbeitung, dann das Urteil eines Richters. Für die härtesten Probleme. | 4 Nachrichten |
| **❓ Rückfrage · 2✉** | ChatGPT fragt erst, was fehlt → du antwortest in einem Fenster, das aufgeht → Claude gibt eine präzise Antwort. Für vage Fragen. Der einzige Modus, in dem du mitten im Lauf den Bildschirm berühren sollst — aber nur in seinem eigenen Dialog, sonst nirgends. | 2 Nachrichten |
| **➕ Delta · 2✉** | Claude schreibt die Ankerantwort → ChatGPT liefert NUR eine Stichpunktliste mit Verbesserungen, kein komplettes Umschreiben. Die günstigere Alternative zur Synthese, wenn du auf dein Nachrichtenbudget achtest. | 2 Nachrichten |
| **🎨 Bild · 2–3✉** | Beschreibe, was gezeichnet werden soll → beide KI-Künstler skizzieren es blind (Vektor-SVG, jeder in einer frischen Sitzung — kein Blick zum anderen) → es öffnet sich eine Seite mit zwei Skizzen nebeneinander, ◆ CLAUDE und ◆ CHATGPT — such dir eine aus (du wirst gefragt: nur Skizzen · 2✉ oder + das Urteil eines vergleichenden Richters · 3✉ — der Richter vergleicht den Skizzencode; die fertigen Bilder siehst du ohnehin selbst). Das Bild wird gesichert (Dateien → iCloud Drive → Shortcuts → `Poly-image.html`), und der SVG-Code landet in deiner Zwischenablage: Füge ihn in einen beliebigen Konverter oder eine Website ein, und du bekommst eine Bilddatei in jeder Größe. | 2–3 Nachrichten |
| **ℹ️ Was ist Poly** | Eine Erklärung auf dem Bildschirm: was Poly ist und wann welcher Modus passt — ganz ohne KI-Aufrufe. Von dort bringt dich „🔁 Anderer Modus“ mit derselben Frage zurück zur Modusauswahl. | 0 Nachrichten |

**Eine Abkürzung ins Menü selbst** (optional): Halte den Begleiter **Poly Quiet** griffbereit — ein fertiger Kritik-Lauf mit einem Tipp, ganz ohne Modusauswahl (das Ergebnis geht direkt in Zwischenablage und Journal, keine Bildschirme) — oder **Poly Voice**, dasselbe per Stimme, mit vorgelesenem Ergebnis. Beide Symbole kannst du genau wie Poly auf den Home-Bildschirm legen und hast so einen „Schnellknopf“ neben dem vollen Menü.

Die Kosten stehen direkt im Menü (das ✉-Zeichen). Fortschrittsmitteilungen kommen während des Laufs — „[Schritt 2/4]…“. Das Journal hält den Modus und die rohen Zwischenantworten fest: Wird das Endergebnis abgeschnitten, sind die Entwürfe trotzdem nicht verloren. Die finale Antwort öffnet sich bildschirmfüllend mit einer Teilen-Taste (Quick Look).

**Zwei Stufen.** Stufe 1 ist der Kern: das vollautomatische Poly-Duett samt der automatischen Begleiter unten — installiere es ohne Zögern, das ist die eigentliche Neuerung. Stufe 2 ist eine PRO-Erweiterung für Fortgeschrittene: **🎼 Poly Multi** (ein manueller Chor aus 10 KIs aus den USA und China mit einer Ost-West-Synthese) kommt separat und ist für das Kernerlebnis nicht nötig — hol es dir, wenn dir die Grundlagen vertraut sind.

**Automatische Poly-Begleiter** (enthalten): **Poly Voice** — antippen, diktieren, die Kritik-Kette läuft, die Antwort wird vorgelesen (gut beim Gehen oder Kochen); **Poly Photo** — teile ein Foto oder PDF, die Texterkennung auf dem Gerät liest den Text (kostenlos, ohne Netz) und gibt ihn direkt an Poly weiter; **Poly Quiet** — dieselbe Kette wie Kritik, aber ohne Mitteilungen und ohne Abschlussbildschirm: Das Ergebnis geht nur in Zwischenablage und Journal (für schnelle Läufe im Hintergrund); **Poly Compress** (nur Geräte mit Apple Intelligence: iPhone 15 Pro und neuer, die komplette Reihe 16/16e/17) — markiere eine Textwand → Teilen → Compress: Apples kostenloses Modell auf dem Gerät schrumpft ihn und startet Poly automatisch (Schutz gegen Timeouts bei langen Texten).

Direkt nach der Modusauswahl kommt eine **Statusmitteilung** („was gerade passiert und wie lange es dauert“). Danach vergehen etwa 1–2 Minuten, bis die Antwort auf dem Bildschirm und in der Zwischenablage steht. Fertige Formulierungen für über 20 gängige Aufgaben stehen in `recipes.md`. Die finale Antwort beginnt immer mit dem Kern in einer Zeile und endet mit „Confidence: high/medium/low“. **Während der Kurzbefehl läuft, lass das Handy in Ruhe** — eine Berührung des Bildschirms bricht ihn ab (wirkt es, als sei er stillschweigend gestorben, starte ihn einfach neu). Die Ausnahme ist **❓ Rückfrage**: Sie öffnet absichtlich ein zweites Fenster und bittet dich, Rückfragen zu beantworten (oder auf „überspringen“ zu tippen) — das ist kein Fehler, das gehört zum Ablauf. Antworte, und der Kurzbefehl läuft von allein weiter.

## Superkräfte

- **Aus jeder App heraus:** Text markieren → Teilen → Poly — dein Fragefeld enthält den Text bereits; ergänze „übersetzen/prüfen/erklären“ und starte.
- **Journal:** Jeder Lauf hängt sich an `Poly-journal.md` an (Dateien → iCloud Drive → Shortcuts). Deine gesamte Historie aus Fragen und Urteilen liegt an einem Ort; erlaube beim ersten Lauf den Dateizugriff mit **Immer erlauben**.
- **Start ohne Hände:** Einstellungen → Action Button → „Kurzbefehl ausführen“ → Poly. Oder ein Doppeltippen auf die Rückseite des Geräts: Einstellungen → Bedienungshilfen → Tippen → Auf Rückseite tippen → Poly. Per Stimme: „Hey Siri, Poly“.
- **Mehr Einstiegspunkte:** ein Widget auf dem Home- oder Sperrbildschirm (Home-Bildschirm lange drücken → + → Shortcuts → Poly); das Kontrollzentrum (Einstellungen → Kontrollzentrum → „Shortcuts“ hinzufügen); ein NFC-Tag auf dem Schreibtisch oder im Auto (Shortcuts → Automation → NFC → Poly ausführen).
- **Fotos ins Duett:** Der Hauptweg ist der Begleiter **Poly Photo** (Foto/PDF teilen → Texterkennung → Poly startet für dich). Für eine *visuelle* Deutung eines Bildes (nicht des Textes darauf) nimm das Kamera-Widget von Claude → Analyse → Kopieren → den Text in Poly teilen.
- **Eigene Texte prüfen:** Markiere deinen Entwurf irgendwo → Teilen → Poly → Modus **🩺 Berater** — er prüft, ohne umzuschreiben (und wird nie zum Co-Autor).
- **Auf iPhone 15 Pro und neuer:** Shortcuts hat eine Aktion „Modell verwenden“ (Apple Intelligence, kostenlos, ohne Internet), mit der sich Poly erweitern lässt — etwa für eine automatische Modusauswahl. Auf iPhone 14 und älter gibt es die Aktion nicht; Poly funktioniert auch ohne sie einwandfrei.
- **Sofort zuhören (optional):** Klapp im Kurzbefehl-Editor die erste „Frage“-Aktion auf und aktiviere den Schalter fürs sofortige Diktieren — dann lauscht das Gerät direkt nach dem Antippen des Symbols auf deine Frage. Standardmäßig aus, weil das für getippten Text und das Teilen-Menü bequemer ist.

## Über iCloud — kein bezahlter Plan nötig

Poly braucht kein kostenpflichtiges iCloud. Der Kernablauf (Frage → beide KIs → Antwort auf dem Bildschirm und in der Zwischenablage) rührt iCloud überhaupt nicht an. Nur zwei optionale Annehmlichkeiten nutzen es: das Lauf-Journal und die Bilddatei — beide im Kilobyte-Bereich, und die kostenlosen 5 GB jeder Apple-ID decken davon Jahrzehnte ab. Ist iCloud Drive aus oder voll, landet die Antwort trotzdem auf deinem Bildschirm und in deiner Zwischenablage (das ist von der Konstruktion her garantiert) — nur der Journaleintrag entfällt. Du willst gar kein Journal? Siehe „Privatsphäre“ weiter unten.

## Privatsphäre

`Poly-journal.md` speichert jede Frage und jede Antwort im Klartext in iCloud Drive. Du willst keine Historie? Lösch die Journal-Aktion im Kurzbefehl-Editor. Um Vorhandenes zu tilgen, lösch die Datei `Poly-journal.md` in Dateien. Wird das Journal zu groß, benenne die Datei einfach um (z. B. in `Poly-journal-august.md`) — beim nächsten Lauf entsteht automatisch ein neues.

## Wenn etwas klemmt

- **ChatGPT sagt „You are logged out“** (obwohl du eindeutig angemeldet bist) — öffne die ChatGPT-App, schließ sie, starte Poly neu. Ein bekannter Aussetzer, der sich immer so beheben lässt.
- **Claude sagt „This model isn't available right now“** — das Tageslimit des kostenlosen Claude ist erreicht, oder in der Claude-App ist ein Modell gewählt, das dein Tarif nicht enthält. Wähle Sonnet in der Claude-App oder warte, bis das Limit zurückgesetzt wird; bis dahin prüft Trio mit einer kostenlosen KI per Schlüssel.
- **Claude schweigt / leere Antwort bei einer langen Frage** — die Claude-Aktion hat einen Timeout: Sie kann die Kontrolle zurückgeben, bevor Claude fertig ist, während Claude die Antwort in der eigenen App weiterschreibt. Öffne Claude, dort steht die Antwort — kopiere sie mit der Taste der App. Fürs nächste Mal: Eine kürzere Frage kommt zuverlässiger zurück. Ist es schlicht fehlgeschlagen, wisch Shortcuts aus der App-Übersicht und starte neu.
- **Poly weitergeben:** Verschick `Poly.shortcut` als einzelne Datei, nicht gezippt (ein Zip bedeutet auf dem Handy zusätzliche Schritte). In Telegram: Datei lange drücken → Teilen/In Dateien sichern, nicht ein einzelner Tipp.
- **Benenn den Poly-Kurzbefehl nicht um.** Die Begleiter Photo und Compress sowie die Taste „🔁 Anderer Modus“ rufen ihn alle unter dem exakten Namen „Poly“ auf. Benennst du ihn um (oder importierst ihn erneut und endest bei „Poly 1“), hören diese drei Wege stillschweigend auf zu funktionieren. Entsteht bei einer Neuinstallation ein Duplikat, lösch den alten Kurzbefehl und behalte genau einen namens „Poly“.
- **Schwächere Antworten als erwartet** — die Aktion nutzt das Modell, das in der Claude-App als Standard eingestellt ist: Claude öffnen, Modell wechseln, App schließen, Poly neu starten. Gute Gewohnheit: Vor einem wichtigen Lauf das Modell in Claudes Kopfzeile prüfen.
- **Über „Teilen“ kam nur ein nackter Link an und nichts passierte** — die Aktionen rufen Webseiten nicht selbst ab: Öffne die Seite, markiere einen Teil des Textes und teile diesen Text.
- **Bonus:** Die finale Antwort geht auch in die geteilte Zwischenablage (Universal Clipboard) — auf einem Mac oder iPad fügst du sie mit Cmd+V ein, ohne das Handy anzufassen.
- **Nach einem großen iOS-Update** (etwa auf iOS 27) starte einen Test-Lauf mit Kritik. Ein großes Shortcuts-Update kann Berechtigungen erneut abfragen oder eine zusätzliche „Fertig“-Karte zeigen — ein Lauf bringt das zum Vorschein und erledigt es.
- Die Nachrichtenkosten gehen von deinen **Abos** beim jeweiligen Dienst ab (keine API) und teilen sich die Limits mit deinen normalen Chats. Verwendet wird jeweils das Modell, das in der App als Standard eingestellt ist.

## Was nach der finalen Antwort kommt

Unter dem Abschlussbildschirm fragt Poly: **„✅ Fertig“** oder **„🔁 Anderer Modus — dieselbe Frage“**. Die zweite Option startet Poly mit bereits eingetragener Frage neu (du kannst sie bearbeiten) und lässt dich einen anderen Modus wählen. Praktisch, um erst Kritik laufen zu lassen und direkt danach die Streitkarte zur selben Frage — ohne alles neu zu tippen.
