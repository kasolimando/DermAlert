import itertools
from flask_injector import inject
from DermAlertMS_Core.Database.IDermAlertDBContext import IDermAlertDBContext
from DermAlertMS_Application.Commands.PatchStatusCommand import PatchStatusCommand
from DermAlertMS_Application.Mappers.StatusMapper import *
from DermAlertMS_Application.Responses.Response import Response
from DermAlertMS_Infrastructure.Utils.HttpStatusCode import HttpStatusCode
from DermAlertMS_Application.Exceptions.CustomException import CustomException
from DermAlertMS_Application.Validations.UserValidation import *


class PatchStatusHandler:

    @inject
    def __init__(self, dermAlertDBContext: IDermAlertDBContext):
        self._dermAlertDBContext = dermAlertDBContext

    def Handle(self,request : PatchStatusCommand):
        try:
            if (request.requestPatchStatus is None or request.requestUsername is None):
                raise CustomException(['Solicitud Invalida'])
            else:
                oldPerson = ValidateData(self._dermAlertDBContext,request.requestUsername)
                StatusEntityToNewEntity(request.requestPatchStatus,oldPerson)
                self._dermAlertDBContext.Commit()
                return Response('La operación ha sido existosa',HttpStatusCode['CREATED'],'',True,'')
        except CustomException as e:
            raise CustomException(list(e.errorMessage))
        except Exception as e:
            raise CustomException(['Ha ocurrido un error por favor intente mas tarde handler',str(e)])
            
