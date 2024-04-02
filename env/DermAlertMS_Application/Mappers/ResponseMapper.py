from DermAlertMS_Application.Responses.Response import Response
import json

def ModifyResponse(response : Response):
    return json.loads(json.dumps(response.__dict__, ensure_ascii=False))