class SurveyResponses:
    id = int
    question = str
    value = int


    def __init__(self, response):
        self.question = response.question
        self.value = response.value
        self.id = response.id

