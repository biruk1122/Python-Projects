#Higest Score from List
student_scores = input("insert student scores\n").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score

print(f"The highest score in the class is: {highest_score}")
