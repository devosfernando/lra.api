from flask import Blueprint, request, jsonify

#from src.jwt.jsonWebToken import generateAccessToken, validateToken, validarUserDominio
from routes.ateneaExecution import routerAteneaExecution
from routes.channelExecution import routerChannelExecution
from routes.executionsDate import routerExecutionsDate
from routes.tokenRoute import getTokenJira
from routes.kpi import routerkpi
from routes.trx import routerTrx
from routes.kpiYear import routerYearKpi
from routes.parametry import routerParametry

router = Blueprint('router', __name__)

@router.route('/kpi', methods=['GET', 'POST'])
def atenea_kpi_prevMonth_route():
    return routerAteneaExecution(request)

@router.route('/channel/execution', methods=['GET', 'POST']) 
def channel_execution_route():
    return routerChannelExecution(request)

@router.route('/kpi', methods=['GET', 'POST']) 
def kpi_route():
    return routerkpi(request)

@router.route('/trx', methods=['GET', 'POST'])
 
def trx_route():
    return routerTrx(request)

@router.route('/year/kpi', methods=['GET', 'POST'])
 
def year_kpi_route():
    return routerYearKpi(request)

@router.route('/token/jira', methods=['GET', 'POST'])
 
def get_token_jira_route():
    return getTokenJira(request)

@router.route('/executionsDate', methods=['GET', 'POST'])
def executions_date_route():
    return routerExecutionsDate(request)

@router.route('/parametry', methods=['GET', 'POST'])
 
def parametry_route():
    return routerParametry(request)

@router.route('/auth/parametry', methods=['GET', 'POST'])
def auth_parametry_route():
    return routerParametry(request)

bar ="""
@router.route('/auth/securityToken', methods=['POST'])
def security_token_route():
    email = request.json.get('email', '')
    if email == '':
        return jsonify({
            'status': 400,
            'message': 'Bad Request'
        }), 400
    else:
        resp = validarUserDominio(email)
        if resp:
            access_token = generateAccessToken(email)
            response = {
                'message': 'Usuario autenticado',
                'token': access_token
            }
            return jsonify(response), 200
        else:
            return jsonify({
                'status': 403,
                'message': 'Access Denied'
            }), 403"""