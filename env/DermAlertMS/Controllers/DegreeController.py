from flask import Blueprint, request, jsonify
from flask_injector import inject
from DermAlertMS_Application.Commands.AddDegreeCommand import AddDegreeCommands
from DermAlertMS_Application.Commands.DeleteDegreeCommand import DeleteDegreeCommands
from DermAlertMS_Application.Commands.PutDegreeCommand import PutDegreeCommands
from DermAlertMS_Application.Handlers.Commands.AddDegreeHandler import AddDegreeHandler
from DermAlertMS_Application.Handlers.Queries.ConsultDegreeHandler import ConsultDegreeHandler
from DermAlertMS_Application.Handlers.Commands.DeleteDegreeHandler import DeleteDegreeHandler
from DermAlertMS_Application.Handlers.Commands.PutDegreeHandler import PutDegreeHandler
from DermAlertMS_Application.Mappers.ResponseMapper import ModifyResponse
from DermAlertMS_Application.Exceptions.CustomException import CustomException
from DermAlertMS_Application.Responses.Response import Response
from DermAlertMS_Infrastructure.Utils.HttpStatusCode import HttpStatusCode
from DermAlertMS_Application.Requests.DegreeRequest import DegreeRequest

degrees = Blueprint("degrees", __name__)

@degrees.route("/", methods=['POST'])

@inject
def PostDegree(handler: AddDegreeHandler):
    try:
        command = AddDegreeCommands(DegreeRequest(request)) 
        response = handler.Handle(command)
        return jsonify(ModifyResponse(response)), response.status_code  
    except CustomException as e:
        response = Response('Datos no válidos',HttpStatusCode['BAD REQUEST'],'',False,e.errorMessage)
        return jsonify(ModifyResponse(response)), HttpStatusCode['BAD REQUEST']
    

@degrees.route("/", methods=['GET'])

@inject
def GetDegree(handler: ConsultDegreeHandler):
    try:
        response = handler.Handle()
        return jsonify(ModifyResponse(response)), response.status_code 
    except CustomException as e:
        response = Response('No se poseen grados académicos registradas',HttpStatusCode['NOT FOUND'],'',False,e.errorMessage)
        return jsonify(ModifyResponse(response)), HttpStatusCode['NOT FOUND']
    


@degrees.route("/<int:id>", methods=['DELETE'])

@inject
def DeleteDegree(handler: DeleteDegreeHandler, id):
    try:
        command = DeleteDegreeCommands(id)
        response = handler.Handle(command)
        return jsonify(ModifyResponse(response)), response.status_code 
    except CustomException as e:
        response = Response('No se poseen grados académicos registradas',HttpStatusCode['NOT FOUND'],'',False,e.errorMessage)
        return jsonify(ModifyResponse(response)), HttpStatusCode['NOT FOUND']
    
@degrees.route("/<int:id>", methods=['PUT'])

@inject
def PutDegree(handler: PutDegreeHandler, id):
    try:
        command = PutDegreeCommands(DegreeRequest(request),id)
        response = handler.Handle(command)
        return jsonify(ModifyResponse(response)), response.status_code 
    except CustomException as e:
        response = Response('No se poseen grados académicos registradas',HttpStatusCode['CONFLICT'],'',False,e.errorMessage)
        return jsonify(ModifyResponse(response)), HttpStatusCode['CONFLICT']
