const routering = require('express').Router();
const { validateToken } = require("../jwt/jeisonWebToken");
const currentHostRunsExecutions = require('../controllers/executionsDate')

routering.get('/executionsDate',validateToken,(req,res)=>{
    console.log("Entro por executions date desde endPoint")
    currentHostRunsExecutions.executionDate(req,res);
})

module.exports = routering