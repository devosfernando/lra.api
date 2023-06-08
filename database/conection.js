const mysql = require("mysql");
const dotenvi = require("dotenv").config();
const querys = require("../database/querys.json");

//FUNCION PARA OBTENER EL QUERY DE LA CLASE
function querySwitch(datos) {
  switch (datos) {
    case 0:
      console.log(`Kpi mes anterior`);
      return querys["kpi"]["prevMonth"]["kpiSql"];
    case 1:
      console.log(`Ejecuciones del mes anterior Atenea`);
      return querys["kpi"]["prevMonth"]["ateneaExecutions"];
    case 2:
      console.log(`Canal Ejecuciones Mes anterior`);
      return querys["kpi"]["prevMonth"]["channelExecutions"];
    case 3:
      console.log(`Kpi mes actual`);
      return querys["kpi"]["lastMonht"]["kpiSql"];
    case 4:
      console.log(`Ejecuciones del ultimo mes Atenea`);
      return querys["kpi"]["lastMonht"]["ateneaExecutions"];
    case 5:
      console.log(`Canal de ejecuciones ultimo mes`);
      return querys["kpi"]["lastMonht"]["channelExecutions"];
    case 6:
      console.log(`Top Transacciones`);
      return querys["top"]["trx"];
    case 7:
      console.log(`Top Transacciones 6 meses`);
      return querys["top"]["trxLasteSixMoth"];
    case 8:
      console.log(`Fecha de ejecuciones mes actual Mainframe vs Ether`);
      return querys["executionsDate"];
    case 9:
      console.log(`Fecha de ejecuciones para el año actual`);
      return querys["kpiYear"];
    case 10:
      console.log(`Parametria para grafica`);
      return querys["parametry"];
    default:
      break;
  }
}

async function prepareConnection(queryf) {
  let datosConexion = mysql.createConnection({
    host: process.env.HOST,
    port: process.env.PORT,
    database: process.env.DATABASE,
    user: process.env.USER,
    password: process.env.PASSWORD,
  });

  return await new Promise((resolve, reject) => {
    datosConexion.connect(function (err) {
      if (err) {
        console.log(`Error de conexion: ${err.stack} `);
        endConection(datosConexion);
      } else {
        console.log(`Datos desde el queryf ${queryf}`);
        let respuesta = querySwitch(queryf);
        console.log(respuesta);

        datosConexion.query(querySwitch(queryf), (err, result) => {
          if (err) {
            reject(err);
            endConection(datosConexion);
          }
          if (result) {
            resolve(result);
            endConection(datosConexion);
          }
        });
      }
    });
  });
}

async function endConection(datosConexion) {
  // Cierra la conexión
  datosConexion.end(function (error) {
    console.log("Close conection");
  });
}

module.exports = {
  prepareConnection,
};
