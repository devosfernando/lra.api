const routering = require('express').Router();
const { validateToken } = require("../jwt/jeisonWebToken");
const yearKpi = require('../controllers/yearKpi')

routering.get('/year',validateToken,(req,res)=>{
    console.log("Entro por ejecuciones para el año actual")
    yearKpi.kpiYear(req,res);
})

module.exports = routering