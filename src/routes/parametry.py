from flask import Blueprint, request, jsonify
from controllers.parametry import listarParametry, getParametryFront

routerParametry = Blueprint('routering', __name__)

@routerParametry.route('/parametry', methods=['GET'])
def parametry_route():
    return listarParametry(request, jsonify)

@routerParametry.route('/parametry/data', methods=['GET'])
def parametry_data_route():
    return getParametryFront(request, jsonify)
