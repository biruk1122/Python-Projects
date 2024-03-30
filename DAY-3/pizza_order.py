"""Pizza Delivery"""

print("Thank You for Choosing Pizza Deliveries")
size = input("What Size Pizza Do You Want? S, M, or L ")
if size == "S":
    bill = 12
    print("Small Pizza is $15 ")
if size == "M":
    bill = 20
    print("Your Medium Pizza is $20 ")
if size == "L":
    bill = 25
    print("Your Large Pizza is $25 ")
add_pepperoni = input("Do You Want Pepperoni? Y or N ")
if add_pepperoni == "Y":
    bill += 2
    print(f"Your Bill is ${bill}")
extra_cheese = input("Do You Want Extra Cheese? Y or N ")
if extra_cheese == "Y":
    bill += 3
    print((f"Your Bill is ${bill}"))
