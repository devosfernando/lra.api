from flask import Blueprint, request, jsonify
from controllers.tokenController import getTokenJira, updateDate

routering = Blueprint('routering', __name__)

@routering.route('/getToken', methods=['GET'])
def get_token_route():
    return getTokenJira(request, jsonify)

@routering.route('/update', methods=['POST'])
def update_route():
    return updateDate(request, jsonify)
