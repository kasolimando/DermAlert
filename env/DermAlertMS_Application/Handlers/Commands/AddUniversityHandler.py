import itertools
from flask_injector import inject
from DermAlertMS_Core.Database.IDermAlertDBContext import IDermAlertDBContext
from DermAlertMS_Application.Commands.AddUniversityCommand import AddUniversityCommands
from DermAlertMS_Application.Mappers.UniversityMapper import *
from DermAlertMS_Application.Responses.Response import Response
from DermAlertMS_Infrastructure.Utils.HttpStatusCode import HttpStatusCode
from DermAlertMS_Application.Exceptions.CustomException import CustomException
from DermAlertMS_Application.Validations.UniversityValidation import ValidateData


class AddUniversityHandler:

    @inject
    def __init__(self, dermAlertDBContext: IDermAlertDBContext):
        self._dermAlertDBContext = dermAlertDBContext

    def Handle(self,request : AddUniversityCommands):
        try:
            if (request.requestAddUniversity is None):
                raise CustomException(['Solicitud Invalida'])
            else:
                newUniversity = MapRequestEntity(request.requestAddUniversity)
                ValidateData(self._dermAlertDBContext,newUniversity)
                self._dermAlertDBContext.save(newUniversity)
                return Response('Ha sido existosa la operación',HttpStatusCode['CREATED'],'',True,'')
        except CustomException as e:
            raise CustomException(list(itertools.chain(*e.errorMessage)))
        except Exception as e:
            raise CustomException(['Ha ocurrido un error por favor intente mas tarde handler',str(e)])
            
