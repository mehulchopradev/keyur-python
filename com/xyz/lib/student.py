# Developer X
class Student:

    def __init__(self, name, roll, marks, gender):
        # Constructor

        # object attributes
        self.name = name
        self.roll = roll
        self.marks = marks
        self.gender = gender

    def get_details(self):
        # self - current object for which the "outside user" called this method
        ''' return 'Name : ' + self.name + '\nGender: ' + self.gender\
            + '\nRoll: ' + str(self.roll) + '\nMarks: ' + str(self.marks) '''

        ''' return 'Name: {0}\nGender: {1}\nRoll: {2}\nMarks: {3}'.format(self.name\
            , self.gender, self.roll, self.marks) '''

        return 'Name: {name}\nGender: {gender}\nRoll: {roll}\nMarks: {marks}'.format(\
            marks=self.marks, gender=self.gender, name=self.name, roll=self.roll)

    def get_grade(self):
        marks = self.marks
        if marks > 100 or marks < 0:
            grade = 'I'
        elif marks >= 70:
            grade = 'A'
        elif marks >= 60:
            grade = 'B'
        elif marks >= 40:
            grade = 'C'
        else:
            grade = 'F'

        return grade

    def get_name_roll(self):
        return (self.name, self.roll)