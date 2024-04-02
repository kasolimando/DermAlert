class SpecialityReponses:
    id = int
    description = str


    def __init__(self, response):
        self.description = response.description
        self.id = response.id

