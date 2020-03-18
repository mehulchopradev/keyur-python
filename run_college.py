from com.xyz.college.student import Student
from com.xyz.college.professor import Professor

i = 10
s = Student('keyur', 'm', 10)
p = Professor('mehul', 'm', ['Physics', 'Maths'])

''' print(s.name)
print(s.roll)

print(p.name)
print(p.subjects) '''

print(i)
# Internally
# print(i.__str__())
# print(int.__str__(i))

print(s)
# Internally
# print(s.__str__())
# print(Student.__str__(s))
# print(CollegeUser.__str__(s))
# print(object.__str__(s))

print(p)

# print(s.get_details())

# Internally
# Student.get_details(s)
# CollegeUser.get_details(s)


# print(p.get_details())

# Internally
# Professor.get_details(p)
# CollegeUser.get_details(p)