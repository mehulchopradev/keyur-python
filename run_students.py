from com.xyz.lib.student_ops import get_details, get_grade

name = 'Mehul'
roll = 10
gender = 'm'
marks = 78

print(get_details(name=name, roll=roll, gender=gender, marks=marks))
print(get_grade(marks=marks))