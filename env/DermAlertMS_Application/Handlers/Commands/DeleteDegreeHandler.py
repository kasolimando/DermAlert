from flask_injector import inject
from DermAlertMS_Core.Database.IDermAlertDBContext import IDermAlertDBContext
from DermAlertMS_Application.Commands.DeleteDegreeCommand import DeleteDegreeCommands
from DermAlertMS_Application.Mappers.DegreeMapper import *
from DermAlertMS_Application.Responses.Response import Response
from DermAlertMS_Infrastructure.Utils.HttpStatusCode import HttpStatusCode
from DermAlertMS_Application.Exceptions.CustomException import CustomException
from DermAlertMS_Application.Validations.DegreeValidation import *


class DeleteDegreeHandler:

    @inject
    def __init__(self, dermAlertDBContext: IDermAlertDBContext):
        self._dermAlertDBContext = dermAlertDBContext

    def Handle(self,request : DeleteDegreeCommands):
        try:
            if (request.requestDeleteDegree is None):
                raise CustomException(['Solicitud Invalida'])
            else:
                degree = ValidateDelete(self._dermAlertDBContext,request.requestDeleteDegree)
                self._dermAlertDBContext.delete(degree)
                return Response('Ha sido exitosa la operacion',HttpStatusCode['NO CONTENT'],'',True,'')
        except CustomException as e:
            raise CustomException(e.errorMessage)
        except Exception as e:
            raise CustomException(['Ha ocurrido un error por favor intente mas tarde handler',e])
            
