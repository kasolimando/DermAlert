from DermAlertMS_Core.Database.IDermAlertDBContext import IDermAlertDBContext
from DermAlertMS_Core.Entities.Person import Person
from DermAlertMS_Application.Exceptions.CustomException import CustomException


def ValidateData(dermAlertDBContext: IDermAlertDBContext,username):
    try:
        personValidate = dermAlertDBContext.getByField(Person,'username', username)
        if personValidate is None:
            raise CustomException([f'No existe el usuario {username}'])
        return personValidate
    except CustomException as e:
        raise CustomException(e.errorMessage)
    except Exception as e:
        raise CustomException(['Ha ocurrido un error por favor intente mas tarde Validation',str(e)])