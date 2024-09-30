from tkinter import simpledialog, messagebox

# Input
answer_vegetarian = simpledialog.askstring("Input", "Are you a vegetarian?").lower()
answer_vegan = simpledialog.askstring("Input", "Are you a vegan?").lower()
answer_gluten = simpledialog.askstring("Input", "Do you need gluten free?").lower()

# Process and output
if (answer_vegetarian == 'yes' and answer_vegan == 'yes' and answer_gluten == 'yes'):
  messagebox.showinfo("Restaurant", "Corner Café"
    "\nThe Chef’s Kitchen")
elif (answer_vegetarian == 'yes' and answer_vegan == 'no' and answer_gluten == 'yes'):
  messagebox.showinfo("Restaurant", "Main Street Pizza Company")
elif (answer_vegetarian == 'yes' and answer_vegan == 'no' and answer_gluten == 'no'):
  messagebox.showinfo("Restaurant", "Mama’s Fine Italian")
elif (answer_vegetarian == 'no' and answer_vegan == 'no' and answer_gluten == 'no'): 
  messagebox.showinfo("Restaurant", "Joe’s Gourmet Burgers")
else:
  messagebox.showinfo("No restaurant in the list", "You'll have to look for a restaurant that matches that criteria by yourself.")