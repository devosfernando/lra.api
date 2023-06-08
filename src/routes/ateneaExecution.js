const routering = require('express').Router();
const currentHostRunsExecutions = require('../controllers/ateneaExecution')

routering.get('/prevMonht/ateneaExecution',(req,res)=>{
    currentHostRunsExecutions.listarPrevMonht(req,res);
})

routering.get('/lastMonht/ateneaExecution',(req,res)=>{
    currentHostRunsExecutions.listarLastMonht(req,res);
})

module.exports = routering