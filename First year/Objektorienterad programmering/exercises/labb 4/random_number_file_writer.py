import random

# Input
number = int(input("Write how many numbers you want the file to hold: "))

f = open("random_numbers.txt", 'w')

# Process and output
for i in range(number):
  n = random.randint(1, 500)  
  f.write(str(n) + "\n")