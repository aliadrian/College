from tkinter import messagebox, simpledialog

# Prompt the user to write price of each item
price_of_item_1 = simpledialog.askinteger(title="Item 1", prompt="What is the price of your first item? ")
price_of_item_2 = simpledialog.askinteger(title="Item 2", prompt="What is the price of your second item? ")
price_of_item_3 = simpledialog.askinteger(title="Item 3", prompt="What is the price of your third item? ")
price_of_item_4 = simpledialog.askinteger(title="Item 4",prompt="What is the price of your fourth item? ")
price_of_item_5 = simpledialog.askinteger(title="Item 5", prompt="What is the price of your fifth item? ")

# Calculation of the total price
total = price_of_item_1 + price_of_item_2 + price_of_item_3 + price_of_item_4 + price_of_item_5

# Calculation of tax
sales_tax = total * 0.7

# Output of the total and tax
messagebox.showinfo(title=f"Total of sale and tax\n",message=f"Total of the sale: {total}\nTax: {sales_tax:,.0f}$")