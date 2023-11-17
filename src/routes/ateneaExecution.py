from flask import Blueprint, request, jsonify
from controllers.ateneaExecution import listarPrevMonth, listarLastMonth

routerAteneaExecution = Blueprint('routering', __name__)

@routerAteneaExecution.route('/prevMonht/ateneaExecution', methods=['GET'])
def prevMonthAteneaExecutionRoute():
    return listarPrevMonth(request, jsonify())

@routerAteneaExecution.route('/lastMonht/ateneaExecution', methods=['GET'])
def lastMonthAteneaExecutionRoute():
    return listarLastMonth(request, jsonify())