from flask_injector import inject
from DermAlertMS_Core.Database.IDermAlertDBContext import IDermAlertDBContext
from DermAlertMS_Application.Queries.ConsultDegreeQuery import ConsultDegreeQuery
from DermAlertMS_Application.Mappers.DegreeMapper import *
from DermAlertMS_Application.Responses.Response import Response
from DermAlertMS_Infrastructure.Utils.HttpStatusCode import HttpStatusCode
from DermAlertMS_Application.Exceptions.CustomException import CustomException


class ConsultDegreeHandler:

    @inject
    def __init__(self, dermAlertDBContext: IDermAlertDBContext):
        self._dermAlertDBContext = dermAlertDBContext

    def Handle(self):
        try:
            degrees = self._dermAlertDBContext.getAll(Degree)
            degrees = EntityToRequest(degrees)
            return Response('',HttpStatusCode['OK'],degrees,True,'')
        except CustomException as e:
            raise CustomException(e.errorMessage)  
        except Exception as e:
            raise CustomException(['Ha ocurrido un error por favor intente mas tarde handler',str(e)])
            
