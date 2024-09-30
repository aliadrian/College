from tkinter import simpledialog, messagebox

# Initialisering av variabler
siffra = 0
summa = 0

# Input och process
while siffra >= 0: 
  siffra = simpledialog.askinteger("Siffror", "Ange positiva siffror, för att avsluta programmet ange en negativ siffra: ")
  if siffra < 0:
    break
  summa += siffra

# Output
messagebox.showinfo("Resultat", f"Summan är: {summa}")
  
