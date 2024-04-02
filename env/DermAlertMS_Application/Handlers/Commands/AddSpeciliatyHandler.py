import itertools
from flask_injector import inject
from DermAlertMS_Core.Database.IDermAlertDBContext import IDermAlertDBContext
from DermAlertMS_Application.Commands.AddSpecialityCommand import AddSpecialityCommands
from DermAlertMS_Application.Mappers.SpecialityMapper import *
from DermAlertMS_Application.Responses.Response import Response
from DermAlertMS_Infrastructure.Utils.HttpStatusCode import HttpStatusCode
from DermAlertMS_Application.Exceptions.CustomException import CustomException
from DermAlertMS_Application.Validations.SpecialityValidation import ValidateData


class AddSpecialityHandler:

    @inject
    def __init__(self, dermAlertDBContext: IDermAlertDBContext):
        self._dermAlertDBContext = dermAlertDBContext

    def Handle(self,request : AddSpecialityCommands):
        try:
            if (request.requestAddSpeciality is None):

                newSpeciality = MapRequestEntity(request.requestAddSpeciality)
                ValidateData(self._dermAlertDBContext,newSpeciality)
                self._dermAlertDBContext.save(newSpeciality)
                return Response('Ha sido existosa la operación',HttpStatusCode['CREATED'],'',True,'')
        except CustomException as e:
            raise CustomException(list(e.errorMessage))
        except Exception as e:
            raise CustomException(['Ha ocurrido un error por favor intente mas tarde handler',str(e)])
            
