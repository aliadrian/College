number = 0
def get_number_input():
  number = int(input("Write a number: "))
  return number

# help(get_number_input)
# tal1 = get_number_input()
# tal2 = get_number_input()

# print(tal1 + tal2)

# sum = 0
# for counter in range(3):
#   number = get_number_input()
#   sum += number
  
# print(sum)

def calc_cube_vol(side):
  cube_vol = side * side * side
  return cube_vol

cube_volume = calc_cube_vol(3)
print(f"Volume of the cube is {str(cube_volume)}")