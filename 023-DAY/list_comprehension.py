# numbers
number = [1, 2, 3, 4, 5]
new_number = [n + 1 for n in number]

# Strings
name = "Biruk"
letter_list = [letter for letter in name]

# Ranges
range_list = [num * 2 for num in range(1, 5)]

# Conditional List Comprehension
names = ["Alex", "Kurdacha", "Ermis", "Denis", "Devon", "Bura"]
short_names = [name for name in names if len(name) < 5]
long_names = [name.upper() for name in names if len(name) > 5]
