import json
from vara import Vara
import PySimpleGUI as sg

# Funktion för att ladda varor från en JSON-fil om den finns, annars returnera en tom lista
def load_items_from_json(filename):
    try:
        with open(filename, 'r', encoding='utf-8-sig') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return {}

# Funktion för att spara varor till en JSON-fil
def save_items_to_json(items, filename):

    try:
        with open(filename, 'r', encoding='utf-8-sig') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}
    
    for item in shopping_list:
        item_name = item.get_name()
        data[item_name] = {
            'name': item.get_name(),
            'amount': item.get_amount(),
            'price': item.get_price()
        }

    with open(filename, 'w', encoding='utf-8-sig') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

# Funktion för att lägga till en vara i shoppinglistan
def add_item(name, amount, price):
    item = Vara(name, amount, price)
    shopping_list.append(item)

# Funktion för att skriva ut antalet varor i shoppinglistan
def print_item_count(window):
    window['-OUTPUT-'].update(f"Antal varor: {len(shopping_list)}")

# Funktion för att söka efter en vara och skriva ut dess information
def search_item(name, window):
    if name in shopping_list:
        window['-OUTPUT-'].update(shopping_list[name])
    else:
        window['-OUTPUT-'].update('Varan hittades inte.')

# Funktion för att skriva ut all information om alla varor
def print_all_items(window):
        output = ""
        for item in shopping_list:
            output += str(item) + "\n"  # Anropa __str__ metoden för varje Vara-objekt
        window['-OUTPUT-'].update(output)

# Funktion för att uppdatera antal och pris på en vara
def update_item(name, amount, price, window):
    if name in shopping_list:
        if amount and price:  # Kontroll om både antal och pris är angivna
            try:
                float_price = float(price)
            except ValueError:
                window['-OUTPUT-'].update('Priset måste vara ett numeriskt värde.')
                return

            shopping_list[name]['amount'] = int(amount)
            shopping_list[name]['price'] = float_price
            window['-OUTPUT-'].update(f'{name} uppdaterad: Lagersaldo: {amount}, Pris: {float_price}')
        else:
            window['-OUTPUT-'].update('Både antal och pris måste vara angivna.')
    else:
        window['-OUTPUT-'].update('Varan hittades inte.')

# Funktion för att ta bort en vara från shoppinglistan
def remove_item(name, window):
    if name in shopping_list:
        del shopping_list[name]
        window['-OUTPUT-'].update(f'{name} har tagits bort.')
    else:
        window['-OUTPUT-'].update('Varan hittades inte.')

# Skapa ett fönster med PySimpleGUI
def create_window():
    layout = [
        [sg.Text('Namn'), sg.InputText(key='-NAME-')],
        [sg.Text('Antal'), sg.InputText(key='-AMOUNT-')],
        [sg.Text('Pris'), sg.InputText(key='-PRICE-')],
        [sg.Button('Lägg till vara', key='-ADD-')],
        [sg.Button('Antal varor', key='-COUNT-')],
        [sg.Button('Sök vara', key='-SEARCH-')],
        [sg.Button('Visa alla varor', key='-PRINT_ALL-')],
        [sg.Button('Uppdatera vara', key='-UPDATE-')],
        [sg.Button('Ta bort vara', key='-REMOVE-')],
        [sg.Button('Spara till JSON', key='-SAVE-')],
        [sg.Button('Hämta från JSON', key='-LOAD-')],
        [sg.Text(size=(40, 20), key='-OUTPUT-')]
    ]
    return sg.Window('Shopping List', layout)

# Huvudfunktionen
def main():
    global shopping_list
    shopping_list_data = load_items_from_json('shopping_list.json')
    shopping_list = []  # Initialisera som en tom lista
    for item_name, item_data in shopping_list_data.items():
        item = Vara(item_name, int(item_data['amount']), int(item_data['price']))
        shopping_list.append(item)

    window = create_window()

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED:
            break

        if event == '-ADD-':
            add_item(values['-NAME-'], int(values['-AMOUNT-']), float(values['-PRICE-']))

        elif event == '-COUNT-':
            print_item_count(window)

        elif event == '-SEARCH-':
            search_item(values['-NAME-'], window)

        elif event == '-PRINT_ALL-':
            print_all_items(window)

        elif event == '-UPDATE-':
            update_item(values['-NAME-'], int(values['-AMOUNT-']), float(values['-PRICE-']), window)

        elif event == '-REMOVE-':
            remove_item(values['-NAME-'], window)

        elif event == '-SAVE-':
            save_items_to_json({item_name: {'name': item.get_name(), 'amount': item.get_amount(), 'price': item.get_price()} for item in shopping_list}, 'shopping_list.json')

        elif event == '-LOAD-':
            dict_from_json = load_items_from_json("shopping_list.json")
            shopping_list.clear()  # Rensa den aktuella listan
            for key, value in dict_from_json.items():
                shopping_list[key] = Vara(value['name'], value['amount'], value['price'])

    window.close()

if __name__ == '__main__':
    main()