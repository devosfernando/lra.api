from flask import jsonify
from database.conection import prepareConnection

controlador = {
    'listar': {},
}

# Definición de la función executionDate
def execution_date(req, res):
    try:
        result = prepareConnection(8)
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

# Asignación de la función al controlador
controlador['executionDate'] = execution_date

# Exportación del controlador
