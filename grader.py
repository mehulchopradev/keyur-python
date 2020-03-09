marks = float(input('Enter marks: '))

# if - elif - elif - * - else (selection statement) for more than 2 branches
if marks > 100 or marks < 0:
    print('I')
elif marks >= 70:
    print('A')
elif marks >= 60:
    print('B')
elif marks >= 40:
    print('C')
else:
    print('F')