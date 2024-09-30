infile = open('numbers.txt', 'r')
medelsnitt = 0
räknare = 0
totala = 0

# Process
for rad in infile:
    totala += int(rad)
    if rad:
      räknare += 1
      medelsnitt = totala / räknare

# Output
print(f"Medelsnittet är: {medelsnitt}")