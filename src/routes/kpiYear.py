from flask import Blueprint, request, jsonify
from controllers.yearKpi import kpiYear

routerYearKpi = Blueprint('routering', __name__)

@routerYearKpi.route('/year', methods=['GET'])
def year_kpi_route():
    print("Entro por ejecuciones para el año actual")
    return kpiYear(request, jsonify)