def main():
  result_list = [20, 45, 23, 56, 67]
  total = 0
  for i in result_list:
    total += i
  average = total / len(result_list)
  print(average)
  
main()