const express = require("express");
const bodyParser = require("body-parser");
const app = express();
const router = require('./routes/index')
const dispacher = require("./pushNotification/push")

app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

// Configurar cabeceras y cors
app.use((req, res, next) => {
  res.header('Access-Control-Allow-Origin', '*');
  res.header('Access-Control-Allow-Headers', 'Authorization, X-API-KEY, Origin, X-Requested-With, Content-Type, Accept, Access-Control-Allow-Request-Method');
  res.header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, DELETE');
  res.header('Allow', 'GET, POST, OPTIONS, PUT, DELETE');
  next();
});

app.use('/api/1',router)

app.use('/dispacher',dispacher)

app.get("/",function(req,res){
  //res.redirect('http://plandebackend.ddns.net');
  res.sendFile(__dirname + '/index.html');
})

app.listen(8080,function(){
    console.log("Server started on port 8080")
})

