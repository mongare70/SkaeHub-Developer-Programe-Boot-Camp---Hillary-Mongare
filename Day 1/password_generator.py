import random

import string

def generate_medium_password():
    random_source = string.ascii_letters + string.digits + string.punctuation

    #1 lowercase
    password = random.choice(string.ascii_lowercase)

    #1 uppercase
    password += random.choice(string.ascii_uppercase)

    #1 number
    password += random.choice(string.digits)

    #1 symbol
    password += random.choice(string.punctuation)

    #generate other characters

    for i in range(6):
        password += random.choice(random_source)

    password_list = list(password)

    #shuffle all characters in password_list
    random.SystemRandom().shuffle(password_list)

    password = ''.join(password_list)

    return password

def generate_strong_password():
    random_source = string.ascii_letters + string.digits + string.punctuation

    #1 lowercase
    password = random.choice(string.ascii_lowercase)

    #1 uppercase
    password += random.choice(string.ascii_uppercase)

    #1 number
    password += random.choice(string.digits)

    #1 symbol
    password += random.choice(string.punctuation)

    #generate other characters

    for i in range(11):
        password += random.choice(random_source)

    password_list = list(password)

    #shuffle all characters in password_list
    random.SystemRandom().shuffle(password_list)

    password = ''.join(password_list)

    return password

print("How strong do you want your password?")
print("Enter either 'strong' = 15 characters or 'medium' = 10 characters")

password_strength = input()

if password_strength == "medium":
    print("The medium generated password is:", generate_medium_password())

elif password_strength == "strong":
    print("The strong generated password is:", generate_strong_password())

else:
    print("Invalid input")





