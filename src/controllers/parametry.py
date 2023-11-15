from flask import jsonify
from database.conection import prepareConnection

controlador = {
    'listarParametry': {},
}

def listar_parametry(req, res):
    try:
        result = prepareConnection(10)
        res.status_code = 200
        return jsonify({
            'status': 200,
            'message': 'Ok',
            'response': result
        })
    except Exception as e:
        res.status_code = 500
        return jsonify({
            'status': 500,
            'message': 'Internal Server Error',
            'response': str(e)
        })

def get_parametry_front(req, res):
    try:
        result = prepareConnection(11)
        res.status_code = 200
        return jsonify({
            'status': 200,
            'message': 'Ok',
            'response': result
        })
    except Exception as e:
        res.status_code = 500
        return jsonify({
            'status': 500,
            'message': 'Internal Server Error',
            'response': str(e)
        })

controlador['listarParametry'] = listar_parametry
controlador['getParametryFront'] = get_parametry_front

# Exportación del controlador
