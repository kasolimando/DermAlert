from flask_injector import inject
from DermAlertMS_Core.Database.IDermAlertDBContext import IDermAlertDBContext
from DermAlertMS_Application.Commands.DeleteUniversityCommand import DeleteUniversityCommands
from DermAlertMS_Application.Mappers.UniversityMapper import *
from DermAlertMS_Application.Responses.Response import Response
from DermAlertMS_Infrastructure.Utils.HttpStatusCode import HttpStatusCode
from DermAlertMS_Application.Exceptions.CustomException import CustomException
from DermAlertMS_Application.Validations.UniversityValidation import *


class DeleteUniversityHandler:

    @inject
    def __init__(self, dermAlertDBContext: IDermAlertDBContext):
        self._dermAlertDBContext = dermAlertDBContext

    def Handle(self,request : DeleteUniversityCommands):
        try:
            if (request.requestDeleteUniversity is None):
                raise CustomException(['Solicitud Invalida'])
            else:
                university = ValidateDelete(self._dermAlertDBContext,request.requestDeleteUniversity)
                self._dermAlertDBContext.delete(university)
                return Response('Ha sido exitosa la operacion',HttpStatusCode['NO CONTENT'],'',True,'')
        except CustomException as e:
            raise CustomException(e.errorMessage)
        except Exception as e:
            raise CustomException(['Ha ocurrido un error por favor intente mas tarde handler',e])
            
