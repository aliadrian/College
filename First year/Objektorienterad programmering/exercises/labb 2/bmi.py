from tkinter import simpledialog, messagebox

# Input
weight = simpledialog.askfloat("Weight", "How much do you weigh?")
height = simpledialog.askfloat("Height", "What's your height?")

# Process (calculations)
# Convert in kilos into pounds
weight_in_pounds = weight *  2.205
# Convert height in cm into inches
height_in_inches = height / 2.54

# Calculate BMI
bmi = weight_in_pounds * 703 / (height_in_inches ** 2)

# Process (if-statements) and output
if bmi < 18.5:
  messagebox.showinfo("Underweight", f"Your BMI is {bmi:.2f}\nAccording to your BMI you're underweight.")
elif bmi > 25:
  messagebox.showinfo("Overweight", f"Your BMI is {bmi:.2f}\nAccording to your BMI you're overweight.")
elif bmi > 18.5 or bmi < 25:
  messagebox.showinfo("Optimal weight", f"Your BMI is {bmi:.2f}\nAccording to your BMI you're weight is considered to be optimal.")