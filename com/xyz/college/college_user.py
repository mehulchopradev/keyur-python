
# Super class / Parent class / Base class

# every class in python implicilty inherits from a built in class in python called as `object`
class CollegeUser(object):

    def __init__(self, name, gender):
        # self - Student object, Professor object, any sub class object reference
        self.name = name
        self.gender = gender

    def get_details(self):
        # self - Student object, Professor object, any sub class object reference
        # pass # if no return statement, python function returns a value None
        return 'Name: {0}\nGender: {1}'.format(self.name, self.gender)

    def __str__(self):
        return '{0}|{1}'.format(self.name, self.gender)