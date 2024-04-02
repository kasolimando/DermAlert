from DermAlertMS_Application.Requests.DegreeRequest import DegreeRequest

class PutDegreeCommands:
    
    def __init__(self,request: DegreeRequest, id):
        self.requestPutDegree = request
        self.requestId = id