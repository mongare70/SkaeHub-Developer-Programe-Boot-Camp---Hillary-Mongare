#import random module
import random

#The guess function
def guess_number(number):
    guessed_number = random.randint(1, 5)

    if guessed_number == number:
        return True
    else:
        return False

#Randomly selected number between 1 and 5
random_number = random.randint(1, 5)

x = guess_number(random_number)

if x:
    print("Correct guess!")
else:
    print("Wrong guess!")
