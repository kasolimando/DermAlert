from flask_injector import inject
from DermAlertMS_Core.Database.IDermAlertDBContext import IDermAlertDBContext
from DermAlertMS_Application.Queries.ConsultUniversityQuery import ConsultUniversityQuery
from DermAlertMS_Application.Mappers.UniversityMapper import *
from DermAlertMS_Application.Responses.Response import Response
from DermAlertMS_Infrastructure.Utils.HttpStatusCode import HttpStatusCode
from DermAlertMS_Application.Exceptions.CustomException import CustomException


class ConsultUniversityHandler:

    @inject
    def __init__(self, dermAlertDBContext: IDermAlertDBContext):
        self._dermAlertDBContext = dermAlertDBContext

    def Handle(self):
        try:
            universities = self._dermAlertDBContext.getAll(University)
            universities = EntityToRequest(universities)
            return Response('',HttpStatusCode['OK'],universities,True,'')
        except CustomException as e:
            raise CustomException(e.errorMessage)  
        except Exception as e:
            raise CustomException(['Ha ocurrido un error por favor intente mas tarde handler',str(e)])
            
