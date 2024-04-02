from DermAlertMS_Core.Database.IDermAlertDBContext import IDermAlertDBContext
from DermAlertMS_Core.Entities.Speciality import Speciality
from DermAlertMS_Application.Exceptions.CustomException import CustomException
from DermAlertMS_Application.Validators.SpecialityValidator import SpecialityValidator
from DermAlertMS_Application.Validations.AdminValidations import ValidateAdmin
from DermAlertMS_Core.Entities.Doctor import Doctor


def ValidateData(dermAlertDBContext: IDermAlertDBContext, speciality: Speciality):
    try:
        validator = SpecialityValidator(data=vars(speciality))
        if validator.validate():
            ValidateAdmin(dermAlertDBContext,speciality.created_by)
            specialityValidate = dermAlertDBContext.getByField(Speciality,'description', speciality.description)
            if specialityValidate:
                raise CustomException([f'Ya existe la especialidad {specialityValidate.description}'])
        else:
            raise CustomException(list(validator.errors.values()))
    except CustomException as e:
        raise CustomException(e.errorMessage)
    except Exception as e:
        raise CustomException(['Ha ocurrido un error por favor intente mas tarde Validation',str(e)])
    
def ValidateDelete(dermAlertDBContext: IDermAlertDBContext, id):
    try:
        speciality = ValidateSpeciality(dermAlertDBContext,id)
        doctor = dermAlertDBContext.getByField(Doctor,'speciality', speciality.id)
        if doctor:
            raise CustomException([f'El doctor {doctor.username} tiene afiliado la especialidad'])
        else:
            return speciality
    except CustomException as e:
        raise CustomException(e.errorMessage)
    except Exception as e:
        raise CustomException(['Ha ocurrido un error por favor intente mas tarde Validation',str(e)])


def ValidateSpeciality(dermAlertDBContext: IDermAlertDBContext, id):
    specialityValidate = dermAlertDBContext.getByField(Speciality,'id', id)
    if specialityValidate is None:
        raise CustomException([f'No existe la especialidad {id}'])
    return specialityValidate


def ValidatePut(newSpeciality: Speciality):
    validator = SpecialityValidator(data=vars(newSpeciality))
    if not validator.validate():
        raise CustomException(list(validator.errors.values()))
            