class Frukt:
  def __init__(self, namn, pris, totala):
    self.__namn = namn
    self.__pris = pris
    self.__totala = totala

  def set_namn(self, namn):
    self.__namn = namn

  def set_pris(self, pris):
    self.__pris = pris

  def set_totala(self, totala):
    self.__totala = totala

  def get_namn(self):
    return self.__namn

  def get_pris(self):
    return self.__pris

  def get_totala(self):
    return self.__totala

  def __str__(self):
    return f"Produktnamn: {self.get_namn()}\n" + \
    f"Pris: {self.get_pris()}\n" + \
    f"Antal: {self.get_totala()}" 
  
  def to_dict(self):
    return {
      "namn": self.get_namn(),
      "pris": self.get_pris(),
      "antal": self.get_totala()
    }

  def updatera_pris_antal(self, nytt_pris, nytt_antal):
      try:
          self.set_pris(int(nytt_pris))
          self.set_totala(int(nytt_antal))
          print(f"Pris och antal för {self.get_namn()} har uppdaterats")
          return True
      except Exception as e:
          print(f"Error updating price and quantity: {e}")
          return False
      

frukt_dict = {}