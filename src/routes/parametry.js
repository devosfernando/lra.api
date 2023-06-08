const routering = require('express').Router();
const { validateToken } = require("../jwt/jeisonWebToken");
const parametry = require('../controllers/parametry')

routering.get('/parametry',validateToken,(req,res)=>{
    parametry.listarParametry(req,res);
})

module.exports = routering