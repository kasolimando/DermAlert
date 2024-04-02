from flask_injector import inject
from DermAlertMS_Core.Database.IDermAlertDBContext import IDermAlertDBContext
from DermAlertMS_Application.Queries.ConsultPatientQuery import ConsultPatientQuery
from DermAlertMS_Application.Mappers.PatientMapper import *
from DermAlertMS_Application.Responses.Response import Response
from DermAlertMS_Infrastructure.Utils.HttpStatusCode import HttpStatusCode
from DermAlertMS_Application.Exceptions.CustomException import CustomException
from DermAlertMS_Core.Entities.Person import Person
from DermAlertMS_Core.Entities.Patient import Patient


class ConsultPatientHandler:

    @inject
    def __init__(self, dermAlertDBContext: IDermAlertDBContext):
        self._dermAlertDBContext = dermAlertDBContext

    def Handle(self):
        try:
            patients = self._dermAlertDBContext.getAllJoin(Person,Patient)
            patients = EntityToRequest(patients)
            return Response('',HttpStatusCode['OK'],patients,True,'')
        except CustomException as e:
            raise CustomException(e.errorMessage)  
        except Exception as e:
            raise CustomException(['Ha ocurrido un error por favor intente mas tarde handler',str(e)])
            
