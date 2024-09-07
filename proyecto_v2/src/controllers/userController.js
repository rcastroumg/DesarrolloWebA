import User from '../models/userModel.js';

// Obtener todos los usuarios
export const getUsers = async (req, res) => {
  try {
    const users = await User.find();
    res.json(users);
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
};

// Crear un nuevo usuario
export const createUser = async (req, res) => {
  const { name, email } = req.body;

  const newUser = new User({
    name,
    email,
  });

  try {
    const savedUser = await newUser.save();
    res.status(201).json(savedUser);
  } catch (error) {
    res.status(400).json({ message: error.message });
  }
};

// Actualizar un usuario
export const updateUser = async (req, res) => {
  const { id } = req.params;
  const { name, email } = req.body;

  try {
    const updatedUser = await User.findByIdAndUpdate(
      id,
      { name, email },
      { new: true } // Retorna el documento actualizado
    );

    if (!updatedUser) {
      return res.status(404).json({ message: 'Usuario no encontrado' });
    }

    res.json(updatedUser);
  } catch (error) {
    res.status(400).json({ message: error.message });
  }
};

// Eliminar un usuario
export const deleteUser = async (req, res) => {
  const { id } = req.params;

  try {
    const deletedUser = await User.findByIdAndDelete(id);

    if (!deletedUser) {
      return res.status(404).json({ message: 'Usuario no encontrado' });
    }

    res.json({ message: 'Usuario eliminado exitosamente' });
  } catch (error) {
    res.status(400).json({ message: error.message });
  }
};

