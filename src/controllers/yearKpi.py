from flask import jsonify
from database.conection import prepareConnection

controlador = {
    'listar': {},
}

def kpi_year(req, res):
    try:
        result = prepareConnection(9)
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
controlador['kpiYear'] = kpi_year

# Exportación del controlador
