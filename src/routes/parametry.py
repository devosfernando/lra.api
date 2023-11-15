from flask import Blueprint, request, jsonify
from jwt.jsonWebToken import validateToken
from controllers.parametry import listarParametry, getParametryFront

routering = Blueprint('routering', __name__)

@routering.route('/parametry', methods=['GET'])
@validateToken
def parametry_route():
    return listarParametry(request, jsonify)

@routering.route('/parametry/data', methods=['GET'])
def parametry_data_route():
    return getParametryFront(request, jsonify)
