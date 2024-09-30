import PySimpleGUI as sg
import json
import os.path
import frukt

def main():
    global frukt_dict
    filnamn = "frukt.json"
    json_file_exists = os.path.exists(filnamn)

    frukt_dict = {}

    if json_file_exists:
        frukt_dict = hamta_data_fran_json(filnamn)
    else:
        frukt_obj1 = frukt.Frukt("ananas", 25, 20)
        frukt_obj2 = frukt.Frukt("kiwi", 15, 32)
        frukt_obj3 = frukt.Frukt("päron", 10, 4)

        frukt_dict = {
            frukt_obj1.get_namn(): frukt_obj1,
            frukt_obj2.get_namn(): frukt_obj2,
            frukt_obj3.get_namn(): frukt_obj3,
        }

    antal_frukt = f"Totalt antal frukt: {str(len(frukt_dict))}"

    sg.theme('DarkAmber')

    layout = [
        [sg.Text('Namn'), sg.InputText(key="namn", do_not_clear=False)],
        [sg.Text('Pris'), sg.InputText(key="pris", do_not_clear=False)],
        [sg.Text('Antal'), sg.InputText(key="antal", do_not_clear=False)],
        [sg.Button("Lägg till"), sg.Button("Visa lista"), sg.Button("Avsluta")],
        [sg.Input(key="sok_input", size=(30, 1), do_not_clear=False), sg.Button('Sök efter frukt')],
        [sg.Listbox(values=list(frukt_dict.keys()), size=(20, 6), key="frukt_listbox", enable_events=True)],
        [sg.Text('Pris'), sg.Input(key="uppdatera_pris", size=(10, 1), do_not_clear=False), sg.Text('Antal'), sg.Input(key="uppdatera_antal", size=(10, 1), do_not_clear=False), sg.Button('Uppdatera pris och antal')],
        [sg.Text('Ta bort varuobjekt'), sg.InputText(key="borttag_namn".lower(), do_not_clear=False), sg.Button("Ta bort")],
        [sg.Output(size=(70, 10), key='output')],
        [sg.Push(), sg.Button("Spara till fil", key="spara_till_json")],
        [sg.Text(antal_frukt, size=(15, 1), key="antal_label")]
    ]

    window = sg.Window("Shopping lista", layout)

    while True:
        event, values = window.read()

        if event == "Avsluta" or event == sg.WIN_CLOSED:
            if filnamn:
                spara_till_json_list(filnamn)
            break
        if event == "Lägg till":
            namn = values.get("namn")
            pris = values.get("pris")
            antal = values.get("antal")

            if namn and pris and antal:  # Ensure all values are not None
                if lagg_till_frukt(window, namn, pris, antal):
                    updatera_antal_label(window)
            else:
                sg.popup("Vänligen fyll i alla fält.")

        elif event == "Ta bort":
            borttag_namn = values["borttag_namn"]
            ta_bort_varuobjekt(window, borttag_namn.lower(), filnamn)
        elif event == "Sök efter frukt":
            sok_efter_frukt(window, values)
        elif event == "Uppdatera pris och antal":
            try:
                selected_frukt = values["frukt_listbox"]

                if selected_frukt:
                    valt_namn = selected_frukt[0]
                    nytt_pris = values["uppdatera_pris"]
                    nytt_antal = values["uppdatera_antal"]
                    
                    if not valt_namn or not nytt_pris or not nytt_antal:
                        sg.popup("Vänligen fyll i alla fält.")
                    else:
                        updatera_pris_antal(window, valt_namn, nytt_pris, nytt_antal, filnamn)
            except Exception as e:
                print("")
        elif event == "frukt_listbox":
          frukt_listbox(window, values)
        elif event == "Visa lista":
            kolla_frukt(window)
        elif event == "spara_till_json":
            spara_till_json_dict()
            print("Varuobjekten har sparats till JSON-filen.")

    window.close()

def hamta_data_fran_json(filnamn):
    frukt_dict = {}
    try:
        with open(filnamn, "r", encoding="utf-8") as json_fil:
            data_fran_json = json.load(json_fil)
            for frukt_data in data_fran_json:
                frukt_namn = frukt_data['namn']
                
                frukt_dict[frukt_namn] = frukt.Frukt(frukt_data['namn'], frukt_data.get('pris', 0), frukt_data.get('antal', 0))
            return frukt_dict
    except FileNotFoundError:
        sg.popup_error(f"Filen '{filnamn}' finns inte. Ingen data gick att hämta.")

def lagg_till_frukt(window, namn, pris, antal):
    global frukt_dict

    if not namn or not pris or not antal:
        sg.popup("Vänligen fyll i alla fält.")
        return False

    try:
        updatera_antal_label(window)
        window['output'].update('')
        print(f"Frukten {namn.lower()} har lagts till.") 

        # Konvertera pris och antal till ints
        pris = int(pris)
        antal = int(antal)

        frukt_dict[namn] = frukt.Frukt(namn.lower(), pris, antal)
        window["frukt_listbox"].update(values=[frukt_obj.get_namn() for frukt_obj in frukt_dict.values()])
        return True
    except ValueError as ve:
        print(f"ValueError occurred: {str(ve)}")
        sg.popup(f"Pris och antal måste vara numeriska värden.")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        sg.popup(f"Något gick fel vid tillägg av frukt: {str(e)}")
        return False



def ta_bort_varuobjekt(window, namn, filnamn):
    global frukt_dict

    if not namn:
        sg.popup("Vänligen ange namnet på varuobjektet som du vill ta bort.")
        return
    if namn in frukt_dict:
        del frukt_dict[namn]
        sg.popup(f"Varuobjektet '{namn}' tas bort från shopppinglistan.")
        updatera_antal_label(window)
        window["frukt_listbox"].update(values=[frukt_obj.get_namn() for frukt_obj in frukt_dict.values()])
    else:
        sg.popup(f"Varuobjektet '{namn}' finns inte i shoppinglistan.")

def sok_efter_frukt(window, values):
    try:
        sok_text = values["sok_input"]
        global frukt_dict

        hittade_frukt = {key: frukt_obj for key, frukt_obj in frukt_dict.items() if sok_text.lower() in frukt_obj.get_namn().lower()}
        
        window["output"].update('')
        if not hittade_frukt:
            sg.popup("Frukten finns inte.")
        else:
            frukt_obj = list(hittade_frukt.values())[0]
            print(frukt_obj)
    except Exception as e:
        print(f"An error occured: {e}")
    
def updatera_pris_antal(window, namn, nytt_pris, nytt_antal, filnamn):
    global frukt_dict

    if namn in frukt_dict:
        frukt_obj = frukt_dict[namn]
        if frukt_obj.updatera_pris_antal(nytt_pris, nytt_antal):
            spara_till_json_list(filnamn)
            updatera_antal_label(window)
            window["output"].update('')
            print(f"Pris och antal för {namn} har uppdaterats.")
        else:
            sg.popup("Uppdatering misslyckades")
    else:
        print("Frukten finns inte.")

def updatera_antal_label(window):
    global frukt_dict
    antal = len(frukt_dict)
    window['antal_label'].update(f"Totalt antal frukt: {antal}")

def frukt_listbox(window, values):
    if values["frukt_listbox"]:
        selected_frukt = values["frukt_listbox"][0]
        frukt_obj = frukt_dict[selected_frukt]
        window["uppdatera_pris"].update(value=frukt_obj.get_pris())
        window["uppdatera_antal"].update(value=frukt_obj.get_totala())
    
def kolla_frukt(window):
    global frukt_dict

    window['output'].update('')
    for frukt_obj in frukt_dict.values():
        print(frukt_obj)
        print("-----------------------------------------")

def spara_till_json_list(filnamn):
    global frukt_dict

    frukt_list = []

    for frukt_obj in frukt_dict.values():
        frukt_list.append({
            "namn": frukt_obj.get_namn(),
            "pris": int(frukt_obj.get_pris()),
            "antal": int(frukt_obj.get_totala())
        })

    with open(filnamn, 'w', encoding="utf-8") as f:
        json.dump(frukt_list, f, ensure_ascii=False, indent=2)

def spara_till_json_dict():
    global frukt_dict

    frukt_dict_for_json = {namn: frukt_obj.to_dict() for namn, frukt_obj in frukt_dict.items()}

    with open('dict_of_dicts_frukt.json', 'w', encoding="utf-8") as f:
        json.dump(frukt_dict_for_json, f, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    main()