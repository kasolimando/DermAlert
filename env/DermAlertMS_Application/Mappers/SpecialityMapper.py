from DermAlertMS_Core.Entities.Speciality import Speciality
from DermAlertMS_Application.Requests.SpecialityRequest import SpecialityRequest
import json
from datetime import date
from DermAlertMS_Application.Responses.SpecialityResponse import SpecialityReponses


def MapRequestEntity(request: SpecialityRequest):
    return Speciality(request.description, 
                      request.created_by,
                      request.updated_by)

    
def EntityToRequest(specialities):
    result = []
    for speciality in specialities:
        specialityReponse = SpecialityReponses(speciality)
        data =  json.loads(json.dumps(specialityReponse.__dict__, ensure_ascii=False))
        result.append(data)
    return result

def EntityToNewEntity(newSpeciality, oldSpeciality):
    oldSpeciality.description = newSpeciality.description
    oldSpeciality.updated_by = newSpeciality.updated_by
    oldSpeciality.updated_at = date.today()