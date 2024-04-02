from flask import Blueprint, request, jsonify
from flask_injector import inject
from DermAlertMS_Application.Commands.AddUniversityCommand import AddUniversityCommands
from DermAlertMS_Application.Commands.DeleteUniversityCommand import DeleteUniversityCommands
from DermAlertMS_Application.Commands.PutUniversityCommand import PutUniversityCommands
from DermAlertMS_Application.Handlers.Commands.AddUniversityHandler import AddUniversityHandler
from DermAlertMS_Application.Handlers.Queries.ConsultUniversityHandler import ConsultUniversityHandler
from DermAlertMS_Application.Handlers.Commands.DeleteUniversityHandler import DeleteUniversityHandler
from DermAlertMS_Application.Handlers.Commands.PutUniversityHandler import PutUniversityHandler
from DermAlertMS_Application.Mappers.ResponseMapper import ModifyResponse
from DermAlertMS_Application.Exceptions.CustomException import CustomException
from DermAlertMS_Application.Responses.Response import Response
from DermAlertMS_Infrastructure.Utils.HttpStatusCode import HttpStatusCode
from DermAlertMS_Application.Requests.UniversityRequest import UniversityRequest

university = Blueprint("universities", __name__)

@university.route("/", methods=['POST'])

@inject
def PostUniversity(handler: AddUniversityHandler):
    try:
        command = AddUniversityCommands(UniversityRequest(request)) 
        response = handler.Handle(command)
        return jsonify(ModifyResponse(response)), 201 
    except CustomException as e:
        response = Response('Datos no válidos',HttpStatusCode['BAD REQUEST'],'',False,e.errorMessage)
        return jsonify(ModifyResponse(response)), 400
    

@university.route("/", methods=['GET'])

@inject
def GetUniversity(handler: ConsultUniversityHandler):
    try:
        response = handler.Handle()
        return jsonify(ModifyResponse(response)), 201 
    except CustomException as e:
        response = Response('No se poseen universidades registradas',HttpStatusCode['NOT FOUND'],'',False,e.errorMessage)
        return jsonify(ModifyResponse(response)), 404
    


@university.route("/<int:id>", methods=['DELETE'])

@inject
def DeleteUniversity(handler: DeleteUniversityHandler, id):
    try:
        command = DeleteUniversityCommands(id)
        response = handler.Handle(command)
        return jsonify(ModifyResponse(response)), 204
    except CustomException as e:
        response = Response('No se poseen universidades registradas',HttpStatusCode['NOT FOUND'],'',False,e.errorMessage)
        return jsonify(ModifyResponse(response)), 404
    
@university.route("/<int:id>", methods=['PUT'])

@inject
def PutUniversity(handler: PutUniversityHandler, id):
    try:
        command = PutUniversityCommands(UniversityRequest(request),id)
        response = handler.Handle(command)
        return jsonify(ModifyResponse(response)), 200
    except CustomException as e:
        response = Response('No se poseen universidades registradas',HttpStatusCode['CONFLICT'],'',False,e.errorMessage)
        return jsonify(ModifyResponse(response)), 409
