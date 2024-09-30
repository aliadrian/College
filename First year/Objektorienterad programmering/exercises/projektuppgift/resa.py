class Resa:
  # Konstruktor som initierar en ny Resa-instans med de angivna attributen.
  def __init__(self, rese_id, resetyp, pris, antal_dagar):
    self.__rese_id = rese_id
    self.__resetyp = resetyp
    self.__pris = pris
    self.__antal_dagar = antal_dagar

# Setters för att uppdatera resans attribut.
  
  # Uppdaterar rese_id för resan.
  def set_rese_id(self, rese_id):
    self.__rese_id = rese_id
    
  # Uppdaterar resetyp för resan.
  def set_resetyp(self, resetyp):
    self.__resetyp = resetyp

  # Uppdaterar priset för resan. Förväntar sig ett numeriskt värde.
  def set_pris(self, pris):
    self.__pris = int(pris)

  # Uppdaterar antalet dagar för resan. Förväntar sig ett numeriskt värde.
  def set_antal_dagar(self, antal_dagar):
    self.__antal_dagar = int(antal_dagar)

# Getters för att hämta resans attribut.
  
  # Returnerar rese_id för resan.
  def get_rese_id(self):
    return self.__rese_id
  
  # Returnerar resetyp för resan.
  def get_resetyp(self):
    return self.__resetyp
  
  # Returnerar priset för resan.
  def get_pris(self):
    return self.__pris
  
  # Returnerar antalet dagar för resan.
  def get_antal_dagar(self):
    return self.__antal_dagar
  
  # Returnerar en strängrepresentation av Resa-instansen.
  def __str__(self):
    return f"Rese ID: {self.get_rese_id()}\n" + \
    f"Resetyp: {self.get_resetyp()}\n" + \
    f"Pris: {self.get_pris()}\n" + \
    f"Antal dagar: {self.get_antal_dagar()}"
  
  # Konverterar resan till en dictionary för enklare hantering vid t.ex. JSON-fil.
  def to_dict(self):
    return {
      "rese_id": self.get_rese_id(),
      "resetyp": self.get_resetyp(),
      "pris": self.get_pris(),
      "antal_dagar": self.get_antal_dagar()
    }
  
  # Uppdaterar alla attribut för resan och hanterar eventuella fel.
  def uppdatera_alla_objekt(self, nytt_resetyp, nytt_pris, nytt_antal_dagar):
    try:
        self.set_resetyp(nytt_resetyp)
        self.set_pris(int(nytt_pris))
        self.set_antal_dagar(int(nytt_antal_dagar))
        print(f"Resan till {self.get_rese_id()} har uppdaterats.")
        print(f"Resetyp: {nytt_resetyp}")
        print(f"Pris: {nytt_pris}")
        print(f"Antal dagar: {nytt_antal_dagar}")
        return True
    except Exception as e:
        print(f"Gick inte att uppdatera: {e}")
        return False
