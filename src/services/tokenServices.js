require("dotenv").config();
const moment = require("moment");
const fetch = require("node-fetch");

var { prepareConnection, insertData } = require("../../database/conection");

const messageError = process.env.MESSAGE_ERROR;
const urlCurl = process.env.URL_CURL

function validateData() {
  return new Promise((resol, reject) => {
    prepareConnection(12, "automation")
      .then((resolve) => {
        //Se resuelve la conexión y trae los datos
        console.log(resolve);
        if (resolve[0].date_use == null && resolve[0].date_create != null) {
          let res = validateMain(resolve[0].date_create, resolve[0].value);
          if (res == false) {
            reject(messageError);
          } else {
            resol(res);
          }
        } else {
          let res = validateMain(resolve[0].date_use, resolve[0].value);
          if (res == false) {
            reject(messageError);
          } else {
            resol(res);
          }
        }
      })
      .catch((reject) => {
        //Error en la conexión
        console.log(reject);
      });
  });
}

function callPython() {
  console.log("ENTRO POR LLAMADO AL PYTHON");
  fetch(urlCurl)
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
    })
    .catch((error) => {
      console.log("Hubo un error:", error);
    });
}

function validateMain(dataDate, dataValue) {
  let resFunction = validateDateAndDate(dataDate);
  if (resFunction != false) {
    //Imprimir valor del token
    //console.log(`Token sirve -> ${resolve[0].VALUE}`);
    return dataValue;
  } else {
    //console.log("Token no sirve ");
    callPython();
    return false;
  }
}

function validateDateAndDate(fecha) {
  const fechaData = moment(fecha, "YYYY-MM-DD HH:mm:ss.SSSSSS");
  const fechaActual = moment();
  const diferenciaEnMinutos = fechaActual.diff(fechaData, "minutes");
  if (diferenciaEnMinutos > 10) {
    console.log(
      "La fechaActual es mayor a 10 minutos que la fecha del token Jira."
      //MANDAR A EJECUTAR LA FUNCIÓN QUE LLAME EL PY
    );
    return false;
  } else {
    console.log(
      "La fechaActual no es mayor a 10 minutos que la fecha del token Jira."
    );
    return true;
  }
}

function validateDataInsert(req) {
  //console.log(req)
  return new Promise((resol, rejec) => {
    insertData(req.fecha, req.token,13)
      .then((resolve) => {
        //Se resuelve la conexión y trae los datos
        //console.log(resolve);
        resol(resolve);
      })
      .catch((reject) => {
        //Error en la conexión
        //console.log(reject);
        rejec(reject);
      });
  });
}

module.exports = { validateData, validateDataInsert };
