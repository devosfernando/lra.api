var { prepareConnection } = require("../../database/conection");

const controlador = {
  listar: {},
};

controlador.listarLastMonht = (req, res) => {

  prepareConnection(4)
    .then((resolve) => {
      res.status(200).json({
        status: 200,
        message: "Ok",
        response: resolve,
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
};

controlador.listarPrevMonht = (req, res) => {

  prepareConnection(1)
    .then((resolve) => {
      res.status(200).json({
        status: 200,
        message: "Ok",
        response: resolve,
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
};

module.exports = controlador;