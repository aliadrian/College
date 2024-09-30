class Vara:
    # Här definierar vi konstruktorn
    def __init__(self, name, amount, price):
        self.name = name
        self.amount = amount
        self.price = price

    # Här använder vi oss av set-metoden
    def set_name(self, name):
        self.name = name

    def set_amount(self, amount):
        self.amount = amount

    def set_price(self, price):
        self.price = price

    # Här använder vi oss av get-metoden
    def get_name(self):
        return self.name

    def get_amount(self):
        return self.amount

    def get_price(self):
        return self.price

    # Här använder vi oss av sträng-metoden
    def __str__(self):
        print_data = "Varunamn: " + self.get_name() + "\nLagersaldo: " + \
                   str(self.get_amount()) + "\nPris: " + \
                   str(self.get_price()) +"\n----------------"
        return print_data