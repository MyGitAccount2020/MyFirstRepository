const { connect } = require("mongoose");
const uri="mongodb://localhost:27017"
//const uri = "mongodb://g:Atul@1234@cluster0.enc77.mongodb.net/brillio-db?retryWrites=true&w=majority"

connect(uri)
    .then(() => console.log("Connected"))
    .catch(console.log)