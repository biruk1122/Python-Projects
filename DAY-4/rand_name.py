"""Writing a Program that Will Select a Random Name From the List"""

import random
names_string = "Biruk, Fikadu, Ben, Tony, Stark, Jhony, Filipho"
names = names_string.split(", ")

# Get the Total Number of Items in the List
num_items = len(names)

# Generate Random Numbers Between 0 and the Last Index.
random_choice = random.randint(0, num_items - 1)

# Pick Out Random Person From List of Names Using the Random Number.
person_who_will_pay = names[random_choice]
print(person_who_will_pay + " is Going to Buy the Meal Today!")