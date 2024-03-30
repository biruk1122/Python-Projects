"""The Body Mass Index Program"""

height = input("Enter Your Height\n")
weight = input("Enter Your Weight\n")
weight_as_int = int(weight)
height_as_float = float(height)
bmi = weight_as_int / height_as_float ** 2
print(bmi)
