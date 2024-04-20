from DermAlertMS_Application.Requests.PatientRequest import PatientRequest

class PutPatientCommands:
    
    def __init__(self,request: PatientRequest, username):
        self.requestPutPatient = request
        self.requestUsername = username