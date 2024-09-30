def loop_over_days(day_of_week):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    # range (7) genereates the sequence of number 0, 1, 2, 3, 4, 5, 6
    # and the loop adjusts for the index offset by adding 1 when comparing
    # with "day_of_week"
    for i in range(7):
        if day_of_week == i + 1:
            return days[i - 1]
    
    return "Invalid day"

day_of_week = int(input("Write a number between 1 and 7? "))

result = loop_over_days(day_of_week)
print(result)