const { conexion } = require("./database/conection.js");
const express = require("express");
const cors = require("cors");

// Iniciar la APP
console.log("Mi api res arrancada");

// inicia la BD
conexion();


const app = express();
const puerto = 3390;

app.use(cors());

app.use(express.json());

app.listen(puerto,()=>{
    console.log("servidor corriendo");
    
});

app.get("/prueba",(req,res) => {
    return res.status(200).send(`
        <h1>Probando nuestra ruta</h1>
        `);
})