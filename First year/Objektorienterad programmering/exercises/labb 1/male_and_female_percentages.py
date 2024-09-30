# Dialogruta och meddelandebox som importeras från ett paket som kallas för tkinter
from tkinter import simpledialog,messagebox

# Här skapar vi dialogrutor som användaren fyller i och som sparas i variabler 
males = simpledialog.askinteger('Input', "How many males in the class: ")
females = simpledialog.askinteger('Input', "How many females in the class: ")

# Detta beräknar totala antalet studenter som sparas i en ny variabel (som kallas för students)
students = males + females

# Detta beräknar antalet tjejer och killar som sedan omvandlas till procent
percentage_of_males = males / students * 100
percentage_of_females = females / students * 100

# Sen skrivs resultatet ut i en meddelande ruta
messagebox.showinfo(title="Percentage of males and females", message=f"Percentage of males is: {percentage_of_males:.0f}%\nPercentage of females: {percentage_of_females:.0f}%")
