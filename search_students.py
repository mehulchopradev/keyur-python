from com.xyz.lib.student import Student

''' slist = [
    Student(name='mehul', roll=10, marks=90, gender='m'),
    Student(name='jane', roll=5, marks=67, gender='f'),
    Student(name='jill', roll=23, marks=78, gender='f'),
    Student(name='keyur', roll=26, marks=56, gender='m')
]

q = int(input('Enter roll to search: '))

for student in slist:
    if student.roll == q:
        print(student.get_details())
        break
else:
    # Will execute when the corresponding for loop is exhausted
    # i.e. no break statement has beeen encountered in the for loop
    print('Student not found') '''

smap = {
    10: Student(name='mehul', roll=10, marks=90, gender='m'),
    5: Student(name='jane', roll=5, marks=67, gender='f'),
    23: Student(name='jill', roll=23, marks=78, gender='f'),
    26: Student(name='keyur', roll=26, marks=56, gender='m')
}

q = int(input('Enter roll to search: '))
if q in smap:
    student = smap[q]
    print(student.get_details())
else:
    print('Student not found')
