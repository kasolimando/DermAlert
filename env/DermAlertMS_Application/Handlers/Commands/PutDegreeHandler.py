import itertools
from flask_injector import inject
from DermAlertMS_Core.Database.IDermAlertDBContext import IDermAlertDBContext
from DermAlertMS_Application.Commands.PutDegreeCommand import PutDegreeCommands
from DermAlertMS_Application.Mappers.DegreeMapper import *
from DermAlertMS_Application.Responses.Response import Response
from DermAlertMS_Infrastructure.Utils.HttpStatusCode import HttpStatusCode
from DermAlertMS_Application.Exceptions.CustomException import CustomException
from DermAlertMS_Application.Validations.DegreeValidation import *


class PutDegreeHandler:

    @inject
    def __init__(self, dermAlertDBContext: IDermAlertDBContext):
        self._dermAlertDBContext = dermAlertDBContext

    def Handle(self,request : PutDegreeCommands):
        try:
            if (request.requestPutDegree is None or request.requestId is None):
                raise CustomException(['Solicitud Invalida'])
            else:
                newDegree = MapRequestEntity(request.requestPutDegree)
                oldDegree = ValidateDegree(self._dermAlertDBContext,request.requestId)
                ValidatePut(newDegree)
                EntityToNewEntity(newDegree,oldDegree)
                self._dermAlertDBContext.Commit()
                return Response('La operación ha sido exitosa',HttpStatusCode['OK'],'',True,'')
        except CustomException as e:
            raise CustomException(list(itertools.chain(*e.errorMessage)))
        except Exception as e:
            raise CustomException(['Ha ocurrido un error por favor intente mas tarde handler',str(e)])
            
