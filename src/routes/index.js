const router = require("express").Router();
const executionAtenea = require("./ateneaExecution");
const channelExecution = require('./channelExecution')
const executionsDate = require('./executionsDate')
const kpi = require('./kpi')
const trx = require('./trx')
const yearKpi = require('./kpiYear')
const parametry = require('./parametry')
const {
  generateAccessToken,
  validateToken,
  validarUserDominio,
} = require("../jwt/jeisonWebToken");



router.use("/kpi", validateToken,executionAtenea);

router.use("/kpi", validateToken,channelExecution);

router.use("/kpi", validateToken,kpi);

router.use("/top", validateToken,trx);

router.use("/kpi",validateToken,yearKpi)

router.use("/kpi",validateToken,parametry)

router.use(executionsDate)

router.post("/auth/securityToken", (req, res) => {
  const { email } = req.body;
  if (email === "" || email == null) {
    res.status(400).json({
      status: 400,
      message: "Bad Request ",
    });
  } else {
    validarUserDominio(email)
      .then((resp) => {
        if (resp) {
          const accessToken = generateAccessToken(email);
          res.header("Authorization", accessToken).json({
            message: "usuario autenticado",
            token: accessToken,
          });
          console.log(accessToken);
        } else {
          res.status(403).json({
            status: 403,
            message: "access denied"
          });
        }
      })
      .catch((error) => {
        res.status(500).json({
          status: 500,
          message: "Internal Server Error",
          response: error,
        });
        console.log(error);
      });
  }
});

module.exports = router;
