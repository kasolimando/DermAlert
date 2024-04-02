from datetime import date

class SurveyRequest():
    id = int 
    question =str
    value = int 
    created_at = date.today()
    updated_at = date.today()
    created_by = str
    updated_by = str 

    def __init__(self,request):
        self.question = request.json['question']
        self.value = int(request.json['value'])
        self.created_by = request.json['created_by']
        self.updated_by = request.json.get('updated_by',None)
        self.id = request.json.get('id',None)