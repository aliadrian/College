class Shopping_item:
  def __init__(self, name, price, total):
    self.__name = name
    self.__price = price
    self.__total = total

  def set_name(self, name):
    self.__name = name

  def set_price(self, price):
    self.__price = price

  def set_total(self, total):
    self.__total = total

  def get_name(self):
    return self.__name

  def get_price(self):
    return self.__price

  def get_total(self):
    return self.__total

  def __str__(self):
    utskrift = f"Produktnamn: {self.get_name()}\n" + \
    f"Pris: {str(self.get_price())}\n" + \
    f"Antal: {str(self.get_total())}" 
    return utskrift

