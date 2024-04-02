from DermAlertMS_Core.Database.IDermAlertDBContext import IDermAlertDBContext
from DermAlertMS_Core.Entities.University import University
from DermAlertMS_Application.Exceptions.CustomException import CustomException
from DermAlertMS_Application.Validators.UniversityValidator import UniversityValidator
from DermAlertMS_Application.Validations.AdminValidations import ValidateAdmin
from DermAlertMS_Core.Entities.Doctor import Doctor


def ValidateData(dermAlertDBContext: IDermAlertDBContext, university: University):
    try:
        validator = UniversityValidator(data=vars(university))
        if validator.validate():
            ValidateAdmin(dermAlertDBContext,university.created_by)
            universityValidate = dermAlertDBContext.getByField(University,'description', university.description)
            if universityValidate:
                raise CustomException([f'Ya existe la universidad {universityValidate.description}'])
        else:
            raise CustomException(list(validator.errors.values()))
    except CustomException as e:
        raise CustomException(e.errorMessage)
    except Exception as e:
        raise CustomException(['Ha ocurrido un error por favor intente mas tarde Validation',str(e)])
    
def ValidateDelete(dermAlertDBContext: IDermAlertDBContext, id):
    try:
        university = ValidateUniversity(dermAlertDBContext,id)
        doctor = dermAlertDBContext.getByField(Doctor,'university', university.id)
        if doctor:
            raise CustomException([f'El doctor {doctor.username} tiene afiliada esa universidad'])
        else:
            return university
    except CustomException as e:
        raise CustomException(e.errorMessage)
    except Exception as e:
        raise CustomException(['Ha ocurrido un error por favor intente mas tarde Validation',str(e)])


def ValidateUniversity(dermAlertDBContext: IDermAlertDBContext, id):
    universityValidate = dermAlertDBContext.getByField(University,'id', id)
    if universityValidate is None:
        raise CustomException([f'No existe la universidad {id}'])
    return universityValidate


def ValidatePut(newuniversity: University):
    validator = UniversityValidator(data=vars(newuniversity))
    if not validator.validate():
        raise CustomException(list(validator.errors.values()))
            