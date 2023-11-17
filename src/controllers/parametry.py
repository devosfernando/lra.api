from flask import jsonify
from database.conection import prepareConnection

controlador = {
    'listarParametry': {},
}

def listarParametry(req, res):
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

def getParametryFront(req, res):
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

controlador['listarParametry'] = listarParametry
controlador['getParametryFront'] = getParametryFront

# Exportación del controlador
