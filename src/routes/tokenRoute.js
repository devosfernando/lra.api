const routering = require('express').Router();
const getTokenController = require('../controllers/tokenController')

routering.get('/getToken',(req,res)=>{
    getTokenController.getTokenJira(req,res);
})

routering.post('/update',(req,res)=>{
    getTokenController.updateDate(req,res)
})

module.exports = routering