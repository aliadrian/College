from tkinter import simpledialog, messagebox
# Initialisera total_summa till 0
totala_summan = 0

# En for-loop som itererar över fem dagar
for dag in range(1, 6):
    # Användaren får ange antalet buggar för varje dag
    antal_buggar_str = simpledialog.askstring("Antal buggar", f"Ange antalet buggar för dag {dag}: ")

    antal_buggar = int(antal_buggar_str)

    # Lägg till antalet buggar för dagen till den totala summan
    totala_summan += antal_buggar

# Skriv ut den totala summan efter loopen är klar
messagebox.showinfo("Totalt antal buggar", f"Den totala summan av antal buggar under fem dagar är: {totala_summan}")