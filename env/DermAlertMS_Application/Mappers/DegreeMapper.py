from DermAlertMS_Core.Entities.Degree import Degree
from DermAlertMS_Application.Requests.DegreeRequest import DegreeRequest
import json
from datetime import date
from DermAlertMS_Application.Responses.DegreeResponse import DegreeReponses


def MapRequestEntity(request: DegreeRequest):
    return Degree(request.description, 
                      request.created_by,
                      request.updated_by)

    
def EntityToRequest(degrees):
    result = []
    for degree in degrees:
        degreeReponse = DegreeReponses(degree)
        data =  json.loads(json.dumps(degreeReponse.__dict__, ensure_ascii=False))
        result.append(data)
    return result

def EntityToNewEntity(newDegree, oldDegree):
    oldDegree.description = newDegree.description
    oldDegree.updated_by = newDegree.updated_by
    oldDegree.updated_at = date.today()