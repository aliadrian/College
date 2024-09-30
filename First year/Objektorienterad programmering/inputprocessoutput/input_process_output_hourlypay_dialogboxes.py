from tkinter import messagebox, simpledialog

hours = simpledialog.askfloat("Input", "How many hours did you work?")

payrate = simpledialog.askfloat("Input", "What is your hourly payrate?")

totalPayment = hours * payrate
messagebox.showinfo(title=f"Your total payment: {totalPayment:.2f}", message=f"Your payment will be {totalPayment:.2f} based on the hours worked which was {hours} and with a payrate of {payrate:.2f}. ")