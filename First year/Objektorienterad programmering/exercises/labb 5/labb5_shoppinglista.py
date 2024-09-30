shopping_lista = ['tomat', 'apelsin', 'gurka']

def main():

    fortsatta = True
    while fortsatta:

        val = int(input("1: Visa shoppinglista\n"
                  "2: Lägg till vara\n"
                  "3: Skriva ut hur många varor som finns i listan\n"
                  "4: Ange indexnummer för att skriva ut varan\n"
                  "5: Välj vilken du vill ta bort med nummer\n"
                  "6: Skriv in namnet på den du vill ta bort\n"
                  "7: Avsluta program\n\n"
                  "Välj alternativ: "))

        if val == 1:
            skriv_ut()
        elif val == 2:
            lagg_till()
        elif val == 3:
            antal_varor()
        elif val == 4:
            anvandare_anger_index()
        elif val == 5:
            ta_bort_vara()
        elif val == 6:
            ta_bort_namn()
        elif val == 7:
            print("Här var programmet slut!")
            break
        else:
            print("Snälla välj ett av alternativen: ")


def skriv_ut():
    print(shopping_lista)

def lagg_till():
    namn = input('Skriv namnet på varan du vill lägga till: ')
    shopping_lista.append(namn)

def antal_varor():
    print(len(shopping_lista))

def anvandare_anger_index():
    index_nummer = int(input('Ange nummer på vara du vill visa från listan: '))
    print(shopping_lista[index_nummer])

def ta_bort_vara():
    index_nummer = int(input('Ange nummer på vara du vill ta bort från listan: '))
    shopping_lista.pop(index_nummer)
    print(shopping_lista)

def ta_bort_namn():
    namn = input("Ange namnet du vill ta bort: ")
    shopping_lista.remove(namn)
    print(f"Du tog bort {namn}\n")
    print(shopping_lista)

main()



