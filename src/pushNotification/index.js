require("dotenv").config();
let firebase = require("firebase-admin");
const serviceAccount = {
  type: "service_account",
  project_id: process.env.PROJECT_ID,
  private_key_id: process.env.PRIVATE_KEY_ID,
  private_key: process.env.PRIVATE_KEY,
  client_email: process.env.CLIENT_EMAIL,
  client_id: process.env.CLIENT_ID,
  auth_uri: "https://accounts.google.com/o/oauth2/auth",
  token_uri: "https://oauth2.googleapis.com/token",
  auth_provider_x509_cert_url: "https://www.googleapis.com/oauth2/v1/certs",
  client_x509_cert_url: process.env.CLIENT_X509_CERT_URL,
};

firebase.initializeApp({
  credential: firebase.credential.cert(serviceAccount),
});

console.log("PRIVATE_KEY");
console.log(process.env.API_KEY);

async function sendMessageToToken(token, message, notification_options) {
  const data = await firebase
    .messaging()
    .sendToDevice(token, message, notification_options)
    .then((response) => {
      return response;
      //console.log(response)
      //res.status(200).send("Notification sent s;uccessfully");
    })
    .catch((error) => {
      return error;
      //console.log(error);
    });

  return data;
}

async function sendMessageToTopic(topic, message, notification_options) {
  const data = await firebase
    .messaging()
    .sendToTopic(topic, message, notification_options)
    .then((response) => {
      return response;
      //console.log(response)
      //res.status(200).send("Notification sent s;uccessfully");
    })
    .catch((error) => {
      return error;
      //console.log(error);
    });

  return data;
}

module.exports = {
  sendMessageToToken,
  sendMessageToTopic,
};
