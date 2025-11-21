""" *************************************************************
Aufgabe 4 Kleines Einmaleins als formatierte Tabelle mit 2D-Liste
**************************************************************""" 

# Dieses Programm erstellt die Multiplikationstabelle mit einer 2D-Liste und gibt sie formatiert aus.

# Die maximale Zahl fuer die Multiplikation wird festgelegt 
MAX_FAKTOR = 10

# 1. Erstellung der zweidimensiunalen Liste

# Die Hauptliste, die alle Zeilen der Tabelle enthalten wird
tabelle_ergebnisse = []

# Aeussere Schleife: Geht die Zahlen von 1 bis 10 durch 
for faktor_zeile in range(1, MAX_FAKTOR + 1):
    
    # Eine neue Liste für die aktuelle Zeile wird erstellt
    aktuelle_reihe = []

    # Innere Schleife: Geht die Zahlen von 1 bis 10 durch 
    for faktor_spalte in range(1, MAX_FAKTOR + 1):
        
        # Das Multiplikationsergebnis wird berechnet
        produkt = faktor_zeile * faktor_spalte
        
        # Das Ergebnis wird zur aktuellen Reihe hinzugefügt
        aktuelle_reihe.append(produkt)

    # Die fertige Reihe wird zur Haupttabelle hinzugefügt
    tabelle_ergebnisse.append(aktuelle_reihe)


# ----------------------------------------------------------------------
# 2. Formatierte Ausgabe der Tabelle

# Es wird eine feste Breite von 4 Zeichen pro Zahl gewaehlt, um eine saubere, untereinander ausgerichtete Ausgabe zu gewaehrleisten 
SPALTEN_BREITE = 4

print("\n--- Das Kleine Einmaleins ---\n")

# Kopfzeile mit den Spaltenfaktoren (1 bis 10) wird erstellt.
kopfzeile = " " * SPALTEN_BREITE  # Platz für die erste leere Zelle
for z in range(1, MAX_FAKTOR + 1):
    # Die Zahl wird rechtsbündig in der festgelegten Breite formatiert.
    kopfzeile += f"{z:>{SPALTEN_BREITE}}"
print(kopfzeile)

# Eine Trennlinie wird ausgegeben.
print("=" * (SPALTEN_BREITE * (MAX_FAKTOR + 1)))

# Die Zeilen der Tabelle werden ausgegeben
# index läuft von 0 bis 9.
for index in range(MAX_FAKTOR):
    
    # Der Zeilenfaktor ist der Index + 1.
    faktor_links = index + 1

    # Die Ausgabezeile wird mit dem Zeilenfaktor (rechtsbuendig) gestartet.
    ausgabe_text = f"{faktor_links:>{SPALTEN_BREITE}}"

    # Die Ergebnisliste für die aktuelle Reihe wird geholt.
    ergebnis_reihe = tabelle_ergebnisse[index]

    # Jedes Ergebnis aus der Reihe wird angefuegt.
    for zahl in ergebnis_reihe:
        # Das Ergebnis wird ebenfalls rechtsbuendig formatiert und angehaengt.
        ausgabe_text += f"{zahl:>{SPALTEN_BREITE}}"

    # Die vollstaendige, formatierte Zeile wird ausgegeben.
    print(ausgabe_text)

print("\n------------------------------")


