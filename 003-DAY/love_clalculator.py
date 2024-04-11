print("The Love Calculator is Calculating Your Score...")
name1 = input("What is Your Name? ")
name2 = input("What is Her or His Name? ")

combined_names = name1 + name2
# This line checks the name is lower case letters
lower_names = combined_names.lower()
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))
if score < 10 or score > 90:
    print(f"Your Score is {score}, you together like Coke and Mentos.")
elif (score >= 40) and (score <= 50):
    print(f"Your Score is {score}, You are Alright Together.")
else:
    print(f"Your Score is {score}.")
    