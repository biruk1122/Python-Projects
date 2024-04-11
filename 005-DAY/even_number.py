target = int(input("Enter a Number\n"))
other_number = 0
for number in range(1, target + 1):
    if number % 2 == 0:
        other_number += number
print(other_number)