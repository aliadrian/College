import burk

burk_obj_4 = burk.Burk('Pepsi', 12, 5)

burk.burk_list.append(burk_obj_4)

# for burk in burk.burk_list:
#    print(burk)
#    print("------------------")

burk_obj_dict = {'id4': burk_obj_4}

for k, v in burk_obj_dict.items():
   print(f"key: {k}\nvalues:\n\tNamn: {v.get_namn()}\n\tPris: {v.get_pris()}\n\tAntal: {v.get_antal()}")