from flask import Blueprint, request, jsonify
from controllers.kpi import listarPrevMonht, listarLastMonht

routering = Blueprint('routering', __name__)

@routering.route('/prevMonht/kpi', methods=['GET'])
def prev_month_kpi_route():
    return listarPrevMonht(request, jsonify)

@routering.route('/lastMonht/kpi', methods=['GET'])
def last_month_kpi_route():
    return listarLastMonht(request, jsonify)