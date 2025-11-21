# Einmaleins-Tabelle (2D-Liste)

Ein Python-Programm, das eine Multiplikationstabelle (Kleines Einmaleins) generiert, strukturiert speichert und formatiert ausgibt.

## Aufgabenstellung
Erstellung eines Programms mit folgenden Anforderungen:
1.  Berechnung des kleinen Einmaleins (1x1 bis 10x10).
2.  **Datenstruktur:** Zwingende Verwendung einer **zweidimensionalen Liste** (Liste von Listen) zur Speicherung der Ergebnisse *vor* der Ausgabe.
3.  **Formatierung:** Die Ausgabe muss tabellarisch erfolgen, wobei alle Zahlen korrekt untereinander ausgerichtet sein müssen (rechtsbündig).

## Technische Umsetzung
Der Code demonstriert saubere Programmierung durch:
*   **Datenstrukturen:** Aufbau einer Matrix (2D-Liste) mittels verschachtelter Schleifen (`for`-Loops).
*   **String-Formatierung:** Nutzung von f-Strings mit Breitenangabe und Ausrichtung (`f"{wert:>{breite}}"`), um ein perfektes Raster zu erzeugen, egal ob die Zahlen ein-, zwei- oder dreistellig sind.
*   **Dynamik:** Durch Konstanten (`MAX_FAKTOR`, `SPALTEN_BREITE`) ist die Tabelle leicht erweiterbar (z.B. auf das große Einmaleins).

## Nutzung
Führen Sie das Skript in der Konsole aus:

```bash
python main.py
