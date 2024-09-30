class Burk:
  def __init__(self, namn, pris, antal):
    self.__namn = namn
    self.__pris = pris
    self.__antal_burkar = antal

  def set_namn(self, namn):
    self.__namn = namn

  def set_pris(self, pris):
    self.__pris = pris

  def set_antal(self, antal_burk):
    self.__antal_burkar = antal_burk
  
  def get_namn(self):
    return self.__namn

  def get_pris(self):
    return self.__pris

  def get_antal(self):
    return self.__antal_burkar
  
  def __str__(self):
    utskrift = f"Namn: {self.get_namn()}\n" + \
    f"Pris: {str(self.get_pris())}\n" + \
    f"Antal: {str(self.get_antal())}" 
    return utskrift

  
burk_obj_1 = Burk("Fanta", 19, 10)
burk_obj_2 = Burk("Coca cola", 10, 20)
burk_obj_3 = Burk("Sprite", 15, 30)

burk_list = [burk_obj_1, burk_obj_2, burk_obj_3]

# antal_burk_2 = burk_obj_2.get_antal()
# print(burk_obj_1.get_antal())
# print(burk_obj_1.get_namn())
# print(burk_obj_3.get_antal())

# print(f"Antalet burkar för burk 2: {burk_obj_2.get_antal()}")
# burk_obj_2.set_antal(30)
# print(f"Antalet burkar för burk 2 nu: {burk_obj_2.get_antal()}")

# print(burk_obj_1)

for burk in burk_list:
  print(burk)
  print("------------------")