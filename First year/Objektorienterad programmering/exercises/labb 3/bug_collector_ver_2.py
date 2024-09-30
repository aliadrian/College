from tkinter import simpledialog, messagebox

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
list_of_bugs = []
total = 0

for day in days:
  list_of_bugs = simpledialog.askinteger("Number of bugs",f"How many bugs did you collect on {day}: ")
  bugs = list_of_bugs
  total += bugs

messagebox.showinfo("Total",f"The total number of bugs is collected: {total} bugs")


