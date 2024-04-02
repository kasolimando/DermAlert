from DermAlertMS_Core.Entities.Admin import Admin
from DermAlertMS_Application.Exceptions.CustomException import CustomException
from DermAlertMS_Core.Database.IDermAlertDBContext import IDermAlertDBContext

def ValidateAdmin(dermAlertDBContext: IDermAlertDBContext, admin: str):
    try:
        adminValidate = dermAlertDBContext.getByField(Admin,'username', admin)
        if (adminValidate is None):
            raise CustomException([f'El administrador {admin} no existe'])
    except CustomException as e:
        raise CustomException(e.errorMessage)
    except Exception as e:
        raise CustomException(['Ha ocurrido un error por favor intente mas tarde Validation',str(e)])