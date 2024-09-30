from tkinter import messagebox

# Create variables 
miles_per_hour = 70
time1, time2, time3 = 6, 10, 15

# Calculation of the distance and the output of it
distance = miles_per_hour * time1
messagebox.showinfo(title="Total distance", message=f"Distance in 6 hours: {distance} miles")

distance = miles_per_hour * time2
messagebox.showinfo(title="Total distance", message=f"Distance in 10 hours: {distance} miles")

distance = miles_per_hour * time3
messagebox.showinfo(title="Total distance", message=f"Distance in 15 hours: {distance} miles")



# time = [6, 10, 15]
# for i in time:
#   distance = miles_per_hour * i
#   print(f"Distance in {i} hours: {distance}")