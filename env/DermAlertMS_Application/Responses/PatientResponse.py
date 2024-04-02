from datetime import date

class PatientReponses:
    username = str
    name = str
    last_name = str
    phone = str
    birthdate = str
    iden_doc = str
    address = str
    sex = str
    status = str
    email = str


    def __init__(self, response):
        self.username = response.username
        self.name = response.name
        self.last_name = response.last_name
        self.phone = response.phone
        self.birthdate = response.birthdate.strftime('%Y-%m-%d')
        self.iden_doc = response.iden_doc
        self.address = response.address
        self.sex = response.sex
        self.status = response.status
        self.email = response.email

