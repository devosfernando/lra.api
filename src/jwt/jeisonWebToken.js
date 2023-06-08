const express = require('express')
const app = express();
const jwt = require('jsonwebtoken');
app.use(express.urlencoded({extended:false}))
app.use(express.json())
require('dotenv').config();


function generateAccessToken(user){
    return jwt.sign({user},process.env.API_ACCES_KEY,{expiresIn:'5m'})
}

function validateToken(req,res,next){
    const accessToken = req.headers['authorization'];

    if(!accessToken) res.send('access denied')

    jwt.verify(accessToken,process.env.API_ACCES_KEY,(err,user)=>{
        if(err){
            //res.send('Access denied, token expired or incorrect')
            res.status(400).json({
                status: 400,
                message: "Access denied, token expired or incorrect",
                response: err,
              });
        }else{
            next();
        }
    });
}

async function validarUserDominio(user){
    let dominio = user.substring(user.indexOf("@"))
    if(dominio.toLowerCase() ==="@bbva.com"){
        return await true
    }else{
        return await false
    }
}

module.exports = {
    generateAccessToken,
    validateToken,
    validarUserDominio
}