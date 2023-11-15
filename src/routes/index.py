from flask import Blueprint, request, jsonify
from jwt.jsonWebToken import generateAccessToken, validateToken, validarUserDominio
from ateneaExecution import executionAtenea
from channelExecution import channelExecution
from executionsDate import executionsDate
from tokenRoute import getTokenJira
from kpi import kpi
from trx import trx
from kpiYear import yearKpi
from parametry import parametry

router = Blueprint('router', __name__)

@router.route('/kpi', methods=['GET', 'POST'])
@validateToken
def kpi_route():
    return executionAtenea(request)

@router.route('/kpi', methods=['GET', 'POST'])
@validateToken
def channel_execution_route():
    return channelExecution(request)

@router.route('/kpi', methods=['GET', 'POST'])
@validateToken
def kpi_route():
    return kpi(request)

@router.route('/top', methods=['GET', 'POST'])
@validateToken
def trx_route():
    return trx(request)

@router.route('/kpi', methods=['GET', 'POST'])
@validateToken
def year_kpi_route():
    return yearKpi(request)

@router.route('/kpi', methods=['GET', 'POST'])
@validateToken
def parametry_route():
    return parametry(request)

@router.route('/token', methods=['GET', 'POST'])
@validateToken
def get_token_jira_route():
    return getTokenJira(request)

@router.route('/executionsDate', methods=['GET', 'POST'])
def executions_date_route():
    return executionsDate(request)

@router.route('/auth/parametry', methods=['GET', 'POST'])
def auth_parametry_route():
    return parametry(request)

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
            }), 403

