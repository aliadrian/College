from tkinter import simpledialog, messagebox

# Initialisering av variabler
mil_per_timme = 0.0
timmar = []
distans = 0

# Input
mil_per_timme = simpledialog.askfloat("Mil per timme", f"Vad är fordonets hastighet i km/h: ")
timmar = simpledialog.askinteger("Timmar", f"Hur många timmar har du rest: ")
resultat_str = "Totala resvägen för varje timme\n"

# Process
for timme in range(1, timmar + 1):
  distans = mil_per_timme * timme
  resultat_str += f"Timme {timme}: {distans}\n"

# Output
messagebox.showinfo("Distance traveled", f"{resultat_str}")  