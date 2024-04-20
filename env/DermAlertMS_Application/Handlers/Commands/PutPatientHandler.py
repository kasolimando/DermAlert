import itertools
from flask_injector import inject
from DermAlertMS_Core.Database.IDermAlertDBContext import IDermAlertDBContext
from DermAlertMS_Application.Commands.PutPatientCommand import PutPatientCommands
from DermAlertMS_Application.Mappers.PatientMapper import *
from DermAlertMS_Application.Mappers.PersonMapper import *
from DermAlertMS_Application.Responses.Response import Response
from DermAlertMS_Infrastructure.Utils.HttpStatusCode import HttpStatusCode
from DermAlertMS_Application.Exceptions.CustomException import CustomException
from DermAlertMS_Application.Validations.PatientValidation import ValidatePatient,ValidatePut
from DermAlertMS_Application.Validations.UserValidation import ValidateData


class PutPatientHandler:

    @inject
    def __init__(self, dermAlertDBContext: IDermAlertDBContext):
        self._dermAlertDBContext = dermAlertDBContext

    def Handle(self,request : PutPatientCommands):
        try:
            if (request.requestPutPatient is None or request.requestUsername is None):
                raise CustomException(['Solicitud Invalida'])
            else:
                newPatient = MapRequestEntity(request.requestPutPatient)
                newPerson = MapRequestEntityPerson(request.requestPutPatient)
                oldPatient = ValidatePatient(self._dermAlertDBContext,request.requestUsername)
                oldPerson = ValidateData(self._dermAlertDBContext,request.requestUsername)
                ValidatePut(newPerson)
                EntityToNewEntity(newPatient,oldPatient)
                EntityToNewEntityPerson(newPerson,oldPerson)
                self._dermAlertDBContext.Commit()
                return Response('La operación ha sido exitosa',HttpStatusCode['OK'],'',True,'')
        except CustomException as e:
            raise CustomException(list(itertools.chain(*e.errorMessage)))
        except Exception as e:
            raise CustomException(['Ha ocurrido un error por favor intente mas tarde handler',str(e)])
            
