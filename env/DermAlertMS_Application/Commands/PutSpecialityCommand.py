from DermAlertMS_Application.Requests.SpecialityRequest import SpecialityRequest

class PutSpecialityCommands:
    
    def __init__(self,request: SpecialityRequest, id):
        self.requestPutSpeciality = request
        self.requestId = id