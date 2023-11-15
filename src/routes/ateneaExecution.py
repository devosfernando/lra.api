from flask import Blueprint, request, jsonify
from controllers.ateneaExecution import listarPrevMonht, listarLastMonht

routering = Blueprint('routering', __name__)

@routering.route('/prevMonht/ateneaExecution', methods=['GET'])
def prev_month_atenea_execution_route():
    return listarPrevMonht(request, jsonify)

@routering.route('/lastMonht/ateneaExecution', methods=['GET'])
def last_month_atenea_execution_route():
    return listarLastMonht(request, jsonify)