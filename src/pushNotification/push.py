from flask import Flask, request, jsonify
from firebase_admin import messaging
from database.conection import prepareConnection
import os
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('API_ACCES_KEY')

def generate_notification_options():
    return messaging.AndroidConfig(
        priority='high',
        ttl=datetime.utcnow() + timedelta(days=1)
    )

def generate_message_notification(title, body):
    return messaging.Notification(
        title=title,
        body=body
    )

def send_message_to_token(registration_token, notification, options):
    message = messaging.Message(
        notification=notification,
        token=registration_token,
        android=options
    )
    return messaging.send(message)

def send_message_to_topic(topic, notification, options):
    message = messaging.Message(
        notification=notification,
        topic=topic,
        android=options
    )
    return messaging.send(message)

@app.route('/notification/token', methods=['POST'])
def send_notification_to_token():
    try:
        registration_token = request.json.get('registrationToken', '')
        if not registration_token:
            return jsonify({'status': 400, 'message': 'Bad Request'}), 400

        resolve = prepare_connection(0)
        notification_options = generate_notification_options()
        emoji = ''
        kpi_real = float(resolve[0]["hist_kpiReal"])
        kpi_estimado = float(resolve[0]["hist_kpiEstimado"])

        if kpi_real > kpi_estimado:
            emoji = '\U0001F44F'
            print("Esta con manitos arriba")
        elif kpi_real == kpi_estimado:
            emoji = '\U0001F603'
            print("Esta feliz")
        elif kpi_real < kpi_estimado:
            print("Esta triste")
            emoji = '\U0001F61F'

        notification_title = f'{emoji} ESTADISTICAS KPI BBVA'
        notification_body = f'Fecha: {resolve[0]["hist_date"].strftime("%Y-%m-%d")} \nKpi estimado: {kpi_estimado * 100:.2f}%\nKpi real: {kpi_real * 100:.2f}%'
        notification = generate_message_notification(notification_title, notification_body)

        send_message_to_token(registration_token, notification, notification_options)

        return jsonify({'status': 200, 'message': 'Ok', 'response': {'Status': 'Sending Notification to One user....'}})
    except Exception as e:
        return jsonify({'status': 500, 'message': 'Internal Server Error', 'response': str(e)}), 500

@app.route('/notification/topic', methods=['POST'])
def send_notification_to_topic():
    try:
        registration_topic = request.json.get('registrationTopic', '')
        if not registration_topic:
            return jsonify({'status': 400, 'message': 'Bad Request'}), 400

        resolve = prepare_connection(0)
        notification_options = generate_notification_options()
        emoji = ''
        kpi_real = float(resolve[0]["hist_kpiReal"])
        kpi_estimado = float(resolve[0]["hist_kpiEstimado"])

        if kpi_real > kpi_estimado:
            emoji = '\U0001F44F'
            print("Esta con manitos arriba")
        elif kpi_real == kpi_estimado:
            emoji = '\U0001F603'
            print("Esta feliz")
        elif kpi_real < kpi_estimado:
            print("Esta triste")
            emoji = '\U0001F61F'

        notification_title = f'{emoji} ESTADISTICAS KPI BBVA'
        notification_body = f'Fecha: {resolve[0]["hist_date"].strftime("%Y-%m-%d")} \nKpi estimado: {kpi_estimado * 100:.2f}%\nKpi real: {kpi_real * 100:.2f}%'
        notification = generate_message_notification(notification_title, notification_body)

        send_message_to_topic(registration_topic, notification, notification_options)

        return jsonify({'status': 200, 'message': 'Ok', 'response': {'Status': 'Sending Notification to One user....'}})
    except Exception as e:
        return jsonify({'status': 500, 'message': 'Internal Server Error', 'response': str(e)}), 500

if __name__ == '__main__':
    app.run(port=8080, debug=True)
