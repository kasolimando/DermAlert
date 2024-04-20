from datetime import date, datetime

class StatusRequest():
    username = str
    status = str
    updated_at = date

    def __init__(self,request):
        self.username = request.json['username']
        self.status = request.json['status']
        self.updated_at = date.today()