from flask import Blueprint, request, jsonify
from jwt.jsonWebToken import validateToken
from controllers.yearKpi import kpiYear

routering = Blueprint('routering', __name__)

@routering.route('/year', methods=['GET'])
@validateToken
def year_kpi_route():
    print("Entro por ejecuciones para el año actual")
    return kpiYear(request, jsonify)