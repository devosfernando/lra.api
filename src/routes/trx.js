const routering = require('express').Router();
const currentHostRunsExecutions = require('../controllers/trx')

routering.get('/trx',(req,res)=>{
    currentHostRunsExecutions.listarTrx(req,res);
})

routering.get('/trxLasteSixMoth',(req,res)=>{
    currentHostRunsExecutions.listarSixMonht(req,res);
})

module.exports = routering