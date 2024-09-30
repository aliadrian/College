f = open("random_numbers.txt", "r")
total = 0
counter = 0

# Process
for i in f:
  total += int(i)
  if i:
    counter += 1

# Output
print(f"Total: {total}\nNumber of random numbers: {counter}")
