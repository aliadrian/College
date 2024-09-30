import json

dict_of_dicts_bilar = {
  'qwe123': {
    'regnr': 'qwe123', 
    'brand': 'volvo',
    'year': '2000'
  },
  'qwe456': { 
    'regnr': 'qwe456',
    'brand': 'saab',
    'year': '2009'
  },
  'qwe789': {
    'regnr': 'qwe789',
    'brand': 'kia',
    'year': '2010'
  }
}

# print(dict_of_dicts_bilar)
# print(f"bilinfo för qwe456 {dict_of_dicts_bilar['qwe456']}")

# for brand_info in dict_of_dicts_bilar.values():
#     all_info = f"Registreringsnummer för {brand_info['brand']} är: {brand_info['regnr']}"
#     print(all_info.lower())

dict_data_from_json = {}

with open('dict_of_dicts_bilar.json', 'w', encoding='utf-8') as jsonfile:
  json.dump(dict_of_dicts_bilar, jsonfile, ensure_ascii=False, indent=2)

with open('dict_of_dicts_bilar.json', 'r', encoding='utf-8') as json_read_file:
  dict_data_from_json = json.load(json_read_file)
  print(dict_data_from_json)

for k, v in dict_data_from_json.items():
  print(f"Regnr: {k}\nInfo om bilen: {v.values()}")
  print(v)
  print("-----------------")
  for v in v.values():
    print(v, end=' ,')
  print("\n---------------")

for v in dict_data_from_json.values():
  print(f"Värden för regnr är följande: {v['regnr']}")