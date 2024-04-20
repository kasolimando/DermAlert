from DermAlertMS_Application.Requests.StatusRequest import StatusRequest

class PatchStatusCommand:
    
    def __init__(self,request: StatusRequest, username):
        self.requestPatchStatus = request
        self.requestUsername = username