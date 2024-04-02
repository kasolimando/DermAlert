import itertools
from flask_injector import inject
from DermAlertMS_Core.Database.IDermAlertDBContext import IDermAlertDBContext
from DermAlertMS_Application.Commands.AddSurveyCommand import AddSurveyCommands
from DermAlertMS_Application.Mappers.SurveyMapper import *
from DermAlertMS_Application.Responses.Response import Response
from DermAlertMS_Infrastructure.Utils.HttpStatusCode import HttpStatusCode
from DermAlertMS_Application.Exceptions.CustomException import CustomException
from DermAlertMS_Application.Validations.SurveyValidation import ValidateData


class AddSurveyHandler:

    @inject
    def __init__(self, dermAlertDBContext: IDermAlertDBContext):
        self._dermAlertDBContext = dermAlertDBContext

    def Handle(self,request : AddSurveyCommands):
        try:
            if (request.requestAddSurvey is None):
                raise CustomException(['Solicitud Invalida'])
            else:
                newSurvey = MapRequestEntity(request.requestAddSurvey)
                ValidateData(self._dermAlertDBContext,newSurvey)
                self._dermAlertDBContext.save(newSurvey)
                return Response('Ha sido existosa la operación',HttpStatusCode['CREATED'],'',True,'')
        except CustomException as e:
            raise CustomException(list(itertools.chain(*e.errorMessage)))
        except Exception as e:
            raise CustomException(['Ha ocurrido un error por favor intente mas tarde handler',str(e)])
            
