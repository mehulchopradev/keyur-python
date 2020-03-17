# Developer Y

from com.xyz.lib.student import Student

print(Student.count) # 0 (Accessing the class attribute)

# s1 = Student() # 3004 (RAM)
'''
Internally
1. Reserve memory in the RAM for the Student object (3004)
2. Student.__init__(3004)
'''

''' s1.name = 'mehul chopra'
s1.roll = 10
s1.marks = 90.45
s1.gender = 'm' '''

s1 = Student('mehul chopra', 10, 90.45, 'm')
'''
Internally
1. Reserve memory in the RAM for the Student object (3004)
2. Student.__init__(3004, 'mehul chopra', 10, 90.45, 'm')
'''


s2 = Student('jane', 12, 45, 'f') # 3006 (RAM)
''' s2.name = 'jane'
s2.roll = 12
s2.marks = 45
s2.gender = 'f' '''

# print(s1)
# print(s2)

''' print(s1.name)
print(s1.roll)

print(s2.name)
print(s2.roll) '''

print(Student.count) # 2

print(s1.get_details())
# Python Internally
# print(Student.get_details(s1))

print(s2.get_details())
# Internally
# print(Student.get_details(s2))

print(s1.get_grade())
# Internally
# print(Student.get_grade(s1))

print(s2.get_grade())
# Internally
# print(Student.get_grade(s2))

s3 = Student('jill', 15, 34, 'f') # 3009 (RAM)
''' s3.s_name = 'jill'
s3.r = 15
s3.marks = 34
s3.gen = 'f' '''

print(s3.get_details())

''' t = s1.get_name_roll()
name = t[0]
roll = t[1] '''

name, roll = s1.get_name_roll() # tuple unpacking (even works for list)
print(name)
print(roll)
# Internally
# Student.get_name_roll(s1)

print(Student.count) # 3

# calling a class method
s4 = Student.create_student(name='keyur', gender='m', roll=90, marks=98)
print(s4.get_details())