from tkinter import simpledialog, messagebox

# Input
mass = simpledialog.askfloat("Mass of Object", "Write the mass of the object in kilograms: ")

# Process (calculation)
weight = mass * 9.8

# Process (if-statements) and output
if (weight < 100): {
  messagebox.showinfo("Light object", "The object is too light.")
} 
elif (weight > 500): {
  messagebox.showinfo("Heavy object", "The object is too heavy.")
}
else: {
  messagebox.showinfo("Weight in newtons", f"Your object weighs {weight:.2f} newtons.")
}