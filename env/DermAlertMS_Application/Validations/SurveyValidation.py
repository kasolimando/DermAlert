from DermAlertMS_Core.Database.IDermAlertDBContext import IDermAlertDBContext
from DermAlertMS_Core.Entities.Survey import Survey
from DermAlertMS_Application.Exceptions.CustomException import CustomException
from DermAlertMS_Application.Validators.SurveyValidator import SurveyValidator
from DermAlertMS_Application.Validations.AdminValidations import ValidateAdmin
from DermAlertMS_Core.Entities.Response import Response


def ValidateData(dermAlertDBContext: IDermAlertDBContext, survey: Survey):
    try:
        validator = SurveyValidator(data=vars(survey))
        if validator.validate():
            ValidateAdmin(dermAlertDBContext,survey.created_by)
            surveyValidate = dermAlertDBContext.getByField(Survey,'question', survey.question)
            if surveyValidate:
                raise CustomException([f'Ya existe la pregunta {surveyValidate.question}'])
        else:
            raise CustomException(list(validator.errors.values()))
    except CustomException as e:
        raise CustomException(e.errorMessage)
    except Exception as e:
        raise CustomException(['Ha ocurrido un error por favor intente mas tarde Validation',str(e)])
    
def ValidateDelete(dermAlertDBContext: IDermAlertDBContext, id):
    try:
        survey = ValidateSurvey(dermAlertDBContext,id)
        response = dermAlertDBContext.getByField(Response,'id', survey.id)
        if response:
            raise CustomException([f'Se cuentan con respuestas para la pregunta {response.question}'])
        else:
            return survey
    except CustomException as e:
        raise CustomException(e.errorMessage)
    except Exception as e:
        raise CustomException(['Ha ocurrido un error por favor intente mas tarde Validation',str(e)])


def ValidateSurvey(dermAlertDBContext: IDermAlertDBContext, id):
    surveyValidate = dermAlertDBContext.getByField(Survey,'id', id)
    if surveyValidate is None:
        raise CustomException([f'No existe la pregunta'])
    return surveyValidate


def ValidatePut(newSurvey: Survey):
    validator = SurveyValidator(data=vars(newSurvey))
    if not validator.validate():
        raise CustomException(list(validator.errors.values()))
            