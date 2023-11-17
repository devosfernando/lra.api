from flask import Blueprint, request, jsonify
from controllers.trx import listarTrx, listarSixMonth

routerTrx = Blueprint('routering', __name__)

@routerTrx.route('/trx', methods=['GET'])
def trx_route():
    return listarTrx(request, jsonify)

@routerTrx.route('/trxLasteSixMoth', methods=['GET'])
def six_month_trx_route():
    return listarSixMonth(request, jsonify)
