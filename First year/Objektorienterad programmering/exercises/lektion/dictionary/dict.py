glass_dict = {'nogger': 15, 'daimstrut': 28, 'cornetto': 24}
glass_dict['päronsplit'] = 20

print(glass_dict)

antal = len(glass_dict)

print(f"Antal glassar i dict: {antal}")

print(f"Pris för daimstrut: {glass_dict["daimstrut"]}")

print(f"Försöker få tag på ett glass som heter piggelin: {glass_dict.get('piggelin', 'finns inte')}")

glass = glass_dict.setdefault('magnum', 30) # Läggs till om den nyckeln inte finns
print(f"Värdet för magnum: {glass}")

glass_dict['cornetto'] = 10 # Skriver över värdet på nyckel cornetto
print(glass_dict)

for glass, pris in glass_dict.items():
  print(f"Glass: {glass}\nPris: {pris}")

for k in glass_dict.keys():
  print(k)

for v in glass_dict.values():
  print(v)

print(f"Summan av alla glasspriser: {sum(glass_dict.values())}")

del glass_dict['nogger']
print(glass_dict)

svar = glass_dict.pop('cornetto', "finns inte") # Returnerar något om man vill skriva ut det till användaren

print(svar)
print(glass_dict)

senaste_tillagda = glass_dict.popitem() # Tar bort den senaste inlagda
print(f"Tog bort den senaste tillagda som är: {senaste_tillagda}")
print(glass_dict)

glass_dict.clear() # Tömmer dict
print(glass_dict)

