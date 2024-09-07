//const { default: mongoose } = require("mongoose");
const mongoose = require("mongoose");

const conexion = async () => {
    try{
        await mongoose.connect("mongodb://127.0.0.1:27017/mi_blog");
        console.log("Conectado correctaente");
        
    } catch (error) {
        console.log(error);
        throw new Error("No se establecio la conexion");
    }
}

module.exports = {
    conexion
}