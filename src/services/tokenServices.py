import os
import datetime
import requests
from database.conection import prepareConnection, insertData
from dotenv import load_dotenv

load_dotenv()

messageError = os.environ.get("MESSAGE_ERROR")
urlCurl = os.environ.get("URL_CURL")


def validateData():
    def validateMain(dataDate, dataValue):
        resFunction = validateDateAndDate(dataDate)
        if resFunction is not False:
            return dataValue
        else:
            callPython()
            return False

    def callPython():
        print("ENTRO POR LLAMADO AL PYTHON")
        response = requests.get(urlCurl)
        data = response.json()
        print(data)

    def validateDateAndDate(fecha):
        fechaData = datetime.datetime.strptime(fecha, "%Y-%m-%d %H:%M:%S.%f")
        fechaActual = datetime.datetime.now()
        diferenciaEnMinutos = (fechaActual - fechaData).total_seconds() / 60
        if diferenciaEnMinutos > 10:
            print("La fechaActual es mayor a 10 minutos que la fecha del token Jira.")
            return False
        else:
            print("La fechaActual no es mayor a 10 minutos que la fecha del token Jira.")
            return True

    try:
        resolve = prepareConnection(12, "automation")
        dataDate = resolve[0].date_create if resolve[0].date_use is None else resolve[0].date_use
        dataValue = resolve[0].value
        if dataDate is not None and dataValue is not None:
            res = validateMain(str(dataDate), str(dataValue))
            return res
        else:
            return messageError
    except Exception as e:
        print("Error en la conexión:", e)


def validateDataInsert(req):
    try:
        resolve = insertData(req['fecha'], req['token'], 13)
        return resolve
    except Exception as e:
        print("Error en la conexión:", e)


if __name__ == "__main__":
    result = validateData()
    print(result)
