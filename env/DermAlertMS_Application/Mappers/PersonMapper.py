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

def EntityToNewEntityPerson(newPerson, oldPerson):
    oldPerson.username = newPerson.username
    oldPerson.name  = newPerson.name
    oldPerson.last_name  = newPerson.last_name
    oldPerson.phone  = newPerson.phone
    oldPerson.birthdate  = newPerson.birthdate
    oldPerson.iden_doc  = newPerson.iden_doc
    oldPerson.address  = newPerson.address
    oldPerson.sex  = newPerson.sex
    oldPerson.updated_at  = date.today()