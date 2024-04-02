from flask_injector import inject
from DermAlertMS_Core.Database.IDermAlertDBContext import IDermAlertDBContext
from DermAlertMS_Application.Commands.DeleteSpecialityCommand import DeleteSpecialityCommands
from DermAlertMS_Application.Mappers.SpecialityMapper import *
from DermAlertMS_Application.Responses.Response import Response
from DermAlertMS_Infrastructure.Utils.HttpStatusCode import HttpStatusCode
from DermAlertMS_Application.Exceptions.CustomException import CustomException
from DermAlertMS_Application.Validations.SpecialityValidation import *


class DeleteSpecialityHandler:

    @inject
    def __init__(self, dermAlertDBContext: IDermAlertDBContext):
        self._dermAlertDBContext = dermAlertDBContext

    def Handle(self,request : DeleteSpecialityCommands):
        try:
            if (request.requestDeleteSpeciality is None):
                raise CustomException(['Solicitud Invalida'])
            else:
                speciality = ValidateDelete(self._dermAlertDBContext,request.requestDeleteSpeciality)
                self._dermAlertDBContext.delete(speciality)
                return Response('Ha sido exitosa la operacion',HttpStatusCode['NO CONTENT'],'',True,[])
        except CustomException as e:
            raise CustomException(e.errorMessage)
        except Exception as e:
            raise CustomException(['Ha ocurrido un error por favor intente mas tarde handler',e])
            
