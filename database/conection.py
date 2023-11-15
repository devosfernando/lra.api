import pymysql
import json
import os

# Cargar las configuraciones desde el archivo .env
from dotenv import load_dotenv
load_dotenv()

# Cargar las consultas desde el archivo JSON
with open('querys.json', 'r') as file:
    querys = json.load(file)

def query_switch(datos):
    switcher = {
        0: "Kpi mes anterior",
        1: "Ejecuciones del mes anterior Atenea",
        2: "Canal Ejecuciones Mes anterior",
        3: "Kpi mes actual",
        4: "Ejecuciones del ultimo mes Atenea",
        5: "Canal de ejecuciones ultimo mes",
        6: "Top Transacciones",
        7: "Top Transacciones 6 meses",
        8: "Fecha de ejecuciones mes actual Mainframe vs Ether",
        9: "Fecha de ejecuciones para el año actual",
        10: "Parametria para grafica",
        11: "Parametria para front",
        12: "Parametria DB para JIRA",
        13: "Insert DB para JIRA",
    }
    return switcher.get(datos, "Invalid query index")

def prepare_connection(queryf, database_con="planbackend"):
    datos_conexion = {}
    
    print(f"BASE DE DATOS {database_con}")

    if database_con == "planbackend":
        datos_conexion = {
            "host": os.environ.get("HOST"),
            "port": int(os.environ.get("PORT")),
            "database": os.environ.get("DATABASE"),
            "user": os.environ.get("USER"),
            "password": os.environ.get("PASSWORD"),
        }
    else:
        datos_conexion = {
            "host": os.environ.get("HOST"),
            "port": int(os.environ.get("PORT")),
            "database": os.environ.get("DATABASE_JIRA"),
            "user": os.environ.get("USER"),
            "password": os.environ.get("PASSWORD"),
        }

    connection = pymysql.connect(**datos_conexion)

    try:
        with connection.cursor() as cursor:
            print(f"Datos desde el queryf {queryf}")
            respuesta = query_switch(queryf)
            print(respuesta)

            cursor.execute(querys[respuesta])

            result = cursor.fetchall()
            return result
    finally:
        connection.close()

def insert_data(fecha, token, queryf):
    datos_conexion = {
        "host": os.environ.get("HOST"),
        "port": int(os.environ.get("PORT")),
        "database": os.environ.get("DATABASE_JIRA"),
        "user": os.environ.get("USER"),
        "password": os.environ.get("PASSWORD"),
    }

    connection = pymysql.connect(**datos_conexion)

    try:
        with connection.cursor() as cursor:
            print(f"Datos desde el queryf {queryf}")
            respuesta = query_switch(queryf)
            print(respuesta)

            cursor.execute(querys[respuesta], [fecha, token])

            connection.commit()
            result = cursor.fetchall()
            return result
    finally:
        connection.close()

# Ejemplo de uso
# reemplaza 0 con el índice del caso que deseas probar
result = prepare_connection(0)
print(result)

# reemplaza 13 con el índice del caso que deseas probar
result_insert = insert_data("2023-01-01", "example_token", 13)
print(result_insert)
