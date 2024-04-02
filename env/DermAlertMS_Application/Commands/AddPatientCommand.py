from DermAlertMS_Application.Requests.PatientRequest import PatientRequest

class AddPatientCommands:
    
    def __init__(self,request : PatientRequest):
        self.requestAddPatient = request