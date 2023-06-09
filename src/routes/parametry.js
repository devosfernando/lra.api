const routering = require('express').Router();
const { validateToken } = require("../jwt/jeisonWebToken");
const parametry = require('../controllers/parametry')

routering.get('/parametry',validateToken,(req,res)=>{
    parametry.listarParametry(req,res);
})

routering.get('/parametry/data',(req,res)=>{
    parametry.getParametryFront(req,res);
})

module.exports = routering