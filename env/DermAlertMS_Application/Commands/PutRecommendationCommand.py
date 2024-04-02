from DermAlertMS_Application.Requests.RecommendationRequest import RecommendationRequest

class PutRecommendationCommands:
    
    def __init__(self,request: RecommendationRequest, id):
        self.requestPutRecommendation = request
        self.requestId = id