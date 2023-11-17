from flask import Blueprint, request, jsonify
from controllers.executionsDate import executionDate

routerExecutionsDate = Blueprint('routering', __name__)

@routerExecutionsDate.route('/executionsDate', methods=['GET'])
def executions_date_route():
    print("Entro por executions date desde endPoint")
    return executionDate(request, jsonify)
