from DermAlertMS_Core.Entities.University import University
from DermAlertMS_Application.Requests.UniversityRequest import UniversityRequest
import json
from datetime import date
from DermAlertMS_Application.Responses.UniversityResponse import UniversityReponses


def MapRequestEntity(request: UniversityRequest):
    return University(request.description, 
                      request.created_by,
                      request.updated_by)

    
def EntityToRequest(universities):
    result = []
    for university in universities:
        universityReponse = UniversityReponses(university)
        data =  json.loads(json.dumps(universityReponse.__dict__, ensure_ascii=False))
        result.append(data)
    return result

def EntityToNewEntity(newUniversity, oldUniversity):
    oldUniversity.description = newUniversity.description
    oldUniversity.updated_by = newUniversity.updated_by
    oldUniversity.updated_at = date.today()