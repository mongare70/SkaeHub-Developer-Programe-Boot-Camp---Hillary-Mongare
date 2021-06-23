#import math module
import math

#function to check if n is power of 4
def is_power_of_four(n):
    if (n == 0):
        return False
    
    #Divide n by 4 iteratively and exit when n == 1
    while (n != 1):
            if (n % 4 != 0):
                return False
            n = n // 4
             
    return True

try: 
    number = int(input("Enter a positive number: "))

    if number > 0:
        x = is_power_of_four(number)

        if x:
            print("{} is a power of four".format(number))
        
        else:
            print("{} is not a power of four".format(number))

    else:
        print("Invalid Input!")

except ValueError:
    print("Error: you must enter a number")
