#import math module
import math

#function to find the square root of n
def square_root_of_n(n):
    return math.sqrt(n)

#function to find if n is a whole number
def test_if_int(n):
    x = int(n)
    
    temp = n - x

    if temp > 0:
        return False
    
    return True

try: 
    number = int(input("Enter a number: "))

    if number > 0:
        x = square_root_of_n(number)
        y = test_if_int(x)
        
        if y:
            print("{} is a perfect square".format(number))
        
        else:
            print("{} is not a perfect square".format(number))

    else:
        x = square_root_of_n(abs(number))
        y = test_if_int(x)
        
        if y:
            print("{} is a perfect square".format(number))
        
        else:
            print("{} is not a perfect square".format(number))

except ValueError:
    print("Error: you must enter a number")
