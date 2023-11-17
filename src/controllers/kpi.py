from flask import jsonify
from database.conection import prepareConnection

controlador = {
    'listar': {},
}

def listarLastMonht(req, res):
    try:
        result = prepareConnection(3)
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

def listarPrevMonht(req, res):
    try:
        result = prepareConnection(0)
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


# Exportación del controlador
