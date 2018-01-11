
class User:
    def __init__(self, question1_array, question2_array, question3_array):
        self.question1_array = question1_array
        self.question2_array = question2_array
        self.question3_array = question3_array

    def get_question1(self):
        return self.question1_array

    def get_question2(self):
        return self.question2_array

    def get_question3(self):
        return self.question3_array
