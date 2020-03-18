from .college_user import CollegeUser

class Professor(CollegeUser):
    def __init__(self, name, gender, subjects):
        # self - Professor object
        super().__init__(name, gender)
        # Internally
        # CollegeUser.__init__(self, name, gender)

        self.subjects = subjects