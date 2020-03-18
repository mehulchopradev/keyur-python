# User defined exception class

class MinBalError(Exception):

    def __init__(self, message):
        super().__init__(message)