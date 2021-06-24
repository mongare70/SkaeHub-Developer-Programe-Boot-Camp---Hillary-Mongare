import numpy as np

print("Python program to find the number of weekdays in a certain month in the year of your choice")

year = input("Enter the year of your choice: ")

month = input("Enter the month of your choice (1-12): ")

# if month is between January and November
if int(month) < 12:
    next_month = int(month)+1

# if month is December
elif int(month) == 12:
    next_year = str(int(year)+1)
    
    next_month = 1
    next_month = str(f"{next_month:02}")

    number_of_weekdays = np.busday_count("{}-{}".format(year, month), "{}-{}".format(next_year, next_month)) 
    print("The number of weekdays in the month of {}-{} are: {}".format(year, month, number_of_weekdays))

    exit()

else:
    print("Enter months 1-12!")
    exit()

if len(month) <= 2:
    month = str(f"{int(month):02}")
    next_month = str(f"{next_month:02}")

number_of_weekdays = np.busday_count("{}-{}".format(year, month), "{}-{}".format(year, next_month)) 
print("The number of weekdays in the month of {}-{} are: {}".format(year, month, number_of_weekdays))