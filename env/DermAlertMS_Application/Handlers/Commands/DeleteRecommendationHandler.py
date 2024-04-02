from flask_injector import inject
from DermAlertMS_Core.Database.IDermAlertDBContext import IDermAlertDBContext
from DermAlertMS_Application.Commands.DeleteRecommendationCommand import DeleteRecommendationCommands
from DermAlertMS_Application.Mappers.RecommendationMapper import *
from DermAlertMS_Application.Responses.Response import Response
from DermAlertMS_Infrastructure.Utils.HttpStatusCode import HttpStatusCode
from DermAlertMS_Application.Exceptions.CustomException import CustomException
from DermAlertMS_Application.Validations.RecommendationValidation import ValidateRecommendation


class DeleteRecommendationHandler:

    @inject
    def __init__(self, dermAlertDBContext: IDermAlertDBContext):
        self._dermAlertDBContext = dermAlertDBContext

    def Handle(self,request : DeleteRecommendationCommands):
        try:
            if (request.requestDeleteRecommendation is None):
                raise CustomException(['Solicitud Invalida'])
            else:
                recommendation = ValidateRecommendation(self._dermAlertDBContext,request.requestDeleteRecommendation)
                self._dermAlertDBContext.delete(recommendation)
                return Response('Ha sido exitosa la operacion',HttpStatusCode['NO CONTENT'],'',True,'')
        except CustomException as e:
            raise CustomException(e.errorMessage)
        except Exception as e:
            raise CustomException(['Ha ocurrido un error por favor intente mas tarde handler',str(e)])
            
