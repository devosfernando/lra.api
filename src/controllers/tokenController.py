from flask import jsonify, request
from services.tokenServices import validateData, validateDataInsert

controlador = {
    'listar': {},
}

def get_token_jira(req, res):
    try:
        validateData().then(resolve => {
            res.status_code = 200
            return jsonify({
                'status': 200,
                'message': 'Ok',
                'response': resolve
            })
        }).catch(reject => {
            res.status_code = 200
            return jsonify({
                'status': 200,
                'message': 'Ok',
                'response': reject
            })
        })
    except Exception as e:
        res.status_code = 500
        return jsonify({
            'status': 500,
            'message': 'Internal Server Error',
            'response': str(e)
        })

def update_date(req, res):
    try:
        validateDataInsert(req.json).then(resp => {
            res.status_code = 200
            return jsonify({
                'status': 200,
                'message': 'Ok',
                'response': resp
            })
        }).catch(err => {
            res.status_code = 200
            return jsonify({
                'status': 200,
                'message': 'Ok',
                'response': err
            })
        })
    except Exception as e:
        res.status_code = 500
        return jsonify({
            'status': 500,
            'message': 'Internal Server Error',
            'response': str(e)
        })

# Asignación de funciones al controlador
controlador['getTokenJira'] = get_token_jira
controlador['updateDate'] = update_date

# Exportación del controlador
