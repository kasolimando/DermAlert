from DermAlertMS_Core.Database.IDermAlertDBContext import IDermAlertDBContext
from DermAlertMS_Core.Entities.Recommendation import Recommendation
from DermAlertMS_Application.Exceptions.CustomException import CustomException
from DermAlertMS_Application.Validators.RecommendationValidator import RecommendationValidator
from DermAlertMS_Application.Validations.AdminValidations import ValidateAdmin
from DermAlertMS_Core.Entities.Doctor import Doctor


def ValidateData(dermAlertDBContext: IDermAlertDBContext, recommendation: Recommendation):
    try:
        validator = RecommendationValidator(recommendation)
        if validator.validate():
            ValidateAdmin(dermAlertDBContext,recommendation.created_by)
            recommendationValidate = dermAlertDBContext.getByField(Recommendation,'description', recommendation.description)
            if recommendationValidate:
                raise CustomException([f'Ya existe la recomendación {recommendationValidate.description}'])
        else:
            raise CustomException(list(validator.errors.values()))
    except CustomException as e:
        raise CustomException(e.errorMessage)
    except Exception as e:
        raise CustomException(['Ha ocurrido un error por favor intente mas tarde Validation',str(e)])


def ValidateRecommendation(dermAlertDBContext: IDermAlertDBContext, id):
    RecommendationValidate = dermAlertDBContext.getByField(Recommendation,'id', id)
    if RecommendationValidate is None:
        raise CustomException([f'No existe la recomendación {id}'])
    return RecommendationValidate


def ValidatePut(newRecommendation: Recommendation):
    validator = RecommendationValidator(newRecommendation)
    if not validator.validate():
        raise CustomException(list(validator.errors.values()))
            