from flask import Flask, request, send_from_directory
from flask_cors import CORS
from routes import index  # Asegúrate de tener un archivo llamado routes/index.py con tu enrutador
from pushNotification import push

app = Flask(__name__)
CORS(app)

@app.route('/api/1', methods=['GET', 'POST', 'OPTIONS', 'PUT', 'DELETE'])
def api():
    return index.route(request)

@app.route('/dispacher', methods=['GET', 'POST', 'OPTIONS', 'PUT', 'DELETE'])
def dispacher():
    return push.route(request)

@app.route('/')
def root():
    return send_from_directory(__name__, 'index.html')

if __name__ == '__main__':
    app.run(port=8080)