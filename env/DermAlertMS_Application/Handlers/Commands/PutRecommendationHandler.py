import itertools
from flask_injector import inject
from DermAlertMS_Core.Database.IDermAlertDBContext import IDermAlertDBContext
from DermAlertMS_Application.Commands.PutRecommendationCommand import PutRecommendationCommands
from DermAlertMS_Application.Mappers.RecommendationMapper import *
from DermAlertMS_Application.Responses.Response import Response
from DermAlertMS_Infrastructure.Utils.HttpStatusCode import HttpStatusCode
from DermAlertMS_Application.Exceptions.CustomException import CustomException
from DermAlertMS_Application.Validations.RecommendationValidation import ValidateRecommendation,ValidatePut


class PutRecommendationHandler:

    @inject
    def __init__(self, dermAlertDBContext: IDermAlertDBContext):
        self._dermAlertDBContext = dermAlertDBContext

    def Handle(self,request : PutRecommendationCommands):
        try:
            if (request.requestPutRecommendation is None or request.requestId is None):
                raise CustomException(['Solicitud Invalida'])
            else:
                newRecommendation = MapRequestEntity(request.requestPutRecommendation)
                oldRecommendation = ValidateRecommendation(self._dermAlertDBContext,request.requestId)
                ValidatePut(newRecommendation)
                EntityToNewEntity(newRecommendation,oldRecommendation)
                self._dermAlertDBContext.Commit()
                return Response('La operación ha sido exitosa',HttpStatusCode['OK'],'',True,'')
        except CustomException as e:
            raise CustomException(list(itertools.chain(*e.errorMessage)))
        except Exception as e:
            raise CustomException(['Ha ocurrido un error por favor intente mas tarde handler',str(e)])
            
