import itertools
from flask_injector import inject
from DermAlertMS_Core.Database.IDermAlertDBContext import IDermAlertDBContext
from DermAlertMS_Application.Commands.AddDegreeCommand import AddDegreeCommands
from DermAlertMS_Application.Mappers.DegreeMapper import *
from DermAlertMS_Application.Responses.Response import Response
from DermAlertMS_Infrastructure.Utils.HttpStatusCode import HttpStatusCode
from DermAlertMS_Application.Exceptions.CustomException import CustomException
from DermAlertMS_Application.Validations.DegreeValidation import ValidateData


class AddDegreeHandler:

    @inject
    def __init__(self, dermAlertDBContext: IDermAlertDBContext):
        self._dermAlertDBContext = dermAlertDBContext

    def Handle(self,request : AddDegreeCommands):
        try:
            if (request.requestAddDegree is None):
                raise CustomException(['Solicitud Invalida'])
            else:
                newDegree = MapRequestEntity(request.requestAddDegree)
                ValidateData(self._dermAlertDBContext,newDegree)
                self._dermAlertDBContext.save(newDegree)
                return Response('Ha sido existosa la operación',HttpStatusCode['CREATED'],'',True,'')
        except CustomException as e:
            raise CustomException(list(e.errorMessage))
        except Exception as e:
            raise CustomException(['Ha ocurrido un error por favor intente mas tarde handler',str(e)])
            
