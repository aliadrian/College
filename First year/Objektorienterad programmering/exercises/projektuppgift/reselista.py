import PySimpleGUI as sg
import json
import os.path
import resa

# Huvudfunktion som kör programmet.
def main():
  filnamn = "resor.json"  # Filnamnet där resor sparas/läses från.
  json_file_exists = os.path.exists(filnamn) # Kontrollerar om filen existerar.

  resor_dict = {}  # Dictionary för att lagra resor.

# Läser in resor från JSON-filen om den existerar, annars skapar två fördefinierade resor.
  if json_file_exists:
    resor_dict = hamta_data_fran_json(filnamn)
  else:
    # Skapar exempelresor och lägger till dem i resor_dict.
    rese_obj1 = resa.Resa("oslo", "weekend", 290, 14)
    rese_obj2 = resa.Resa("bergen", "familjeresa", 450, 21)

    resor_dict = {
      rese_obj1.get_rese_id(): rese_obj1,
      rese_obj2.get_rese_id(): rese_obj2
    }

  sg.theme("DarkGreen2")

  antal_resor = f"Totalt antal resor: {str(len(resor_dict))}"

  # Layout definierar strukturen och innehållet i GUI-fönstret.
  layout = [
    # Inputfält och knappar för att hantera resor.
    [sg.Text("Resenamn"), sg.InputText(key="rese_id", do_not_clear=False)],
    [sg.Text("Resetyp"), sg.InputText(key="resetyp", do_not_clear=False)],
    [sg.Text("Pris"), sg.InputText(key="pris", do_not_clear=False)],
    [sg.Text("Antal dagar"), sg.InputText(key="antal_dagar", do_not_clear=False)],
    [sg.Button("Lägg till"), sg.Button("Visa resor"), sg.Button("Avsluta"), sg.Button("Töm"), sg.Button("Sortera A-Z"), sg.Button("Sortera pris")],
    [sg.Input(key="sok_input", size=(30, 1), do_not_clear=False), sg.Button("Sök efter resetyp")],
    [sg.Listbox(values=list(resor_dict.keys()), size=(20, 6), key="reselista", enable_events=True)],
    [sg.Text("Pris"), sg.Input(key="uppdatera_pris", size=(10, 1), do_not_clear=False), sg.Text("Resetyp"), sg.Input(key="uppdatera_resetyp", size=(10, 1), do_not_clear=False), sg.Text("Antal dagar"), sg.Input(key="uppdatera_antal_dagar", size=(10, 1), do_not_clear=False), sg.Button("Uppdatera")],
    [sg.Text("Ta bort resa"), sg.InputText(key="borttag_rese_id".lower(), do_not_clear=False, size=(50, 1)), sg.Button("Ta bort")],
    [sg.Output(size=(70, 10), key="output")],
    [sg.Push(), sg.Button("Spara", key="spara_till_json")],
    [sg.Text(antal_resor, size=(15, 1), key="antal_label")]
  ]
  # Skapar och visar fönstret med den definierade layouten.
  window = sg.Window("Reselista", layout)

  # Händelseloop för att hantera användarinteraktion.
  while True:
    event, values = window.read()  # Läser händelser och värden från GUI-element.

    # Hanterar olika händelser (knapptryckningar, etc.) och uppdaterar GUI:t därefter.
    if event == "Avsluta" or event == sg.WIN_CLOSED:
      if filnamn:
        spara_till_json_lista(filnamn, resor_dict)
      break

    if event == "Lägg till":
      rese_id = values.get("rese_id")
      resetyp = values.get("resetyp")
      pris = values.get("pris")
      antal_dagar = values.get("antal_dagar")

      if rese_id and resetyp and pris and antal_dagar:
        if lagg_till_resa(window, resor_dict, rese_id, resetyp, pris, antal_dagar):
          uppdatera_antal_label(window, resor_dict)
      else:
        sg.popup("Vänligen fyll i alla fält.")

    elif event == "Ta bort":
      borttag_rese_id = values["borttag_rese_id"]
      ta_bort_reseobjekt(window, borttag_rese_id.lower(), resor_dict)
    elif event == "Sök efter resetyp":
      sok_efter_resa(window, values, resor_dict)
    elif event == "Uppdatera":
    # Hämtar det valda objektet från listboxen
      vald_resa = values.get("reselista", [])
      if vald_resa:
          valt_rese_id = vald_resa[0]  # Antag att endast en kan väljas åt gången
          nytt_resetyp = values["uppdatera_resetyp"]
          nytt_pris = values["uppdatera_pris"]
          nytt_antal_dagar = values["uppdatera_antal_dagar"]
          uppdatera_objekt(window, valt_rese_id, nytt_resetyp, nytt_pris, nytt_antal_dagar, resor_dict, filnamn)

      else:
          sg.popup("Välj en resa från listan först.")
    elif event == "reselista":
      reselista(window, values, resor_dict)
    elif event == "Visa resor":
      visa_lista(window, resor_dict)
    elif event == "Töm":
      tomma_lista(window, resor_dict)
    elif event == "Sortera A-Z":
      sortera_resor_bokstavsordning(window, resor_dict)
    elif event == "Sortera pris":
      sortera_resor_efter_pris(window, resor_dict)
    elif event == "spara_till_json":
      spara_till_json_dict(resor_dict)
      window["output"].update("")
      print("Alla resor har sparats.")

  window.close() # Stänger GUI-fönstret när programmet avslutas.

# De efterföljande funktionerna implementerar logiken för att läsa in resor från fil, lägga till nya resor, uppdatera GUI:t med mera.
  
# Läser in resor från en JSON-fil och returnerar dem som ett dictionary.
def hamta_data_fran_json(filnamn):
  resor_dict = {}
  try:
    with open(filnamn, "r", encoding="utf-8") as f:
      data_fran_json = json.load(f)
      for rese_data in data_fran_json:
        rese_id = rese_data.get("rese_id")
        resetyp = rese_data.get("resetyp")
        pris = rese_data.get("pris", 0)
        antal_dagar = rese_data.get("antal_dagar", 0)

        resor_dict[rese_id] = resa.Resa(rese_id, resetyp, pris, antal_dagar)
      return resor_dict
  except FileNotFoundError:
    sg.popup(f"Filen '{filnamn}' finns inte. Ingen data gick att hämtas.")

# Lägger till en ny resa i systemet baserat på användarinmatning.
def lagg_till_resa(window, resor_dict, rese_id, resetyp, pris, antal_dagar):
    if not rese_id or not resetyp or not pris or not antal_dagar:
        sg.popup("Vänligen fyll i alla fält.")
        return False
 
    try:
        pris = int(pris)
        antal_dagar = int(antal_dagar)
 
        # Kontrollerar om pris och antal dagar är icke-negativa heltal
        if pris < 0 or antal_dagar < 0:
            sg.popup("Pris och antal dagar måste vara positiva heltal.")
            return False
 
        # Kontrollerar att rese_id och resetyp inte enbart är siffror
        if rese_id.isdigit() or resetyp.isdigit():
            sg.popup("Rese ID och resetyp får inte enbart bestå av siffror.")
            return False
 
        # Kontrollerar att rese_id och resetyp är strängar som innehåller bokstäver (tillåter inte enbart siffror)
        if not rese_id.replace(" ", "").isalpha() or not resetyp.replace(" ", "").isalpha():
            sg.popup("Rese ID och resetyp måste vara strängar som innehåller bokstäver.")
            return False
 
        uppdatera_antal_label(window, resor_dict)
        window["output"].update('')
 
        # Kontrollerar om rese_id redan finns
        if rese_id.lower() in resor_dict:
            sg.popup(f"Resan med ID '{rese_id}' finns redan. Ange ett annat ID.")
            return False
 
        # Lägger till den nya resan
        resor_dict[rese_id.lower()] = resa.Resa(rese_id.lower(), resetyp, pris, antal_dagar)
        window["reselista"].update(values=[rese_id for rese_id in resor_dict])
        print(f"Resa {rese_id.lower()} har lagts till.\n")
        print(f"Rese ID: {rese_id}")
        print(f"Resetyp: {resetyp}")
        print(f"Pris: {pris}")
        print(f"Antal dagar: {antal_dagar}")
        return True
    except ValueError as ve:
        print(f"Fel på typ av värde.")
        sg.popup("Pris och antal dagar måste vara numeriska värden.")
        return False
    except Exception as e:
        print(f"Ett oväntat fel inträffade: {str(e)}")
        sg.popup(f"Något gick fel vid tillägg av resa: {str(e)}")
        return False

# Uppdaterar textfältet som visar det totala antalet resor i GUI:t.
def uppdatera_antal_label(window, resor_dict):
  antal = len(resor_dict)
  window["antal_label"].update(f"Totalt antal resor: {antal}")

# Tar bort en specifik resa från systemet baserat på ett givet rese_id.
def ta_bort_reseobjekt(window, rese_id, resor_dict):
  if not rese_id:
      sg.popup("Vänligen ange namnet på resan du vill ta bort.")
      return
  if rese_id in resor_dict:
      del resor_dict[rese_id]
      window["output"].update("")
      if (len(resor_dict)) <= 0:
        print("Det finns inga resor kvar.")
      else:
        print(f"Följande resor finns kvar: \n")
        for rese_obj in resor_dict.values():
          print(rese_obj)
          print("***********************\n")
      window["reselista"].update(values=list(resor_dict.keys()))
      print(f"Resan till {rese_id} togs bort från reselistan.")
      uppdatera_antal_label(window, resor_dict)
  else:
      window["output"].update("")
      print(f"Resa '{rese_id}' finns inte i reselistan.")

# Söker efter resor baserat på resetyp och visar resultatet i GUI:t.
def sok_efter_resa(window, values, resor_dict):
  try:
      sok_text = values["sok_input"]

      if not sok_text.strip():
          sg.popup("Vänligen fyll i sökfältet.")
          return

      hittade_resor = {key: rese_obj for key, rese_obj in resor_dict.items() if sok_text.lower() in rese_obj.get_resetyp().lower()}

      if not hittade_resor:
          sg.popup("Ingen resa matchar sökningen.")
      else:
          window["output"].update("")
          for rese_obj in hittade_resor.values():
              print(f"{rese_obj}\n**************\n")
  except Exception as e:
      sg.popup(f"Ett fel uppstod: {e}")

# Uppdaterar attributen för en befintlig resa baserat på det angivna rese_id.
def uppdatera_objekt(window, rese_id, nytt_resetyp, nytt_pris, nytt_antal_dagar, resor_dict, filnamn):
    if rese_id in resor_dict:
        rese_obj = resor_dict[rese_id]
        window["output"].update('')

        try:
            rese_obj.uppdatera_alla_objekt(nytt_resetyp, nytt_pris, nytt_antal_dagar)
            spara_till_json_lista(filnamn, resor_dict)
            uppdatera_antal_label(window, resor_dict)
        except ValueError as ve:
            sg.popup("Uppdatering misslyckades:", ve)
    else:
        sg.popup("Resan finns inte.")

# Uppdaterar antalet visade resor i GUI:t.
def uppdatera_label(window, resor_dict):
  antal_resor = len(resor_dict)
  window['antal_resor_label'].update(f"Totala antal resor: {antal_resor}")

# Hanterar val av resa från listan i GUI:t och visar detaljer om den valda resan.
def reselista(window, values, resor_dict): 
  try:
      if "reselista" in values:
          selected_resa = values["reselista"][0]
          if selected_resa in resor_dict:
              rese_obj = resor_dict[selected_resa]
              window["uppdatera_resetyp"].update(value=rese_obj.get_resetyp())
              window["uppdatera_pris"].update(value=rese_obj.get_pris())
              window["uppdatera_antal_dagar"].update(value=rese_obj.get_antal_dagar())
          else:
              print("Den valda resan hittades inte.")
      else:
          print("Resan finns inte.")
  except Exception as e:
      print(f"Ett fel uppstod: {e}")

# Visar en lista över alla resor i systemet i GUI:t.
def visa_lista(window, resor_dict):
  window["output"].update("")
  if (len(resor_dict) <= 0):
    print("Det finns inga resor.")
  else:
    for rese_obj in resor_dict.values():
      print(rese_obj)
      print("***********************\n")

# Tömmer listan över resor och uppdaterar GUI:t för att reflektera detta.
def tomma_lista(window, resor_dict, filnamn="resor.json"):
  try:
    resor_dict.clear()
    window["output"].update("Listan har blivit tömd.")
    window["reselista"].update(values=[])
    uppdatera_antal_label(window, resor_dict)
    spara_till_json_lista(filnamn, resor_dict)

    with open(filnamn, "w") as f:
      json.dump([], f)

  except Exception as e:
    print(f"Ett fel uppstod: {e}")

# Sorterar resor i bokstavsordning efter rese_id och uppdaterar GUI:t.
def sortera_resor_bokstavsordning(window, resor_dict):
  sorterade_rese_ids = sorted(resor_dict.keys(), key=lambda x: x.lower())

  window["reselista"].update(values=sorterade_rese_ids)

  print("Resorna har sorterats i bokstavsordning")
  window["output"].update("")

# Sorterar resor efter pris i stigande ordning och visar detta i GUI:t.
def sortera_resor_efter_pris(window, resor_dict):
    # Sorterar resorna baserat på pris i stigande ordning
    sorterade_resor = sorted(resor_dict.items(), key=lambda item: item[1].get_pris())
 
    # Skapar en formatterad sträng med varje resas namn och pris på en egen rad
    sorterad_resa_str = '\n'.join([f"{resa[0]} - {resa[1].get_pris()} kr" for resa in sorterade_resor])
 
    # Uppdaterar listboxen (eller annat lämpligt GUI-element) med de sorterade resorna
    window['output'].update(sorterad_resa_str)

# Sparar den aktuella listan av resor till en JSON-fil.
def spara_till_json_lista(filnamn, resor_dict):

  resor_list = []

  for rese_obj in resor_dict.values():
    resor_list.append({
      "rese_id": rese_obj.get_rese_id(),
      "resetyp": rese_obj.get_resetyp(),
      "pris": int(rese_obj.get_pris()),
      "antal_dagar": int(rese_obj.get_antal_dagar())
    })

    with open(filnamn, "w", encoding="utf-8") as f:
      json.dump(resor_list, f, ensure_ascii=False, indent=2)

# Sparar resorna till en JSON-fil i form av dictionary.
def spara_till_json_dict(resor_dict):
  
  resor_dict_for_json = {rese_id: rese_obj.to_dict() for rese_id, rese_obj in resor_dict.items()}

  with open("dict_of_dicts_resor.json", "w", encoding="utf-8") as f:
    json.dump(resor_dict_for_json, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
  main()

