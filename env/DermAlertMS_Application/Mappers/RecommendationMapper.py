from DermAlertMS_Core.Entities.Recommendation import Recommendation
from DermAlertMS_Application.Requests.RecommendationRequest import RecommendationRequest
import json
from datetime import date
from DermAlertMS_Application.Responses.RecommendationResponse import RecommendationResponses


def MapRequestEntity(request: RecommendationRequest):
    return Recommendation(request.description, 
                  request.entry_value, 
                  request.end_value, 
                      request.created_by,
                      request.updated_by)

    
def EntityToRequest(recommendations):
    result = []
    for recommendation in recommendations:
        recommendationReponse = RecommendationResponses(recommendation)
        data =  json.loads(json.dumps(recommendationReponse.__dict__, ensure_ascii=False))
        result.append(data)
    return result

def EntityToNewEntity(newRecommendation, oldRecommendation):
    oldRecommendation.description = newRecommendation.description
    oldRecommendation.entry_value = newRecommendation.entry_value
    oldRecommendation.end_value = newRecommendation.end_value
    oldRecommendation.updated_by = newRecommendation.updated_by
    oldRecommendation.updated_at = date.today()