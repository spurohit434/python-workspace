students_data = open('csv_data.txt', 'r')
students = students_data.readlines()
students_data.close()
students = [line.strip() for line in students[1:]]
print(students)

for student in students:
    student = student.split(',')
    name = student[0]
    age = student[1]
    dept = student[2]
    university = student[3]
    print(f'{name.title()} is {age}, studying in {dept} in {university}')
