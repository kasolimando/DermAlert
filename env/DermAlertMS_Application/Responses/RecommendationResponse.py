class RecommendationResponses:
    id = int
    description = str
    entry_value = int
    end_value = int


    def __init__(self, response):
        self.description = response.description
        self.entry_value = response.entry_value
        self.end_value = response.end_value
        self.id = response.id

