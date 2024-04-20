from flask import Blueprint, request, jsonify
from flask_injector import inject
from DermAlertMS_Application.Commands.PatchStatusCommand import PatchStatusCommand
from DermAlertMS_Application.Handlers.Commands.PatchStatusHandler import PatchStatusHandler
from DermAlertMS_Application.Mappers.ResponseMapper import ModifyResponse
from DermAlertMS_Application.Exceptions.CustomException import CustomException
from DermAlertMS_Application.Responses.Response import Response
from DermAlertMS_Infrastructure.Utils.HttpStatusCode import HttpStatusCode
from DermAlertMS_Application.Requests.StatusRequest import StatusRequest


people = Blueprint("people", __name__)


@people.route("/<username>", methods=['PATCH'])

@inject
def StatusPatient(handler: PatchStatusHandler, username):
    try:
        command = PatchStatusCommand(StatusRequest(request),username)
        response = handler.Handle(command)
        return jsonify(ModifyResponse(response)), response.status_code 
    except CustomException as e:
        response = Response('Ha ocurrido un error, por favor intente más tarde',HttpStatusCode['CONFLICT'],'',False,e.errorMessage)
        return jsonify(ModifyResponse(response)), HttpStatusCode['CONFLICT']
