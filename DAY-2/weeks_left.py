"""Write A Program using a maths and f-string that tells as how many weeks we have left if we have lived until 90
years old. """

age = input("Enter Your Age\n")
years = 90 - int(age)
weeks = years * 52
print(f"You Have {weeks} Left")
