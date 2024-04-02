from datetime import date

class DegreeRequest():
    id = int 
    description =str
    created_at = date.today()
    updated_at = date.today()
    created_by = str
    updated_by = str 

    def __init__(self,request):
        self.description = request.json['description']
        self.created_by = request.json['created_by']
        self.updated_by = request.json.get('updated_by',None)
        self.id = request.json.get('id',None)