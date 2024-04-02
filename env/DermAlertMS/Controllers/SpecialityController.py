from flask import Blueprint, request, jsonify
from flask_injector import inject
from DermAlertMS_Application.Commands.AddSpecialityCommand import AddSpecialityCommands
from DermAlertMS_Application.Commands.DeleteSpecialityCommand import DeleteSpecialityCommands
from DermAlertMS_Application.Commands.PutSpecialityCommand import PutSpecialityCommands
from DermAlertMS_Application.Handlers.Commands.AddSpeciliatyHandler import AddSpecialityHandler
from DermAlertMS_Application.Handlers.Queries.ConsultSpecialityHandler import ConsultSpecialityHandler
from DermAlertMS_Application.Handlers.Commands.DeleteSpecialityHandler import DeleteSpecialityHandler
from DermAlertMS_Application.Handlers.Commands.PutSpecialityHandler import PutSpecialityHandler
from DermAlertMS_Application.Mappers.ResponseMapper import ModifyResponse
from DermAlertMS_Application.Exceptions.CustomException import CustomException
from DermAlertMS_Application.Responses.Response import Response
from DermAlertMS_Infrastructure.Utils.HttpStatusCode import HttpStatusCode
from DermAlertMS_Application.Requests.SpecialityRequest import SpecialityRequest

specialities = Blueprint("specialities", __name__)

@specialities.route("/", methods=['POST'])

@inject
def PostSpeciality(handler: AddSpecialityHandler):
    try:
        command = AddSpecialityCommands(SpecialityRequest(request)) 
        response = handler.Handle(command)
        return jsonify(ModifyResponse(response)), 201 
    except CustomException as e:
        response = Response('Datos no válidos',HttpStatusCode['BAD REQUEST'],'',False,e.errorMessage)
        return jsonify(ModifyResponse(response)), 400
    

@specialities.route("/", methods=['GET'])

@inject
def GetSpeciality(handler: ConsultSpecialityHandler):
    try:
        response = handler.Handle()
        return jsonify(ModifyResponse(response)), 201 
    except CustomException as e:
        response = Response('No se poseen grados académicos registradas',HttpStatusCode['NOT FOUND'],'',False,e.errorMessage)
        return jsonify(ModifyResponse(response)), 404
    


@specialities.route("/<int:id>", methods=['DELETE'])

@inject
def DeleteSpeciality(handler: DeleteSpecialityHandler, id):
    try:
        command = DeleteSpecialityCommands(id)
        response = handler.Handle(command)
        return jsonify(ModifyResponse(response)), 204
    except CustomException as e:
        response = Response('No se poseen grados académicos registradas',HttpStatusCode['NOT FOUND'],'',False,e.errorMessage)
        return jsonify(ModifyResponse(response)), 404
    
@specialities.route("/<int:id>", methods=['PUT'])

@inject
def PutSpeciality(handler: PutSpecialityHandler, id):
    try:
        command = PutSpecialityCommands(SpecialityRequest(request),id)
        response = handler.Handle(command)
        return jsonify(ModifyResponse(response)), 200
    except CustomException as e:
        response = Response('No se poseen grados académicos registradas',HttpStatusCode['CONFLICT'],'',False,e.errorMessage)
        return jsonify(ModifyResponse(response)), 409
