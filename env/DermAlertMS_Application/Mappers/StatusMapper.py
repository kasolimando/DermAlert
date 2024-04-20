from DermAlertMS_Core.Entities.Person import Person
from DermAlertMS_Application.Requests.StatusRequest import StatusRequest
import json
from datetime import date


def MapRequestEntityPerson(request: StatusRequest):
    return Person(request.username, 
                  request.status,
                  request.updated_at)


def StatusEntityToNewEntity(newPerson, oldPerson):
    oldPerson.status = newPerson.status
    oldPerson.updated_at = newPerson.updated_at
