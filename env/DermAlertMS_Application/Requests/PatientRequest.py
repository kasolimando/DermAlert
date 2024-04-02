from datetime import date, datetime

class PatientRequest():
    username = str
    name = str
    last_name = str
    phone = str
    birthdate = date
    iden_doc = str
    address = str
    sex = str
    status = str
    email = str
    password = str 
    created_at = date.today()
    updated_at = date.today()

    def __init__(self,request):
        self.username = request.json['username']
        self.name = request.json['name']
        self.last_name = request.json['last_name']
        self.phone = request.json['phone']
        self.birthdate = datetime.strptime(request.json['birthdate'], "%d/%m/%Y")
        self.iden_doc = request.json['iden_doc']
        self.address = request.json['address']
        self.sex = request.json['sex']
        self.status = request.json['status']
        self.email = request.json['email']
        self.status = request.json['status']
        self.password = request.json['password']
        self.created_at = date.today()
        self.updated_at = date.today()