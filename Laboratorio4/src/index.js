//Importar dependencias
const {connection} = require("./database/connection.js");
const express = require("express");
const cors = require("cors");

//Inicializar la APP
console.log("APP de Red Social arrancada");

//Conectar a la BD
connection();

//Crear servidor NODE
const app = express();
const puerto = 4000;

//Configurar cors
app.use(cors());


//Convertir los datos de body a objetos js
app.use(express.json());
app.use(express.urlencoded({extended:true}));


//Cartar conf rutas
const UserRoutes = require("./routes/user.js");
const PublicationRoutes = require("./routes/publication.js");
const FollowRoutes = require("./routes/follow.js");

app.use("/api/user", UserRoutes);
app.use("/api/user", PublicationRoutes);
app.use("/api/user", FollowRoutes);


//Ruta de prueba
app.get("/ruta-prueba", (req,res) =>{
    return res.status(200).json(
        {
        "id": 1,
        "nombre": "Carlos Arias",
        "web": "www.chanosbusiness.com.gt"
        }
    );
});

//Poner servidor a escuchar peticiones Http
app.listen(puerto,() =>{
    console.log("Servidor de node corriendo en el puerto:  ", puerto);
});