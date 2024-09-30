from tkinter import messagebox
 
# Konstant för kaloriförbränning per minut
kalorier_per_minut = 4.2
 
# Lista med olika tidsintervall i minuter
tid_intervall = [10, 15, 20, 25, 30]
 
# Skapa en sträng för att hålla tabellhuvudet
result_str = "Tid (min) Förbrända kalorier\n"
 
# En for-loop som itererar över tidsintervallen
for tid in tid_intervall:
    # Beräkna förbrända kalorier för varje tidsintervall
    forbranda_kalorier = kalorier_per_minut * tid
    result_str += f"{tid}\t{forbranda_kalorier}\n"
    # Lägg till raden för det aktuella tidsintervallet i resultatsträngen
messagebox.showinfo("Resultat", f"{result_str}")