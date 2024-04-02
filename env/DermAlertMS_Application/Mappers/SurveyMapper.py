from DermAlertMS_Core.Entities.Survey import Survey
from DermAlertMS_Application.Requests.SurveyRequest import SurveyRequest
import json
from datetime import date
from DermAlertMS_Application.Responses.SurveyResponse import SurveyResponses


def MapRequestEntity(request: SurveyRequest):
    return Survey(request.description, 
                  request.atr, 
                      request.created_by,
                      request.updated_by)

    
def EntityToRequest(surveys):
    result = []
    for survey in surveys:
        surveyReponse = SurveyResponses(survey)
        data =  json.loads(json.dumps(surveyReponse.__dict__, ensure_ascii=False))
        result.append(data)
    return result

def EntityToNewEntity(newSurvey, oldSurvey):
    oldSurvey.question = newSurvey.question
    oldSurvey.value = newSurvey.value
    oldSurvey.updated_by = newSurvey.updated_by
    oldSurvey.updated_at = date.today()