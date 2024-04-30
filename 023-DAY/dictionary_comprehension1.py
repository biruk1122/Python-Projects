import pandas

student_dic = {
    "student": ["Bryan", "James", "July"],
    "score": [70, 73, 87]
}

student_data_frame = pandas.DataFrame(student_dic)
print(student_data_frame)
