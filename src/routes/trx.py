from flask import Blueprint, request, jsonify
from controllers.trx import listarTrx, listarSixMonht

routering = Blueprint('routering', __name__)

@routering.route('/trx', methods=['GET'])
def trx_route():
    return listarTrx(request, jsonify)

@routering.route('/trxLasteSixMoth', methods=['GET'])
def six_month_trx_route():
    return listarSixMonht(request, jsonify)
