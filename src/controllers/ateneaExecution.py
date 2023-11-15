from flask import jsonify
from database.conection import prepareConnection

controlador = {
    'listar': {},
}

def listar_last_month(req, res):
    try:
        result = prepareConnection(4)
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

def listar_prev_month(req, res):
    try:
        result = prepareConnection(1)
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

# Asignación de funciones al controlador
controlador['listarLastMonht'] = listar_last_month
controlador['listarPrevMonht'] = listar_prev_month

# Exportación del controlador
