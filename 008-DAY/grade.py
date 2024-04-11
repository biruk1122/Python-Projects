"""Grading Program"""

student_scores = {
    "Lawira": 83,
    "David": 79,
    "Mikel": 74,
    "Mayer": 98,
    "Bacho": 65
}

# Create an Empty Dictionary
student_grade = {}

# Convert Student Scores to Grades
for student in student_scores:
    scores = student_scores[student]
    if scores > 90:
        student_grade[student] = "Outstanding"
    elif scores > 80:
        student_grade[student] = "Exceeds Expectations"
    elif scores > 70:
        student_grade[student] = "Acceptable"
    else:
        student_grade[student] = "Fail"
print(student_grade)
