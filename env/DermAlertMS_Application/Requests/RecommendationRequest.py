from datetime import date

class RecommendationRequest():
    id = int 
    description =str
    entry_value = int 
    end_value = int 
    created_at = date.today()
    updated_at = date.today()
    created_by = str
    updated_by = str 

    def __init__(self,request):
        self.description = request.json['description']
        self.entry_value = int(request.json['entry_value'])
        self.end_value = int(request.json['end_value'])
        self.created_by = request.json['created_by']
        self.updated_by = request.json.get('updated_by',None)
        self.id = request.json.get('id',None)