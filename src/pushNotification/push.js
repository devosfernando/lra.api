const express = require("express");
const bodyParser = require("body-parser");
const Notification = require("./index");
const router = require("express").Router();
const { prepareConnection } = require("../../database/conection");

router.use(bodyParser.urlencoded({ extended: false }));

router.use(bodyParser.json());

router.post("/notification/token", function (req, res) {
  //res.send("Sending Notification to One user....")

  //kpi.listarLastMonht(req,res)
  prepareConnection(0)
    .then((resolve) => {
      const registrationToken = req.body.registrationToken;
      console.log(registrationToken);
      //const message = req.body.message;

      let respuesta = {
        fecha: resolve[0]["hist_date"].toISOString(),
        kpiEstimado: resolve[0]["hist_kpiEstimado"],
        kpiReal: resolve[0]["hist_kpiReal"],
      };

      const notification_options = {
        priority: "high",
        timeToLive: 60 * 60 * 24,
      };

      const message_notification = {
        notification: {
          title: " \u{1F602} ESTADISTICAS KPI BBVA ",
          body: `Fecha: ${respuesta.fecha.slice(
            0,
            respuesta.fecha.indexOf("T")
          )} 
              Kpi estimado: ${respuesta.kpiEstimado} %
              Kpi real: ${Number(respuesta.kpiReal).toFixed(4)} %
            `,
        },
      };

      resServerMessage(
        registrationToken,
        message_notification,
        notification_options
      );

      res.status(200).json({
        status: 200,
        message: "Ok",
        response: {
          Status: "Sending Notification to One user....",
        },
      });

      console.log(resolve);
    })
    .catch((reject) => {
      res.status(500).json({
        status: 500,
        message: "Internal Server Error",
        response: reject,
      });
      console.log(reject);
    });
});

router.post("/notification/topic", function (req, res) {
  //const message = req.body.message;

  prepareConnection(0)
    .then((resolve) => {
      const registrationTopic = req.body.registrationTopic;
      console.log(registrationTopic);
      //const message = req.body.message;

      let respuesta = {
        fecha: resolve[0]["hist_date"].toISOString(),
        kpiEstimado: resolve[0]["hist_kpiEstimado"],
        kpiReal: resolve[0]["hist_kpiReal"],
        emoji : ""
      };

      const notification_options = {
        priority: "high",
        timeToLive: 60 * 60 * 24,
      };
      

      if(Number(respuesta.kpiReal).toFixed(4) > respuesta.kpiEstimado){
        respuesta.emoji = `\u{1F44F}`
        console.log("Esta con manitos arriba")
      }else if(Number(respuesta.kpiReal).toFixed(4) == respuesta.kpiEstimado){
        respuesta.emoji = `\u{1F603}`
        console.log("Esta feliz") 
      }else if(Number(respuesta.kpiReal).toFixed(4) < respuesta.kpiEstimado){
        console.log("Esta triste") 
        respuesta.emoji = `\u{1F61F}` 
      }

      const message_notification = {
        notification: {
          title:  ` ${respuesta.emoji} ESTADISTICAS KPI BBVA`,
          body: `Fecha: ${respuesta.fecha.slice(
            0,
            respuesta.fecha.indexOf("T")
          )} 
                Kpi estimado: ${Number((respuesta.kpiEstimado)*100).toFixed(2)}%
                Kpi real: ${((Number(respuesta.kpiReal).toFixed(4))*100).toFixed(2)}%
              `,
        },
      };

      resServerMessageTopic(
        registrationTopic,
        message_notification,
        notification_options
      );

      res.status(200).json({
        status: 200,
        message: "Ok",
        response: {
          Status: "Sending Notification to One user....",
        },
      });

      console.log(resolve);
    })
    .catch((reject) => {
      res.status(500).json({
        status: 500,
        message: "Internal Server Error",
        response: reject,
      });
      console.log(reject);
    });
});

async function resServerMessage(tokenOrTopic, message_notification, options) {
  const respuesta = await Notification.sendMessageToToken(
    tokenOrTopic,
    message_notification,
    options
  );
  console.log(respuesta.results[0]);
  console.log(respuesta);
}

async function resServerMessageTopic(
  tokenOrTopic,
  message_notification,
  options
) {
  const respuesta = await Notification.sendMessageToTopic(
    tokenOrTopic,
    message_notification,
    options
  );
  //console.log(respuesta.results[0])
  console.log(respuesta);
}

module.exports = router;
