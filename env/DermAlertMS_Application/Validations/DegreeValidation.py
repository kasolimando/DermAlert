from DermAlertMS_Core.Database.IDermAlertDBContext import IDermAlertDBContext
from DermAlertMS_Core.Entities.Degree import Degree
from DermAlertMS_Application.Exceptions.CustomException import CustomException
from DermAlertMS_Application.Validators.DegreeValidator import DegreeValidator
from DermAlertMS_Application.Validations.AdminValidations import ValidateAdmin
from DermAlertMS_Core.Entities.Doctor import Doctor


def ValidateData(dermAlertDBContext: IDermAlertDBContext, degree: Degree):
    try:
        validator = DegreeValidator(data=vars(degree))
        if validator.validate():
            ValidateAdmin(dermAlertDBContext,degree.created_by)
            degreeValidate = dermAlertDBContext.getByField(Degree,'description', degree.description)
            if degreeValidate:
                raise CustomException([f'Ya existe el grado académico {degreeValidate.description}'])
        else:
            raise CustomException(list(validator.errors.values()))
    except CustomException as e:
        raise CustomException(e.errorMessage)
    except Exception as e:
        raise CustomException(['Ha ocurrido un error por favor intente mas tarde Validation',str(e)])
    
def ValidateDelete(dermAlertDBContext: IDermAlertDBContext, id):
    try:
        degree = ValidateDegree(dermAlertDBContext,id)
        doctor = dermAlertDBContext.getByField(Doctor,'degree', degree.id)
        if doctor:
            raise CustomException([f'El doctor {doctor.username} tiene afiliado ese grado académico'])
        else:
            return degree
    except CustomException as e:
        raise CustomException(e.errorMessage)
    except Exception as e:
        raise CustomException(['Ha ocurrido un error por favor intente mas tarde Validation',str(e)])


def ValidateDegree(dermAlertDBContext: IDermAlertDBContext, id):
    degreeValidate = dermAlertDBContext.getByField(Degree,'id', id)
    if degreeValidate is None:
        raise CustomException([f'No existe el grado académico {id}'])
    return degreeValidate


def ValidatePut(newDegree: Degree):
    validator = DegreeValidator(data=vars(newDegree))
    if not validator.validate():
        raise CustomException(list(validator.errors.values()))
            