from flask import Blueprint, request, jsonify
from controllers.kpi import listarPrevMonht, listarLastMonht

routerkpi = Blueprint('routering', __name__)

@routerkpi.route('/prevMonht/kpi', methods=['GET'])
def prev_month_kpi_route():
    return listarPrevMonht(request, jsonify)

@routerkpi.route('/lastMonht/kpi', methods=['GET'])
def last_month_kpi_route():
    return listarLastMonht(request, jsonify)