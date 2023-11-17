from flask import Blueprint, request, jsonify
from controllers.channelExecution import listarPrevMonth, listarLastMonth

routerChannelExecution = Blueprint('routering', __name__)

@routerChannelExecution.route('/prevMonht/channelExecutions', methods=['GET'])
def prev_month_channel_executions_route():
    return listarPrevMonth(request, jsonify)

@routerChannelExecution.route('/lastMonht/channelExecutions', methods=['GET'])
def last_month_channel_executions_route():
    return listarLastMonth(request, jsonify)
