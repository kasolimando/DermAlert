from flask import Blueprint, request, jsonify
from flask_injector import inject
from DermAlertMS_Application.Commands.AddRecommendationCommand import AddRecommendationCommands
from DermAlertMS_Application.Commands.DeleteRecommendationCommand import DeleteRecommendationCommands
from DermAlertMS_Application.Commands.PutRecommendationCommand import PutRecommendationCommands
from DermAlertMS_Application.Handlers.Commands.AddRecommendationHandler import AddRecommendationHandler
from DermAlertMS_Application.Handlers.Queries.ConsultRecommendationHandler import ConsultRecommendationHandler
from DermAlertMS_Application.Handlers.Commands.DeleteRecommendationHandler import DeleteRecommendationHandler
from DermAlertMS_Application.Handlers.Commands.PutRecommendationHandler import PutRecommendationHandler
from DermAlertMS_Application.Mappers.ResponseMapper import ModifyResponse
from DermAlertMS_Application.Exceptions.CustomException import CustomException
from DermAlertMS_Application.Responses.Response import Response
from DermAlertMS_Infrastructure.Utils.HttpStatusCode import HttpStatusCode
from DermAlertMS_Application.Requests.RecommendationRequest import RecommendationRequest

recommendations = Blueprint("recommendations", __name__)

@recommendations.route("/", methods=['POST'])

@inject
def PostRecommendation(handler: AddRecommendationHandler):
    try:
        command = AddRecommendationCommands(RecommendationRequest(request)) 
        response = handler.Handle(command)
        return jsonify(ModifyResponse(response)), response.status_code 
    except CustomException as e:
        response = Response('Datos no válidos',HttpStatusCode['BAD REQUEST'],'',False,e.errorMessage)
        return jsonify(ModifyResponse(response)), HttpStatusCode['BAD REQUEST']
    

@recommendations.route("/", methods=['GET'])

@inject
def GetRecommendation(handler: ConsultRecommendationHandler):
    try:
        response = handler.Handle()
        return jsonify(ModifyResponse(response)), response.status_code  
    except CustomException as e:
        response = Response('No se poseen universidades registradas',HttpStatusCode['NOT FOUND'],'',False,e.errorMessage)
        return jsonify(ModifyResponse(response)), HttpStatusCode['NOT FOUND']
    


@recommendations.route("/<int:id>", methods=['DELETE'])

@inject
def DeleteRecommendation(handler: DeleteRecommendationHandler, id):
    try:
        command = DeleteRecommendationCommands(id)
        response = handler.Handle(command)
        return jsonify(ModifyResponse(response)), response.status_code 
    except CustomException as e:
        response = Response('No se poseen universidades registradas',HttpStatusCode['NOT FOUND'],'',False,e.errorMessage)
        return jsonify(ModifyResponse(response)), HttpStatusCode['NOT FOUND']
    
@recommendations.route("/<int:id>", methods=['PUT'])

@inject
def PutRecommendation(handler: PutRecommendationHandler, id):
    try:
        command = PutRecommendationCommands(RecommendationRequest(request),id)
        response = handler.Handle(command)
        return jsonify(ModifyResponse(response)), response.status_code 
    except CustomException as e:
        response = Response('No se poseen universidades registradas',HttpStatusCode['CONFLICT'],'',False,e.errorMessage)
        return jsonify(ModifyResponse(response)), HttpStatusCode['CONFLICT']
