from ast import List

class CustomException(Exception):
    def __init__(self, errorMessage: list):
        self.errorMessage = errorMessage
