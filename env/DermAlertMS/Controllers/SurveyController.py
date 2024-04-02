from flask import Blueprint, request, jsonify
from flask_injector import inject
from DermAlertMS_Application.Commands.AddSurveyCommand import AddSurveyCommands
from DermAlertMS_Application.Commands.DeleteSurveyCommand import DeleteSurveyCommands
from DermAlertMS_Application.Commands.PutSurveyCommand import PutSurveyCommands
from DermAlertMS_Application.Handlers.Commands.AddSurveyHandler import AddSurveyHandler
from DermAlertMS_Application.Handlers.Queries.ConsultSurveyHandler import ConsultSurveyHandler
from DermAlertMS_Application.Handlers.Commands.DeleteSurveyHandler import DeleteSurveyHandler
from DermAlertMS_Application.Handlers.Commands.PutSurveyHandler import PutSurveyHandler
from DermAlertMS_Application.Mappers.ResponseMapper import ModifyResponse
from DermAlertMS_Application.Exceptions.CustomException import CustomException
from DermAlertMS_Application.Responses.Response import Response
from DermAlertMS_Infrastructure.Utils.HttpStatusCode import HttpStatusCode
from DermAlertMS_Application.Requests.SurveyRequest import SurveyRequest

surveys = Blueprint("surveys", __name__)

@surveys.route("/", methods=['POST'])

@inject
def PostSurvey(handler: AddSurveyHandler):
    try:
        command = AddSurveyCommands(SurveyRequest(request)) 
        response = handler.Handle(command)
        return jsonify(ModifyResponse(response)), 201 
    except CustomException as e:
        response = Response('Datos no válidos',HttpStatusCode['BAD REQUEST'],'',False,e.errorMessage)
        return jsonify(ModifyResponse(response)), 400
    

@surveys.route("/", methods=['GET'])

@inject
def GetSurvey(handler: ConsultSurveyHandler):
    try:
        response = handler.Handle()
        return jsonify(ModifyResponse(response)), 201 
    except CustomException as e:
        response = Response('No se poseen universidades registradas',HttpStatusCode['NOT FOUND'],'',False,e.errorMessage)
        return jsonify(ModifyResponse(response)), 404
    


@surveys.route("/<int:id>", methods=['DELETE'])

@inject
def DeleteSurvey(handler: DeleteSurveyHandler, id):
    try:
        command = DeleteSurveyCommands(id)
        response = handler.Handle(command)
        return jsonify(ModifyResponse(response)), 204
    except CustomException as e:
        response = Response('No se poseen universidades registradas',HttpStatusCode['NOT FOUND'],'',False,e.errorMessage)
        return jsonify(ModifyResponse(response)), 404
    
@surveys.route("/<int:id>", methods=['PUT'])

@inject
def PutSurvey(handler: PutSurveyHandler, id):
    try:
        command = PutSurveyCommands(SurveyRequest(request),id)
        response = handler.Handle(command)
        return jsonify(ModifyResponse(response)), 200
    except CustomException as e:
        response = Response('No se poseen universidades registradas',HttpStatusCode['CONFLICT'],'',False,e.errorMessage)
        return jsonify(ModifyResponse(response)), 409
