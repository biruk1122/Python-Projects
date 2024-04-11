"""Multiple if Statments"""

print("Welcome to The Rollercoaster!")
height = int(input("What is Your Height in cm? "))

if height >= 120:
    bill = 0
    print("You Can Ride The Rollercoaster!")
    age = int(input("What is Your Age? "))
    if age < 12:
        bill = 5
        print("Child Tickets are $5. ")
    elif age <= 18:
        bill = 7
        print("Youth Tickets Are $7 ")
    elif age <= 45 and age <= 55:
        print("Everything is Going to be Ok. Have a Free Ride On Us")
    else:
        bill = 12
        print("Adult Tickets Are $12. ")

    add_photo = input("Do You Want A Photo Taken? Y or N ")
    if add_photo == "Y":
        bill += 3
        print(f"Your Final Bill is ${bill}")
    else:
        print("Sorry You Have To Grow Taller Before You Can Ride. ")
