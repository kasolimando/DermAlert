from DermAlertMS_Core.Entities.Person import Person
from DermAlertMS_Application.Requests.PatientRequest import PatientRequest
import json
from datetime import date


def MapRequestEntityPerson(request: PatientRequest):
    return Person(request.username, 
                      request.name,
                      request.last_name,
                      request.phone,
                      request.birthdate,
                      request.iden_doc,
                      request.address,
                      request.sex,
                      request.status,
                      request.email,
                      request.password,
                      request.created_at,
                      request.updated_at)
