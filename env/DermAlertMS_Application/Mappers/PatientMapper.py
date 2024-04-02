from DermAlertMS_Core.Entities.Patient import Patient
from DermAlertMS_Application.Requests.PatientRequest import PatientRequest
import json
from datetime import date
from DermAlertMS_Application.Responses.PatientResponse import PatientReponses
from sqlalchemy import inspect


def MapRequestEntity(request: PatientRequest):
    return Patient(request.username, 
                      request.created_at,
                      request.updated_at)

    
def EntityToRequest(patients):
    result = []
    for person, patient in patients:
        patientReponse = PatientReponses(person)
        data =  json.loads(json.dumps(patientReponse.__dict__, ensure_ascii=False))
        result.append(data)
    return result

def EntityToNewEntity(newPatient, oldPatient):
    oldPatient.username = newPatient.username
    oldPatient.updated_at = date.today()