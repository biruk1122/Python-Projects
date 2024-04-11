target = int(input("Enter a Number\n"))
total = 0
for number in range(2, target + 1, 2):
    total += number
print(total)