from flask import Blueprint, request, jsonify
from controllers.channelExecution import listarPrevMonht, listarLastMonht

routering = Blueprint('routering', __name__)

@routering.route('/prevMonht/channelExecutions', methods=['GET'])
def prev_month_channel_executions_route():
    return listarPrevMonht(request, jsonify)

@routering.route('/lastMonht/channelExecutions', methods=['GET'])
def last_month_channel_executions_route():
    return listarLastMonht(request, jsonify)
