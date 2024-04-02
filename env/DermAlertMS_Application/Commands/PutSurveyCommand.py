from DermAlertMS_Application.Requests.SurveyRequest import SurveyRequest

class PutSurveyCommands:
    
    def __init__(self,request: SurveyRequest, id):
        self.requestPutSurvey = request
        self.requestId = id