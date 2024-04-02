from flask_injector import inject
from DermAlertMS_Core.Database.IDermAlertDBContext import IDermAlertDBContext
from DermAlertMS_Application.Queries.ConsultSpecialityQuery import ConsultSpecialityQuery
from DermAlertMS_Application.Mappers.SpecialityMapper import *
from DermAlertMS_Application.Responses.Response import Response
from DermAlertMS_Infrastructure.Utils.HttpStatusCode import HttpStatusCode
from DermAlertMS_Application.Exceptions.CustomException import CustomException


class ConsultSpecialityHandler:

    @inject
    def __init__(self, dermAlertDBContext: IDermAlertDBContext):
        self._dermAlertDBContext = dermAlertDBContext

    def Handle(self):
        try:
            specialities = self._dermAlertDBContext.getAll(Speciality)
            specialities = EntityToRequest(specialities)
            return Response('',HttpStatusCode['OK'],specialities,True,'')
        except CustomException as e:
            raise CustomException(e.errorMessage)  
        except Exception as e:
            raise CustomException(['Ha ocurrido un error por favor intente mas tarde handler',str(e)])
            
