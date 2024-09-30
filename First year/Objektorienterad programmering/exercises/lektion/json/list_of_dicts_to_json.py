import json

list_of_dicts = [
    {'regnr': 'qwe123', 'brand': 'volvo', 'year': '2000'}, 
    {'regnr': 'qwe456', 'brand': 'saab', 'year': '2009'},
    {'regnr': 'qwe789', 'brand': 'kia', 'year': '2010'}
  ]

print(list_of_dicts)
print(list_of_dicts[0]['regnr'])

# counter = 0
# for bildict in list_of_dicts:
#   if bildict:
#     print(f"Registrerinsnummer för {list_of_dicts[counter]['brand']} är: {list_of_dicts[counter]['regnr']}")
#     counter += 1

data_from_jsonfile = []

with open('bilar.json', 'w', encoding='utf-8') as outfile:
  json.dump(list_of_dicts, outfile, ensure_ascii=False, indent=2)

with open('bilar.json', 'r', encoding="utf-8") as infile:
  data_from_jsonfile = json.load(infile)
  # print(data_from_jsonfile)
  # print(type(data_from_jsonfile))

for bil in data_from_jsonfile:
  print(bil['brand'])

for bil in data_from_jsonfile:
  if bil['year'] == '2000':
    print(bil['brand'])

for bil in data_from_jsonfile:
  if bil['regnr'] == 'qwe456':
    data_from_jsonfile.remove(bil)

  print(data_from_jsonfile)