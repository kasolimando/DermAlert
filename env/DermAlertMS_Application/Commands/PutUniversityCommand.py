from DermAlertMS_Application.Requests.UniversityRequest import UniversityRequest

class PutUniversityCommands:
    
    def __init__(self,request: UniversityRequest, id):
        self.requestPutUniversity = request
        self.requestId = id