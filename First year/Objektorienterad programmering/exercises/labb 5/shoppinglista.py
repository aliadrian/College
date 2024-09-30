shopping_lista = ["tomat", "gurka"]

def menu(val):
  match val:
    case 1:
      show_list()
    case 2:
      add_to_list()
    case 3:
      count_products()
    case 4:
      enter_index()
    case 5:
      remove_by_index()
    case 6:
      remove_by_name()
    case 7:
      print("Programmet har avslutats.")
    case _:
      print("\nSnälla välj ett av alternativen.\n")


def show_list():
  print(f"\nShopping lista: {shopping_lista}\n")

def add_to_list():
  while True:
    name = input("Ange namnet på varan du vill lägga till: ")
    try:
      if name.isdigit():
        print("Felaktig input. Var snäll och skriv ett giltigt namn.")
        continue
      if name not in shopping_lista:
        shopping_lista.append(name)
        print(f"\n{name} har lagts till i listan.\nÅterstående listobjekt: {shopping_lista}\n")
        break
      else:
        print(f"{name} finns redan i listan. Försök igen.") 
    except ValueError:
      print(f"Var snäll och skriv ett giltigt namn.")

def count_products():
  print(f"\nDet finns {len(shopping_lista)} varor i shoppinglistan.\n")

def enter_index():
    while True:
      index_nummer = input("Ange indexnummer för att skriva ut en vara: ")
      try: 
        index_nummer = int(index_nummer)
        if index_nummer < len(shopping_lista):
          print(f"\nVaran som skrevs ut är: {shopping_lista[index_nummer]}\n")
          break
        else:
          print("Index utanför gränserna. Försök igen.")
      except ValueError: 
        print("Felaktig input. Ange ett giltigt heltal.") 

def remove_by_index():
  while True: 
    index_nummer = input("Ange indexnummer på varan du vill ta bort: ")
    try: 
      index_nummer = int(index_nummer)
      if 0 <= index_nummer < len(shopping_lista):
        removed_item = shopping_lista.pop(index_nummer)
        print(f"\nDu tog bort {removed_item}\nListan har nu dessa varor kvar: {shopping_lista}\n")
        break 
      else:
        print(f"Finns ingen vara på index {index_nummer}. Försök igen.")
    except ValueError: 
      print("Felaktig input. Ange ett giltigt heltal.")

def remove_by_name():
  while True:
    name = input("Ange namnet på varan du vill ta bort: ")
    try:
      if name.isdigit():
        print("Felaktig input. Var snäll och skriv ett giltigt namn.")
      elif name in shopping_lista:
        shopping_lista.remove(name)
        print(f"\n{name} borttagen från listan.\nÅterstående varor: {shopping_lista}\n")
        break
      else:
        print(f"{name} finns inte i listan. Försök igen.") 
    except ValueError:
      print(f"Var snäll och skriv ett giltigt namn.")

while True:
  val = int(input("1: Visa shoppinglista\n"
                  "2: Lägg till vara\n"
                  "3: Skriv ut hur många varor som finns i listan\n"
                  "4: Ange indexnummer för att skriva ut varan\n"
                  "5: Välj vilken du vill ta bort med nummer\n"
                  "6: Skriv in namnet på den du vill ta bort\n"
                  "7: Avsluta program\n\n"
                  "Välj alternativ: "))
  menu(val)
  if(val == 7):
    break

  def main():
    menu()