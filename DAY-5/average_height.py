student_height = input("Insert Student Heights\n ").split()
for n in range(0, len(student_height)):
    student_height[n] = int(student_height[n])
total_height = 0
for height in student_height:
    total_height += height
print(f"Total Height = {total_height}")

# Number of Students
number_of_students = 0
for students in student_height:
    number_of_students += 1
print(f"Number of Students = {number_of_students}")

# Average Height
average_height = round(total_height / number_of_students)
print(f"Average Height = {average_height}")
