from flask import Flask, request, jsonify
import jwt
import os
import asyncio

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('API_ACCES_KEY')

def generateAccessToken(user):
    return jwt.encode({'user': user}, app.config['SECRET_KEY'], algorithm='HS256')

def validateToken(req, res, next):
    access_token = req.headers.get('Authorization')

    if not access_token:
        return jsonify({'status': 403, 'message': 'Access denied'}), 403

    try:
        user = jwt.decode(access_token, app.config['SECRET_KEY'], algorithms=['HS256'])
        req.user = user  # Almacenar el usuario decodificado en la solicitud para usarlo en otras partes del código si es necesario
        next()
    except jwt.ExpiredSignatureError:
        return jsonify({'status': 400, 'message': 'Access denied, token expired or incorrect'}), 400

async def validarUserDominio(user):
    dominio = user[user.index('@'):]
    return dominio.lower() == '@bbva.com'

@app.route('/generateToken', methods=['POST'])
async def generateToken():
    email = request.json.get('email', '')
    if not email:
        return jsonify({'status': 400, 'message': 'Bad Request'}), 400

    try:
        if await validarUserDominio(email):
            access_token = generateAccessToken(email)
            return jsonify({'status': 200, 'message': 'Token generated successfully', 'token': access_token.decode('utf-8')})
        else:
            return jsonify({'status': 403, 'message': 'Access denied'}), 403
    except Exception as e:
        return jsonify({'status': 500, 'message': 'Internal Server Error', 'response': str(e)}), 500

if __name__ == '__main__':
    app.run(port=8080, debug=True)
