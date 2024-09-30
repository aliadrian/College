import labb6_frukt as frukt

frukt1 = frukt.Frukt(namn='Apelsin', antalFrukt=10, pris=15)
frukt2 = frukt.Frukt(namn='Banan', antalFrukt=20, pris=28)
frukt3 = frukt.Frukt(namn='Kiwi', antalFrukt=6, pris=20)

frukt_lista = [frukt1, frukt2, frukt3]

def main():

    fortsatta = True
    while fortsatta:

        val = int(input("\n1: Lägg till vara\n"
                  "2: Skriva ut hur många varor som finns i listan\n"
                  "3: Ange namn för att skriva ut varan\n"
                  "4: Skriv ut namn på alla varor\n"
                  "5: Skriv ut alla varor\n"
                  "6: Skriv in nytt pris och antal\n"
                  "7: Ta bort vara med namn\n"
                  "8: Avsluta programmet\n"
                  "Välj alternativ: "))

        if val == 1:
            lagg_till()
        elif val == 2:
            antal_varor()
        elif val == 3:
            anvandare_anger_namn()
        elif val == 4:
            skriv_ut_alla_namn()
        elif val == 5:
            skriv_ut_all_info()
        elif val == 6:
            uppdatera_pris_och_antal()
        elif val == 7:
            ta_bort_vara_med_namn()
        elif val == 8:
            print("Här var programmet slut.")
            fortsatta = False
        else:
            print("Snälla välj ett av alternativen.")

def skriv_ut_alla_namn():
    print('I vår shoppinglista finns det')
    for obj in frukt_lista:
        print(f"Namn på frukt: {obj.get_namn()}")

def lagg_till():
    namn = input('Namn på frukt: ')
    antal = input('Antal: ')
    pris = input('Pris: ')

    frukt_obj = frukt.Frukt(namn=namn, antalFrukt=antal, pris=pris)
    frukt_lista.append(frukt_obj)

def antal_varor():
    print(len(frukt_lista))

def anvandare_anger_namn():
    namn = input('Ange namn på vara du vill visa från listan: ')
    for obj in frukt_lista:
        if(namn.lower() == obj.get_namn().lower()):
            print(obj)
            break
    else:
        print("Frukt finns inte.")

def skriv_ut_all_info():
    for obj in frukt_lista:
        print(f"\n{obj}\n")
        print('---------')

def uppdatera_pris_och_antal():
    vilken_frukt = input("Ange namn på varan du vill ändra pris och antal på: ")
    for obj in frukt_lista:
        if(vilken_frukt.lower() == obj.get_namn().lower()):
            nytt_pris = int(input("Ange nytt pris på varan: "))
            nytt_antal = int(input("Ange nytt antal på varan: "))
            obj.set_pris(nytt_pris)
            obj.set_antal(nytt_antal)
            break
    else:
        print("Frukt finns inte.")

def ta_bort_vara_med_namn():
    vilken_frukt = input("Ange namn på varan du vill ta bort: ")
    for obj in frukt_lista:
        if (obj.get_namn().lower() == vilken_frukt.lower()):
            frukt_lista.remove(obj)
            print(f"Du tog bort {vilken_frukt} från listan.")
            print("Dessa varor är kvar:")
            break
    else:
        print("Frukt finns inte.")
    for varor in frukt_lista:
        print(f"{varor.get_namn()}")

main()