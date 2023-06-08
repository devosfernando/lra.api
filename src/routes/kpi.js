const routering = require('express').Router();
const currentHostRunsExecutions = require('../controllers/kpi')

routering.get('/prevMonht/kpi',(req,res)=>{
    currentHostRunsExecutions.listarPrevMonht(req,res);
})

routering.get('/lastMonht/kpi',(req,res)=>{
    currentHostRunsExecutions.listarLastMonht(req,res);
})


module.exports = routering