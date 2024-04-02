from flask import Blueprint, request, jsonify
from flask_injector import inject
from DermAlertMS_Application.Commands.AddPatientCommand import AddPatientCommands
from DermAlertMS_Application.Handlers.Commands.AddPatientHandler import AddPatientHandler
from DermAlertMS_Application.Mappers.ResponseMapper import ModifyResponse
from DermAlertMS_Application.Exceptions.CustomException import CustomException
from DermAlertMS_Application.Responses.Response import Response
from DermAlertMS_Infrastructure.Utils.HttpStatusCode import HttpStatusCode
from DermAlertMS_Application.Requests.PatientRequest import PatientRequest
from DermAlertMS_Application.Handlers.Queries.ConsultPatientHandler import ConsultPatientHandler


patient = Blueprint("patients", __name__)

@patient.route("/", methods=['POST'])

@inject
def PostPatient(handler: AddPatientHandler):
    try:
        command = AddPatientCommands(PatientRequest(request)) 
        response = handler.Handle(command)
        return jsonify(ModifyResponse(response)), 201 
    except CustomException as e:
        response = Response('Datos no válidos',HttpStatusCode['BAD REQUEST'],'',False,e.errorMessage)
        return jsonify(ModifyResponse(response)), 400


@patient.route("/", methods=['GET'])

@inject
def GetUniversity(handler: ConsultPatientHandler):
    try:
        response = handler.Handle()
        return jsonify(ModifyResponse(response)), 201 
    except CustomException as e:
        response = Response('No se poseen universidades registradas',HttpStatusCode['NOT FOUND'],'',False,e.errorMessage)
        return jsonify(ModifyResponse(response)), 404
    
