"""If the bill was $150.00 Split between 5 People with 12% tip. Each Person Should pay (150 / 5) * 1.12 = 33.6
Round the result to 2 Decimal place = 33.60"""

print("Welcome to the Tip Calculator")
bill = float(input("What was the Total Bill? $"))
tip = int(input("How Much tip Would you Like to Give? 10, 12, 0r 15? "))
people = int(input("How Many People to Split the Bill?"))
bill_with_tip = tip / 100 * bill + bill
bill_per_person = bill_with_tip / people
result = "{:.2f}".format(bill_per_person)
print(f"Each Person Should Pay ${result}")