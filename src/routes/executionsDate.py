from flask import Blueprint, request, jsonify
from jwt.jsonWebToken import validateToken
from controllers.executionsDate import executionDate

routering = Blueprint('routering', __name__)

@routering.route('/executionsDate', methods=['GET'])
@validateToken
def executions_date_route():
    print("Entro por executions date desde endPoint")
    return executionDate(request, jsonify)
