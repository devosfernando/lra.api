from database.conection import prepareConnection

controlador = {
    'listar': {},
}

def listarTrx(req, res):
    try:
        resolve = prepareConnection(6)
        res.status_code = 200
        return {
            'status': 200,
            'message': 'Ok',
            'response': resolve
        }
    except Exception as e:
        res.status_code = 500
        return {
            'status': 500,
            'message': 'Internal Server Error',
            'response': str(e)
        }

def listarSixMonth(req, res):
    try:
        resolve = prepareConnection(7)
        res.status_code = 200
        return {
            'status': 200,
            'message': 'Ok',
            'response': resolve
        }
    except Exception as e:
        res.status_code = 500
        return {
            'status': 500,
            'message': 'Internal Server Error',
            'response': str(e)
        }

# Asignación de funciones al controlador
controlador['listarTrx'] = listarTrx
controlador['listarSixMonth'] = listarSixMonth

# Exportación del controlador