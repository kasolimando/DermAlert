from DermAlertMS_Core.Database.IDermAlertDBContext import IDermAlertDBContext
from DermAlertMS_Core.Entities.Patient import Patient
from DermAlertMS_Core.Entities.Person import Person
from DermAlertMS_Application.Exceptions.CustomException import CustomException
from DermAlertMS_Application.Validators.PersonValidator import PersonValidator
from DermAlertMS_Application.Validations.AdminValidations import ValidateAdmin
from DermAlertMS_Core.Entities.Doctor import Doctor


def ValidateData(dermAlertDBContext: IDermAlertDBContext,person : Person):
    try:
        validator = PersonValidator(data=vars(person))
        if validator.validate():
            patientValidate = dermAlertDBContext.getByField(Person,'username', person.username)
            if patientValidate:
                raise CustomException([f'Ya existe el usuario {person.username}'])
        else:
            raise CustomException(list(validator.errors.values()))
    except CustomException as e:
        raise CustomException(e.errorMessage)
    except Exception as e:
        raise CustomException(['Ha ocurrido un error por favor intente mas tarde Validation',str(e)])
    
def ValidateDelete(dermAlertDBContext: IDermAlertDBContext, id):
    try:
        patient = ValidatePatient(dermAlertDBContext,id)
        doctor = dermAlertDBContext.getByField(Doctor,'Patient', Patient.id)
        if doctor:
            raise CustomException([f'El doctor {doctor.username} tiene afiliada esa universidad'])
        else:
            return Patient
    except CustomException as e:
        raise CustomException(e.errorMessage)
    except Exception as e:
        raise CustomException(['Ha ocurrido un error por favor intente mas tarde Validation',str(e)])


def ValidatePatient(dermAlertDBContext: IDermAlertDBContext, username):
    patientValidate = dermAlertDBContext.getByField(Patient,'username', username)
    if patientValidate is None:
        raise CustomException([f'No el usuario {username}'])
    return patientValidate


def ValidatePut(newPatient: Patient):
    validator = PersonValidator(data=vars(newPatient))
    if not validator.validate():
        raise CustomException(list(validator.errors.values()))
            