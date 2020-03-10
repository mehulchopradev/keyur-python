from com.xyz.lib.student import Student

s1 = Student() # 3004 (RAM)
s1.name = 'mehul chopra'
s1.roll = 10
s1.marks = 90.45
s1.gender = 'm'


s2 = Student() # 3006 (RAM)
s2.name = 'jane'
s2.roll = 12
s2.marks = 78
s2.gender = 'f'

# print(s1)
# print(s2)

''' print(s1.name)
print(s1.roll)

print(s2.name)
print(s2.roll) '''

print(s1.get_details())
print(s2.get_details())