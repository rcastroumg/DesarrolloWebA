from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ModuloRequest(BaseModel):
    Nombre:str
    OrdenMenu:int


class MenuRequest(BaseModel):
    IdModulo:int
    Nombre:str
    OrdenMenu:int


class OpcionRequest(BaseModel):
    IdMenu:int
    Nombre:str
    OrdenMenu:int
    Pagina:str


class RoleRequest(BaseModel):
    Nombre:str


class RoleOpcionRequest(BaseModel):
    IdRole:int
    IdOpcion:int
    Alta:int
    Baja:int
    Cambio:int
    Imprimir:int
    Exportar:int

class UsuarioNuevoRequest(BaseModel):
    UsuarioNuevo:str
    Nombre:str
    Apellido:str
    FechaNacimiento:datetime
    IdStatusUsuario:int
    IdGenero:int
    IdSucursal:int
    TelefonoMovil:str
    CorreoElectronico:str
    Password:str
    #Fotografia:str


class UsuarioRequest(BaseModel):
    IdUsuario:str
    Nombre:str
    Apellido:str
    FechaNacimiento:datetime
    IdStatusUsuario:int
    IdGenero:int
    IdSucursal:int
    TelefonoMovil:str
    CorreoElectronico:str
    Password:str
    Fotografia:Optional[str]
    UltimaFechaIngreso: Optional[str]
    IntentosDeAcceso:Optional[int]
    UltimaFechaCambioPassword: Optional[str]
    RequiereCambiarPassword:Optional[int]


class UsuarioRoleRequest(BaseModel):
    IdUsuario:str
    IdRole:int


class EmpresaRequest(BaseModel):
    Nombre:str
    Direccion:str
    Nit:str
    PasswordCantidadMayusculas:int
    PasswordCantidadMinusculas:int
    PasswordCantidadCaracteresEspeciales:int
    PasswordCantidadCaducidadDias:int
    PasswordLargo:int
    PasswordIntentosAntesDeBloquear:int
    PasswordCantidadNumeros:int
    PasswordCantidadPreguntasValidar:int


class SucursalRequest(BaseModel):
    Nombre:str
    Direccion:str
    IdEmpresa:int


class GeneroRequest(BaseModel):
    Nombre:str


class StatusUsuarioRequest(BaseModel):
    Nombre:str