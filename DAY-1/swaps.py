"""This Program writes to swaps a value  stored in the variable a and b"""

a = input("Enter Value 'a': ")
b = input("Enter Value 'b': ")
print("before swapping: ")
print("a =", a)
print("b = ", b)

# Swap the value using temporary variable

temp = a
a = b
b = temp
# Print the value after swapping

print("\nAfter Swapping: ")
print("a =", a)
print("b =", b)