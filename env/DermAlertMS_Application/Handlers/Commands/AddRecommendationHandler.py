import itertools
from flask_injector import inject
from DermAlertMS_Core.Database.IDermAlertDBContext import IDermAlertDBContext
from DermAlertMS_Application.Commands.AddRecommendationCommand import AddRecommendationCommands
from DermAlertMS_Application.Mappers.RecommendationMapper import *
from DermAlertMS_Application.Responses.Response import Response
from DermAlertMS_Infrastructure.Utils.HttpStatusCode import HttpStatusCode
from DermAlertMS_Application.Exceptions.CustomException import CustomException
from DermAlertMS_Application.Validations.RecommendationValidation import ValidateData


class AddRecommendationHandler:

    @inject
    def __init__(self, dermAlertDBContext: IDermAlertDBContext):
        self._dermAlertDBContext = dermAlertDBContext

    def Handle(self,request : AddRecommendationCommands):
        try:
            if (request.requestAddRecommendation is None):
                raise CustomException(['Solicitud Invalida'])
            else:
                newRecommendation = MapRequestEntity(request.requestAddRecommendation)
                ValidateData(self._dermAlertDBContext,newRecommendation)
                self._dermAlertDBContext.save(newRecommendation)
                return Response('Ha sido existosa la operación',HttpStatusCode['CREATED'],'',True,'')
        except CustomException as e:
            raise CustomException(list(itertools.chain(*e.errorMessage)))
        except Exception as e:
            raise CustomException(['Ha ocurrido un error por favor intente mas tarde handler',str(e)])
            
