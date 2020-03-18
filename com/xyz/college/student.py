from .college_user import CollegeUser

# sub class / Child class / concrete class
class Student(CollegeUser):
    def __init__(self, name, gender, roll):
        # self - Student object
        super().__init__(name, gender)
        # Internally
        # CollegeUser.__init__(self, name, gender)

        self.roll = roll

    # override the method
    # overriden method is called in place of the inherited method
    def get_details(self):
        # self will be Student object
        part1 = super().get_details()
        # Internally
        # CollegeUser.get_details(self)

        part2 = '\nRoll: {0}'.format(self.roll)

        return part1 + part2
