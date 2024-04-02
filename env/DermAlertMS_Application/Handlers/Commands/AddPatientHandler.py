import itertools
from flask_injector import inject
from DermAlertMS_Core.Database.IDermAlertDBContext import IDermAlertDBContext
from DermAlertMS_Application.Commands.AddPatientCommand import AddPatientCommands
from DermAlertMS_Application.Mappers.PatientMapper import *
from DermAlertMS_Application.Mappers.PersonMapper import *
from DermAlertMS_Application.Responses.Response import Response
from DermAlertMS_Infrastructure.Utils.HttpStatusCode import HttpStatusCode
from DermAlertMS_Application.Exceptions.CustomException import CustomException
from DermAlertMS_Application.Validations.PatientValidation import ValidateData


class AddPatientHandler:

    @inject
    def __init__(self, dermAlertDBContext: IDermAlertDBContext):
        self._dermAlertDBContext = dermAlertDBContext

    def Handle(self,request : AddPatientCommands):
        try:
            if (request.requestAddPatient is None):
                raise CustomException(['Solicitud Invalida'])
            else:
                newPatient = MapRequestEntity(request.requestAddPatient)
                newPerson = MapRequestEntityPerson(request.requestAddPatient)
                ValidateData(self._dermAlertDBContext,newPerson)
                self._dermAlertDBContext.save(newPerson)
                self._dermAlertDBContext.save(newPatient)
                return Response('La operación ha sido existosa',HttpStatusCode['CREATED'],'',True,'')
        except CustomException as e:
            raise CustomException(list(e.errorMessage))
        except Exception as e:
            raise CustomException(['Ha ocurrido un error por favor intente mas tarde handler',str(e)])
            
