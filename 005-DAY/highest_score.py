"""Highest Score From the List"""

student_scores = input("Insert Student Scores\n").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
highest_score = 0
for score in student_scores:
    if score > highest_score:
        if score > highest_score:
            highest_score = score
print(f"Highest Score in the Class is: {highest_score}")
