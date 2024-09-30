# Vi använder dialogrutor och meddelandebox som importeras från ett paket som kallas för tkinter
from tkinter import simpledialog,messagebox

# Här skapas det dialogrutor som användaren fyller i och som sparas i variabler 
namn = simpledialog.askstring("Namn", "Fyll i ditt namn: ")
adress = simpledialog.askstring("Adress","Fyll i din adress:")
stad = simpledialog.askstring("Stad", "Vart bor du:")
postnummer = simpledialog.askstring("Postnummer", "Fyll i ditt postnummer:")
mobilnummer = simpledialog.askstring("Mobilnummer", "Fyll i nummer:")
högskoleprogram = simpledialog.askstring("Högskoleprogram","Skriv in ditt program du går:")
 
# Dessa variabler som användaren fyllde i skrivs ut i en meddelanderuta till användaren
messagebox.showinfo(title=f"Information",
                    message=f" Namn: {namn}"
                            f"\n Adress: {adress}"
                            f"\n Stad: {stad}"
                            f"\n Postnunmmer: {postnummer}"
                            f"\n Mobilnummer: {mobilnummer}"
                            f"\n Högskoleprogram: {högskoleprogram}")
 