# Was ist Poly?

C1M ist das Projekt; **Poly** ist das, was du tatsächlich auf dein Handy bekommst. Diese Seite erklärt es in einfachen Worten.

## Was es eigentlich ist

Poly ist ein Knopf auf deinem iPhone, hinter dem zwei KIs stecken. Du stellst eine Frage, und ChatGPT und Claude bearbeiten sie als Paar: Eine antwortet, die andere prüft nach und verbessert — oder beide antworten unabhängig und ihre Antworten werden zusammengeführt, je nach gewähltem Modus. Das Ergebnis landet auf deinem Bildschirm, in deiner Zwischenablage und in einem Journal.

Der Punkt ist Verdichtung. Die alte Abfolge — ChatGPT öffnen, fragen, kopieren, Claude öffnen, einfügen, um eine Prüfung bitten, die Endfassung kopieren — schrumpft auf einen Tipp und rund anderthalb Minuten Warten. Und es ist nicht nur schneller, es ist besser: Eine zweite KI findet tatsächlich die Fehler der ersten. Genau deshalb schlägt ein Paar ein einzelnes Modell.

Es ist keine App aus dem App Store. Es ist ein **Kurzbefehl** für Apples eingebaute App Shortcuts — deshalb installiert es sich mit einem Tipp auf eine Datei und sitzt danach wie ein ganz normales Symbol auf deinem Home-Bildschirm.

## Was es kostet

- **Poly selbst ist kostenlos.** Es ist eine Datei, kein Dienst — kein Abo für Poly, keine Werbung, keine Datensammlung.
- **Die Kosten gehen von deinen ChatGPT- und Claude-Abos ab.** Jeder Lauf verbraucht 1 bis 4 Nachrichten (der Preis steht mit einem ✉-Zeichen direkt im Menü). Er teilt sich die Limits mit deinen normalen Chats in diesen Apps.
- **Kostenlose Konten funktionieren** — das kostenlose Claude nutzt Sonnet 5.5, dasselbe Modell wie das bezahlte Abo; es hat ein Tageslimit. ChatGPT funktioniert so oder so, im Rahmen der eigenen Limits.
- **Kein bezahltes iCloud nötig:** Das Journal ist ein paar Kilobyte groß; die kostenlosen 5 GB decken Jahrzehnte davon ab. Schalte iCloud ab, und die Antwort kommt trotzdem — nur der Journaleintrag entfällt.

## Was du vor der Installation brauchst

Ein iPhone mit iOS 18 oder neuer, mit den installierten Apps ChatGPT und Claude, in beiden angemeldet. Mehr nicht. Die Installation ist ein Tipp auf die Datei `Poly.shortcut` — die Schritt-für-Schritt-Anleitung für Nicht-Techniker steht in `install.md`.

## Wo Poly sich bezahlt macht

- **Schreiben:** Korrektur, bevor du auf Senden tippst; eine unangenehme eingehende Nachricht entschlüsseln; übersetzen und feinschleifen.
- **Entscheidungen:** „soll ich das kaufen“, „soll ich wechseln“, „soll ich das starten“ — ein schneller Blick gegen einen vorsichtigen, dann ein Plan und die Risiken.
- **Fragen mit viel auf dem Spiel** (medizinisch, juristisch, finanziell): zwei unabhängige Meinungen und eine ehrliche Karte der Streitpunkte statt einer selbstsicheren Stimme.
- **Dein eigener Text, unverändert:** Der Modus Berater prüft, ohne zum Co-Autor zu werden.
- **Unterwegs:** der Begleiter Voice — Frage diktieren, Antwort vorgelesen bekommen.
- **Bilder:** zwei Vektorskizzen von zwei verschiedenen KI-Künstlern zur Auswahl.

Fertige Formulierungen für über 20 Aufgaben stehen in `recipes.md`.

## Die ehrlichen Nachteile

- **Während Poly läuft, lass das Handy in Ruhe** (etwa 1–2 Minuten) — eine Berührung des Bildschirms bricht den Lauf ab. Das ist eine Grenze von Apples Plattform, nicht von Poly. Die Ausnahme ist der Modus Rückfrage, der von selbst ein Fenster öffnet und dich um Antworten bittet.
- **Es ist keine Magie im Hintergrund.** Das Handy muss entsperrt sein, die Apps kommen nacheinander in den Vordergrund, in strenger Reihenfolge. Poly ist ein Knopf, den du drückst und auf den du wartest, kein Roboter mit Zeitplan.
- **Die ChatGPT-Aktion kann spinnen:** Manchmal behauptet sie „you are logged out“, obwohl du eindeutig angemeldet bist. Immer behebbar: ChatGPT-App öffnen, schließen, Poly neu starten.
- **Lange Fragen sind riskant:** Die Claude-Aktion hat einen Timeout — bei einer sehr langen Frage kann das Endergebnis leer zurückkommen, und du musst die vollständige Antwort aus der Claude-App selbst holen. Kürzere Fragen kommen zuverlässiger zurück.
- **Das Modell lässt sich nicht aus Poly heraus wählen:** Es nutzt, was in der jeweiligen App als Standard eingestellt ist. Prüfe das Modell in Claude vor einem Lauf, der zählt.
- **Ein großes iOS-Update kann einen Testlauf verlangen** — ein großes Update kann Berechtigungen erneut abfragen.

## Ratlos bei der Modusauswahl?

Öffne im Poly-Menü **📂 Mehr…** → **ℹ️ Was ist Poly** — eine kurze Erklärung jedes Modus, direkt auf deinem Handy, kostenlos. Danach bietet Poly an, dich mit derselben Frage zurück zur Modusauswahl zu bringen.

## Und die anderen KIs — die halbe Arbeit ist dir schon abgenommen

Alles bisher dreht sich um das Paar, denn genau dieses Paar läuft von selbst. Aber auf deinem Handy stecken wahrscheinlich mehr als zwei KIs: Gemini, Grok, DeepSeek, Qwen, Copilot, welche du eben magst. Poly kann auch die hinzuziehen — halbmanuell, und es lohnt sich zu wissen, was das genau heißt.

Bisher hieß „fünf KIs dieselbe Frage stellen“: alles von Hand machen. Die Frage fünfmal schreiben, fünf Antworten auseinanderhalten und sie am Ende selbst zusammenführen. **Poly Multi nimmt dir rund die Hälfte davon ab.** Es schreibt den Prompt, legt ihn in deine Zwischenablage, führt dich eine App nach der anderen durch, sammelt jede Antwort ein, sobald du sie kopiert hast, und übergibt den ganzen Stapel an Claude — der macht daraus ein Dokument, in dem die Widersprüche stehen bleiben. Bei dir bleibt nur, was allein du tun kannst: deine App öffnen, einfügen, abschicken, die Antwort kopieren, zurückkommen.

Es ist also nicht „Poly steuert deine anderen Apps“ — hier wird keine fremde Software automatisiert. Es sind deine eigenen drei Berührungen pro KI, nur das Denken, die Reihenfolge und das Zusammenführen übernimmt Poly für dich. Wenn du das bisher von Hand gemacht hast, geht es etwa doppelt so schnell — und am Ende steht ein Dokument statt fünf Tabs.

Dahin geht das Projekt: mehr Chor, weniger Handarbeit, in dem Maß, wie sich die Apps öffnen. Vorerst läuft das Paar von selbst und der Rest halbmanuell — und das sagen wir lieber offen, statt etwas anderes zu versprechen. Poly Multi kommt neben dem Haupt-Kurzbefehl; hol es dir, wenn dir das Paar in Fleisch und Blut übergegangen ist.

## In einem Satz

Ein kostenloser Knopf, der zwei deiner bezahlten Abos zusammenarbeiten und einander prüfen lässt: ein Preis — 1 bis 4 Nachrichten pro Lauf — und eine Gewohnheit — antippen und das Handy anderthalb Minuten in Ruhe lassen.
