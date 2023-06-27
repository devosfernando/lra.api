var {
    validateData,
    validateDataInsert,
  } = require("../services/tokenServices");
  
  const controlador = {
    listar: {},
  };
  
  controlador.getTokenJira = (req, res) => {
    try {
      validateData()
        .then((resolve) => {
          res.status(200).json({
            status: 200,
            message: "Ok",
            response: resolve,
          });
          console.log(resolve);
        })
        .catch((reject) => {
          res.status(200).json({
            status: 200,
            message: "Ok",
            response: reject,
          });
          console.log(reject);
        });
    } catch (error) {
      res.status(500).json({
        status: 500,
        message: "Internal Server Error",
        response: error,
      });
      console.log(error);
    }
  };
  
  controlador.updateDate = (req, res) => {
    try {
      validateDataInsert(req.body)
        .then((resp) => {
          res.status(200).json({
            status: 200,
            message: "Ok",
            response: resp,
          });
          console.log(resp);
        })
        .catch((err) => {
          res.status(200).json({
            status: 200,
            message: "Ok",
            response: err,
          });
          console.log(err);
        });
    } catch (error) {
      res.status(500).json({
        status: 500,
        message: "Internal Server Error",
        response: error,
      });
      console.log(error);
    }
  };
  
  module.exports = controlador;
  