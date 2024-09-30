import json

frukt = {
  'ananas': {
    'namn': 'ananas', 
    'pris': 25,
    'antal': 20
  },
  'kiwi': { 
    'namn': 'kiwi',
    'pris': 15,
    'antal': 32
  },
  'päron': {
    'namn': 'päron',
    'pris': 10,
    'antal': 4
  }
}

# print(frukt)
# print(f"Info för päron är {frukt['frukt3']}")

# for brand_info in frukt.values():
#     all_info = f"Pris för {brand_info['namn']} är: {brand_info['pris']}"
#     print(all_info.lower())

# dict_data_from_json = {}

with open('frukt.json', 'w', encoding='utf-8') as jsonfile:
  json.dump(frukt, jsonfile, ensure_ascii=False, indent=2)

with open('frukt.json', 'r', encoding='utf-8') as json_read_file:
  dict_data_from_json = json.load(json_read_file)
  print(dict_data_from_json)

# for k, v in dict_data_from_json.items():
#   print(f"Id: {k}\nInfo om frukt: {v.values()}")
#   print(v)
#   print("-----------------")
#   for v in v.values():
#     print(v, end=' ,')
#   print("\n---------------")

# for v in dict_data_from_json.values():
#   print(f"Värden för frukt är följande: {v['namn']}")