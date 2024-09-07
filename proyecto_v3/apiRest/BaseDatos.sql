drop schema if exists Nomina;

create schema if not exists Nomina;

use Nomina;

create table empresa(
    IdEmpresa int not null auto_increment,
    Nombre varchar(100) not null,
    Direccion varchar(200) not null,
    Nit varchar(20) not null,
    PasswordCantidadMayusculas int,
    PasswordCantidadMinusculas int,
    PasswordCantidadCaracteresEspeciales int,
    PasswordCantidadCaducidadDias int,
    PasswordLargo int,
    PasswordIntentosAntesDeBloquear int,
    PasswordCantidadNumeros int,
    PasswordCantidadPreguntasValidar int,
    FechaCreacion datetime not null,
    UsuarioCreacion varchar(100) not null,
    FechaModificacion datetime,
    UsuarioModificacion varchar(100),
    primary key (IdEmpresa)
);

INSERT INTO empresa (
Nombre, Direccion, Nit, PasswordCantidadMayusculas,
PasswordCantidadMinusculas, PasswordCantidadCaracteresEspeciales,
PasswordCantidadCaducidadDias, PasswordLargo,
PasswordIntentosAntesDeBloquear, PasswordCantidadNumeros,
PasswordCantidadPreguntasValidar, FechaCreacion,
UsuarioCreacion, FechaModificacion, UsuarioModificacion
)
VALUES (
'Software Inc.', 'San Jose Pinula, Guatemala', '12345678-9', 1,
1, 1, 60, 8,
5, 2, 1, NOW(),
'system', NULL, NULL
);

select * from empresa e ;


create table sucursal(
    IdSucursal int not null auto_increment,
    Nombre varchar(100) not null,
    Direccion varchar(200) not null,
    IdEmpresa int not null,
    FechaCreacion datetime not null,
    UsuarioCreacion varchar(100) not null,
    FechaModificacion datetime,
    UsuarioModificacion varchar(100),
    primary key (IdSucursal),
    foreign key (IdEmpresa) references empresa(IdEmpresa)
);

INSERT INTO sucursal (
Nombre, Direccion, IdEmpresa, FechaCreacion,
UsuarioCreacion, FechaModificacion, UsuarioModificacion
)
VALUES (
'Oficinas Centrales', 'San Jose Pinula, Guatemala', 1, NOW(),
'system', NULL, NULL
);

select * from sucursal s ;


create table status_usuario(
    IdStatusUsuario int not null auto_increment,
    Nombre varchar(100) not null,
    FechaCreacion datetime not null,
    UsuarioCreacion varchar(100) not null,
    FechaModificacion datetime,
    UsuarioModificacion varchar(100),
    primary key (IdStatusUsuario)
);

INSERT INTO status_usuario (
Nombre, FechaCreacion, UsuarioCreacion,
FechaModificacion, UsuarioModificacion
)
VALUES
('Activo', NOW(), 'system', NULL, NULL),
('Bloqueado por intentos de acceso', NOW(), 'system', NULL, NULL),
('Inactivo', NOW(), 'system', NULL, NULL);

select * from status_usuario su ;


create table genero(
    IdGenero int not null auto_increment,
    Nombre varchar(100) not null,
    FechaCreacion datetime not null,
    UsuarioCreacion varchar(100) not null,
    FechaModificacion datetime,
    UsuarioModificacion varchar(100),
    primary key (IdGenero)
);

INSERT INTO genero (
Nombre, FechaCreacion, UsuarioCreacion,
FechaModificacion, UsuarioModificacion
)
VALUES
('Masculino', NOW(), 'system', NULL, null),
('Femenino', NOW(), 'system', NULL, null);

select * from genero g ;


create table usuario(
    IdUsuario varchar(100) not null,
    Nombre varchar(100) not null,
    Apellido varchar(100) not null,
    FechaNacimiento date not null,
    IdStatusUsuario int not null,
    Password varchar(100) not null,
    IdGenero int not null,
    UltimaFechaIngreso datetime,
    IntentosDeAcceso int,
    SesionActual varchar(100),
    UltimaFechaCambioPassword datetime,
    CorreoElectronico varchar(100),
    RequiereCambiarPassword int,
    Fotografia mediumblob,
    TelefonoMovil varchar(30),
    IdSucursal int not null,
    FechaCreacion datetime not null,
    UsuarioCreacion varchar(100) not null,
    FechaModificacion datetime,
    UsuarioModificacion varchar(100),
    primary key (IdUsuario),
    foreign key (IdStatusUsuario) references status_usuario(IdStatusUsuario),
    foreign key (IdGenero) references genero(IdGenero),
    foreign key (IdSucursal) references sucursal(IdSucursal)
);

INSERT INTO usuario (
IdUsuario, Nombre, Apellido, FechaNacimiento, IdStatusUsuario,
Password, IdGenero, UltimaFechaIngreso, IntentosDeAcceso,
SesionActual, UltimaFechaCambioPassword, CorreoElectronico,
RequiereCambiarPassword, Fotografia, TelefonoMovil,
IdSucursal, FechaCreacion, UsuarioCreacion,
FechaModificacion, UsuarioModificacion
)
VALUES
/*
('system', 'Nologin', 'Nologin', '1990-05-15', 1,MD5('UMGMaster2023!'), 1, NULL, 0,NULL, NULL, 'system@example.com',1, NULL, '555-1234567',1, NOW(), 'system', NULL, NULL),
('Administrador', 'Administrador', 'IT', '1990-05-15', 1, MD5('ITAdmin'), 1, NULL, 0,NULL, NULL, 'itadmin@example.com',1, NULL, '555-1234567',1, NOW(), 'system', NULL, NULL);
*/
('system', 'Nologin', 'Nologin', '1990-05-15', 1,'Eb50y%INPrSvVw', 1, NULL, 0,NULL, NULL, 'system@example.com',1, NULL, '555-1234567',1, NOW(), 'system', NULL, NULL),
('Administrador', 'Administrador', 'IT', '1990-05-15', 1, '75aVPJO', 1, NULL, 0,NULL, NULL, 'itadmin@example.com',1, NULL, '555-1234567',1, NOW(), 'system', NULL, NULL);

select * from usuario u ;


create table usuario_pregunta(
    IdPregunta int not null auto_increment,
    IdUsuario varchar(100) not null,
    Pregunta varchar(100) not null,
    Respuesta varchar(100) not null,
    OrdenPregunta int not null,
    FechaCreacion datetime not null,
    UsuarioCreacion varchar(100) not null,
    FechaModificacion datetime,
    UsuarioModificacion varchar(100),
    primary key (IdPregunta),
    foreign key (IdUsuario) references usuario(IdUsuario)
);

INSERT INTO usuario_pregunta (
IdUsuario, Pregunta, Respuesta, OrdenPregunta, FechaCreacion,
UsuarioCreacion, FechaModificacion, UsuarioModificacion
)
VALUES (
'Administrador', 'Â¿Nombre de tu primera mascota?', 'Rex', 1, NOW(),
'system', NULL, NULL
),
(
'Administrador', 'Â¿Lugar de nacimiento de tu madre?','Guatemala', 2,
NOW(),
'system', NULL, NULL
),
(
'Administrador', 'Â¿Nombre del catedratico del curso de Analisis de Sistemas II', 'Jorge Lopez', 3, NOW(),'system', NULL, NULL
),
(
'Administrador', 'Â¿Nombre de tu curso preferido?', 'Analisis de Sistemas II', 4, NOW(),'system', NULL, NULL
);

select * from usuario_pregunta up ;


create table role(
    IdRole int not null auto_increment,
    Nombre varchar(50) not null,
    FechaCreacion datetime not null,
    UsuarioCreacion varchar(100) not null,
    FechaModificacion datetime,
    UsuarioModificacion varchar(100),
    primary key (idRole)
);

INSERT INTO role (
Nombre, FechaCreacion, UsuarioCreacion,
FechaModificacion, UsuarioModificacion
)
VALUES
(
'Administrador', NOW(), 'system', NULL, NULL
),
(
'Sin Opciones', NOW(), 'system', NULL, NULL
);

select * from `role` r ;


create table usuario_role(
    IdUsuario varchar(100) not null,
    IdRole int not null,
    FechaCreacion datetime not null,
    UsuarioCreacion varchar(100) not null,
    FechaModificacion datetime,
    UsuarioModificacion varchar(100),
    primary key (IdUsuario, IdRole),
    foreign key (IdUsuario) references usuario(IdUsuario),
    foreign key (IdRole) references role(IdRole)
);

INSERT INTO usuario_role (
IdUsuario, IdRole, FechaCreacion,
UsuarioCreacion, FechaModificacion, UsuarioModificacion
)
VALUES
(
'Administrador', 1, NOW(), 'system', NULL, NULL
),
(
'system', 2, NOW(), 'system', NULL, NULL
);

select * from usuario_role ur ;


create table modulo(
    IdModulo int not null auto_increment,
    Nombre varchar(50) not null,
    OrdenMenu int not null,
    FechaCreacion datetime not null,
    UsuarioCreacion varchar(100) not null,
    FechaModificacion datetime,
    UsuarioModificacion varchar(100),
    primary key (IdModulo)
);

INSERT INTO modulo (
Nombre, OrdenMenu, FechaCreacion, UsuarioCreacion
)
VALUES
(
'Configuración', 1, NOW(), 'system'
),
(
'Planilla', 2, NOW(), 'system'
);

select * from modulo;


create table menu(
    IdMenu int not null auto_increment,
    IdModulo int not null,
    Nombre varchar(50) not null,
    OrdenMenu int not null,
    FechaCreacion datetime not null,
    UsuarioCreacion varchar(100) not null,
    FechaModificacion datetime,
    UsuarioModificacion varchar(100),
    primary key (IdMenu),
    foreign key (IdModulo) references modulo(IdModulo)
);
INSERT INTO menu (
IdModulo, Nombre, OrdenMenu, FechaCreacion, UsuarioCreacion
)
VALUES
(
1, 'Parametros Generales', 1, NOW(), 'system'
),
(
1, 'Menu y accesos', 2, NOW(), 'system'
),
(
1, 'Seguridad', 3, NOW(), 'system'
),
(
1, 'Estadisticas', 4, NOW(), 'system'
),
(
1, 'Procedimientos Almacenados', 5, NOW(), 'system'
);
select * from menu;


create table opcion(
    IdOpcion int not null auto_increment,
    IdMenu int not null,
    Nombre varchar(50) not null,
    OrdenMenu int not null,
    Pagina varchar(100) not null,
    FechaCreacion datetime not null,
    UsuarioCreacion varchar(100) not null,
    FechaModificacion datetime,
    UsuarioModificacion varchar(100),
    primary key (IdOpcion),
    foreign key (IdMenu) references menu(IdMenu)
);

INSERT INTO opcion 
(IdMenu, Nombre, OrdenMenu, Pagina, FechaCreacion, UsuarioCreacion)
VALUES
(1, 'Empresas', 1, 'seguridad/generales/empresa', NOW(), 'system'),
(1, 'Sucursales', 2, 'seguridad/generales/sucursales', NOW(), 'system'),
(1, 'Generos', 3, 'seguridad/generales/generos', NOW(), 'system'),
(1, 'Estatus Usuario', 4, 'seguridad/generales/statususer', NOW(), 'system'),
(2, 'Modulos', 1, 'seguridad/generales/modulos', NOW(), 'system'),
(2, 'Menus', 2, 'seguridad/generales/menus', NOW(), 'system'),
(2, 'Opciones', 3, 'seguridad/generales/opciones', NOW(), 'system'),
(3, 'Usuarios', 1, 'seguridad/generales/usuarios', NOW(), 'system'),
(3, 'Roles', 2, 'seguridad/generales/roles', NOW(), 'system'),
(3, 'Asignar Roles a un Usuario', 3, 'asignacion_role_usuario.php',NOW(), 'system'),
(3, 'Asignar Opciones a un Role', 4, 'asignacion_opcion_role.php',NOW(), 'system');
select * from opcion o ;

create table role_opcion(
    IdRole int not null,
    IdOpcion int not null,
    Alta int not null,
    Baja int not null,
    Cambio int not null,
    Imprimir int not null,
    Exportar int not null,
    FechaCreacion datetime not null,
    UsuarioCreacion varchar(100) not null,
    FechaModificacion datetime,
    UsuarioModificacion varchar(100),
    primary key (IdRole,IdOpcion),
    foreign key (IdRole) references role(IdRole),
    foreign key (IdOpcion) references opcion(IdOpcion)
);
insert into role_opcion
(IdRole,IdOpcion,Alta,Baja,Cambio,Imprimir,Exportar,FechaCreacion,UsuarioCreacion)
VALUES
(1,1,1,1,1,1,1,NOW(),'system'),
(1,2,1,1,1,1,1,NOW(),'system'),
(1,3,1,1,1,1,1,NOW(),'system'),
(1,4,1,1,1,1,1,NOW(),'system'),
(1,5,1,1,1,1,1,NOW(),'system'),
(1,6,1,1,1,1,1,NOW(),'system'),
(1,7,1,1,1,1,1,NOW(),'system'),
(1,8,1,1,1,1,1,NOW(),'system'),
(1,9,1,1,1,1,1,NOW(),'system'),
(1,10,1,1,1,1,1,NOW(),'system'),
(1,11,1,1,1,1,1,NOW(),'system');

create table tipo_acceso(
    IdTipoAcceso int not null auto_increment,
    Nombre varchar(100) not null,
    FechaCreacion datetime not null,
    UsuarioCreacion varchar(100) not null,
    FechaModificacion datetime,
    UsuarioModificacion varchar(100),
    primary key (IdTipoAcceso)
);

INSERT INTO tipo_acceso 
(Nombre, FechaCreacion, UsuarioCreacion,FechaModificacion, UsuarioModificacion)
VALUES
('Acceso Concedido', NOW(), 'system', NULL, NULL),
('Bloqueado - Password incorrecto/Numero de intentos exedidos', NOW(),'system', NULL, NULL),
('Usuario Inactivo', NOW(), 'system', NULL, NULL),
('Usuario ingresado no existe', NOW(), 'system', NULL, NULL);

select * from tipo_acceso ta ;

create table bitacora_acceso(
    IdBitacoraAcceso int not null auto_increment,
    IdUsuario varchar(100) not null,
    IdTipoAcceso int not null,
    FechaAcceso datetime not null,
    HttpUserAgent varchar(200),
    DireccionIp varchar(50),
    Accion varchar(100),
    SistemaOperativo varchar(50),
    Dispositivo varchar(50),
    Browser varchar(50),
    Sesion varchar(100),
    primary key (IdBitacoraAcceso),
    foreign key (IdTipoAcceso) references tipo_acceso(IdTipoAcceso)
);
