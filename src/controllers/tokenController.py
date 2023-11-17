from flask import jsonify, request
from services.tokenServices import validateData, validateDataInsert


def getTokenJira(req, res):
    try:
        resolve = validateData()
        res.status_code = 200
        return jsonify({
            'status': 200,
            'message': 'Ok',
            'response': resolve
        })
    except Exception as e:
        res.status_code = 500
        return jsonify({
            'status': 500,
            'message': 'Internal Server Error',
            'response': str(e)
        })

def updateDate(req, res):
    try:
        resp = validateDataInsert(req.json)
        res.status_code = 200
        return jsonify({
            'status': 200,
            'message': 'Ok',
            'response': resp
        })
    except Exception as e:
        res.status_code = 500
        return jsonify({
            'status': 500,
            'message': 'Internal Server Error',
            'response': str(e)
        })

# Asignación de funciones al controlador (ya no necesitas esta parte si usas el enfoque de decoradores)
# controlador['getTokenJira'] = get_token_jira
# controlador['updateDate'] = update_date

# Exportación del controlador (también puedes exportar las funciones directamente si usas el enfoque de decoradores)
# return controlador
