const routering = require('express').Router();
const currentHostRunsExecutions = require('../controllers/channelExecution')

routering.get('/prevMonht/channelExecutions',(req,res)=>{
    currentHostRunsExecutions.listarPrevMonht(req,res);
})

routering.get('/lastMonht/channelExecutions',(req,res)=>{
    currentHostRunsExecutions.listarLastMonht(req,res);
})


module.exports = routering