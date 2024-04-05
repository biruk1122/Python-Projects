"""Create a Password Generator Program"""

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L','M', 'N',
'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Python Password Generator!")
number_of_letters = int(input("How Many Letters Would You Like in Your Password?\n"))
number_of_symbols = int(input(f"How Many Symbols Would You Like?\n"))
number_of_numbers = int(input(f"How Many Numbers Would You Like?\n"))

# Easy Level

password = " "

for char in range(1, number_of_letters + 1):
    password += random.choice(letters)

for char in range(1, number_of_symbols + 1):
    password += random.choice(symbols)

for char in range(1, number_of_numbers + 1):
    password += random.choice(numbers)

print(password)


# Hard Level
password_list = []

for char in range(1, number_of_letters + 1):
    password_list.append(random.choice(letters))

for char in range(1, number_of_symbols + 1):
    password_list += random.choice(symbols)

for char in range(1, number_of_numbers + 1):
    password_list += random.choice(numbers)

random.shuffle(password_list)

# To Change the Password to a String
password = ""
for char in password_list:
    password += char

print(f"Your Password is: {password}")
