// Importar dependencias
const bcrypt = require("bcrypt");
const mongoosePainate = require("mongoose-paginate-v2");


//Importar modelos
const User = require("../models/user");

//Importar servicios
const jwt = require("../services/jwt");

//Acciones de prueba
const pruebaUser = (req, res) => {
    return res.status(200).send({
        message: "Mensaje enviado desde controller/user.js",
        usuario: req.user
    });
};

// Registro de usuarios
const register = async (req, res) => {
    try {
        // Recoger datos de la petición
        let params = req.body;

        // Comprobar que me llegan bien (+validación)
        if (!params.name || !params.email || !params.password || !params.nick) {
            return res.status(400).json({
                status: "error",
                message: "Faltan datos por enviar"
            });
        }

        // Control usuarios duplicados
        const users = await User.find({
            $or: [
                { email: params.email.toLowerCase() },
                { nick: params.nick.toLowerCase() }
            ]
        }).exec();

        if (users && users.length >= 1) {
            return res.status(200).send({
                status: "success",
                message: "El usuario ya existe"
            });
        }

        // Cifrar la contraseña 
        let pwd = await bcrypt.hash(params.password, 10);
        params.password = pwd;

        // Crear objeto de usuario
        let user_to_save = new User(params);

        // Guardar usuario en la BD
        const userStored = await user_to_save.save(); // Eliminar callback, usando await

        // Devolver resultado
        return res.status(200).json({
            status: "success",
            message: "Usuario registrado correctamente",
            user: userStored
        });

    } catch (error) {
        return res.status(500).json({
            status: "error",
            message: "Error en la consulta de usuarios",
            error: error.message
        });
    }
};


const login = async (req, res) => {
    try {
        // Recoger parámetros del body
        let params = req.body;

        if (!params.email || !params.password) {
            return res.status(400).send({
                status: "error",
                message: "Faltan datos por enviar"
            });
        }

        // Buscar en la BD si existe el email o usuario
        const user = await User.findOne({ email: params.email })
            .select({ name: 1, surname: 1, nick: 1, email: 1, role: 1, image: 1, password: 1 })
            .exec();


        if (!user) {
            return res.status(404).send({
                status: "error",
                message: "No existe el usuario"
            });
        }

        // Comprobar la contraseña
        const coincide = await bcrypt.compare(params.password, user.password);
        if (!coincide) {
            return res.status(400).send({
                status: "error",
                message: "Contraseña incorrecta"
            });
        }

        // Si es necesario, aquí puedes generar un token JWT, por ejemplo:
        const token = jwt.createToken(user);

        // const token = jwt.sign({ id: user._id }, 'tu_secreto', { expiresIn: '1h' });

        // Excluir la contraseña antes de devolver los datos del usuario
        user.password = undefined;

        // Devolver los datos del usuario (y el token si usas JWT)
        return res.status(200).send({
            status: "success",
            message: "Login exitoso",
            user: {
                id: user._id,
                name: user.name,
                surname: user.surname,
                nick: user.nick,
                email: user.email,
                role: user.role,
                image: user.image
            },
            token
        });


    } catch (error) {
        return res.status(500).json({
            status: "error",
            message: "Error en el proceso de login",
            error: error.message
        });
    }
};

const profile = async (req, res) => {
    try {
        // Recibir el parámetro del id de usuario por la URL
        const id = req.params.id;

        // Consulta para obtener los datos del usuario, excluyendo password y role
        const userProfile = await User.findById(id)
            .select({ password: 0, role: 0, email: 0 })
            .exec();

        if (!userProfile) {
            return res.status(404).send({
                status: "error",
                message: "El usuario no existe"
            });
        }

        // Devolver la información del usuario
        return res.status(200).send({
            status: "success",
            user: userProfile
        });

    } catch (error) {
        return res.status(500).send({
            status: "error",
            message: "Error al obtener el perfil",
            error: error.message
        });
    }
};


const list = (req, res) => { 
    // Controlar en qué página estamos
    let page = req.params.page ? parseInt(req.params.page) : 1;

    // Número de elementos por página
    const itemsPerPage = 3;

    // Opciones de paginación
    const options = {
        page: page,
        limit: itemsPerPage,
        sort: { _id: 1 }
    };

    // Realizar paginación
    User.paginate({}, options)
        .then((users) => {
            if (!users || users.docs.length === 0) {
                return res.status(404).send({
                    status: "error",
                    message: "No hay usuarios disponibles"
                });
            }

            // Devolver el resultado
            return res.status(200).send({
                status: "success",
                users: users.docs,
                totalDocs: users.totalDocs,
                totalPages: users.totalPages,
                currentPage: users.page,
                itemsPerPage: users.limit,
                hasNextPage: users.hasNextPage,
                hasPrevPage: users.hasPrevPage,
                nextPage: users.nextPage,
                prevPage: users.prevPage
            });
        })
        .catch((error) => {
            return res.status(500).send({
                status: "error",
                message: "Error en la consulta de usuarios",
                error: error.message
            });
        });
};

module.exports = {
    pruebaUser,
    register,
    login,
    profile,
    list
};
