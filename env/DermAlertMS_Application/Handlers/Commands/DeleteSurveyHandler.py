from flask_injector import inject
from DermAlertMS_Core.Database.IDermAlertDBContext import IDermAlertDBContext
from DermAlertMS_Application.Commands.DeleteSurveyCommand import DeleteSurveyCommands
from DermAlertMS_Application.Mappers.SurveyMapper import *
from DermAlertMS_Application.Responses.Response import Response
from DermAlertMS_Infrastructure.Utils.HttpStatusCode import HttpStatusCode
from DermAlertMS_Application.Exceptions.CustomException import CustomException
from DermAlertMS_Application.Validations.SurveyValidation import ValidateDelete


class DeleteSurveyHandler:

    @inject
    def __init__(self, dermAlertDBContext: IDermAlertDBContext):
        self._dermAlertDBContext = dermAlertDBContext

    def Handle(self,request : DeleteSurveyCommands):
        try:
            if (request.requestDeleteSurvey is None):
                raise CustomException(['Solicitud Invalida'])
            else:
                survey = ValidateDelete(self._dermAlertDBContext,request.requestDeleteSurvey)
                self._dermAlertDBContext.delete(survey)
                return Response('Ha sido exitosa la operacion',HttpStatusCode['NO CONTENT'],'',True,'')
        except CustomException as e:
            raise CustomException(e.errorMessage)
        except Exception as e:
            raise CustomException(['Ha ocurrido un error por favor intente mas tarde handler',str(e)])
            
