import express from 'express';
import mongoose from 'mongoose';

const app = express();
const PORT = 3000;

// Middleware para parsear JSON
app.use(express.json());

// Conexión a MongoDB
mongoose.connect('mongodb://localhost:27017/mydatabase')
.then(() => {
  console.log('Conectado a MongoDB');
}).catch((error) => {
  console.error('Error al conectar a MongoDB:', error);
});

// Rutas
import userRoutes from './routes/userRoutes.js';
app.use('/users', userRoutes);

app.listen(PORT, () => {
  console.log(`Servidor corriendo en http://localhost:${PORT}`);
});
