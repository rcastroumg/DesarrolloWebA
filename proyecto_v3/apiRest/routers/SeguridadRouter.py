from fastapi import APIRouter, Depends, HTTPException, status, Request, UploadFile, Header
from fastapi.responses import JSONResponse
from starlette.datastructures import UploadFile as upFile
import json
from models.ModuloModel import ModuloModel
from models.MenuModel import MenuModel
from models.OpcionModel import OpcionModel
from models.RoleModel import RoleModel
from models.RoleOpcionModel import RoleOpcionModel
from models.UsuarioTableModel import UsuarioTableModel
from models.UsuarioRoleModel import UsuarioRoleModel
from models.StatusUsuarioModel import StatusUsuarioModel
from models.GeneroModel import GeneroModel
from models.SucursalModel import SucursalModel
from models.UsuarioRoleModel import UsuarioRoleModel
from models.EmpresaModel import EmpresaModel
from models.UsuarioPreguntaModel import UsuarioPreguntaModel
from models.BitacoraAccesoModel import BitacoraAccesoModel
#from schemas.SeguridadSchema import ModuloRequest,MenuRequest,OpcionRequest,RoleRequest,RoleOpcionRequest
from schemas.SeguridadSchema import *
from utils.ImagesUtil import ImagesUtil
import utils.Cipher as Cipher

router = APIRouter(
    prefix="/seguridad",
    #tags=["Seguridad"],
)


# GENERALES

# Modulos
routerModulo = APIRouter(
    tags=["Modulos"],
)

@routerModulo.get('/generales/modulos')
async def modulos_get():
    modulos = ModuloModel.ObtenerTodosModulos()
    return modulos

@routerModulo.put("/generales/modulos/{IdUsuario}")
async def modulos_put(IdUsuario,model:ModuloRequest):
    ModuloModel.InsertarModulo(model,IdUsuario)
    return

@routerModulo.delete("/generales/modulos/{IdModulo}")
async def modulos_delete(IdModulo):
    ret = ModuloModel.EliminarModulo(IdModulo)
    return ret

@routerModulo.post("/generales/modulos/{IdUsuario}/{IdModulo}")
async def modulos_post(IdUsuario,IdModulo,model:ModuloRequest):
    ret = ModuloModel.ActualizarModulo(model,IdUsuario,IdModulo)
    return ret



# Menus
routerMenu = APIRouter(
    tags=["Menus"],
)

@routerMenu.get('/generales/menus')
async def menus_get():
    menus = MenuModel.ObtenerTodosMenus()
    return menus

@routerMenu.put("/generales/menus/{IdUsuario}")
async def menus_put(IdUsuario,model:MenuRequest):
    MenuModel.InsertarMenu(model,IdUsuario)
    return

@routerMenu.delete("/generales/menus/{IdMenu}")
async def menus_delete(IdMenu):
    ret = MenuModel.EliminarMenu(IdMenu)
    return ret

@routerMenu.post("/generales/menus/{IdUsuario}/{IdMenu}")
async def menus_post(IdUsuario,IdMenu,model:MenuRequest):
    ret = MenuModel.ActualizarMenu(model,IdUsuario,IdMenu)
    return ret


# Opciones
routerOpcion = APIRouter(
    tags=["Opciones"],
)

@routerOpcion.get('/generales/opciones')
async def opciones_get():
    opciones = OpcionModel.ObtenerTodosOpciones()
    return opciones

@routerOpcion.get('/generales/opciones/buscaruta/{IdUsuario}/{ruta}')
async def opciones_ruta_get(IdUsuario,ruta):
    if(ruta == 'home'):
        return True
    opcionBuscado = OpcionModel.findOpcionByRoute(ruta)[0]
    registro = OpcionModel.tieneAcceso(IdUsuario,opcionBuscado["IdOpcion"])
    try:
        error = registro["OOPS"]
        return False
    except:
        try:
            opcion = registro[0]
            return True
        except:
            return False
        
@routerOpcion.get('/generales/opciones/buscapermisos/{IdUsuario}/{ruta}')
async def opciones_ruta_get(IdUsuario,ruta):
    if(ruta == 'home'):
        return True
    opcionBuscado = OpcionModel.findOpcionByRoute(ruta)[0]
    registro = OpcionModel.tieneAcceso(IdUsuario,opcionBuscado["IdOpcion"])
    try:
        error = registro["OOPS"]
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "error":True,
                "mensaje":"Error al obtener los permisos"
            }
        )
    except:
        try:
            opcion = registro[0]
            return opcion
        except:
            return JSONResponse(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content={
                    "error":True,
                    "mensaje":"No tiene permisos"
                }
        )

@routerOpcion.put("/generales/opciones/{IdUsuario}")
async def opciones_put(IdUsuario,model:OpcionRequest):
    OpcionModel.InsertarOpcion(model,IdUsuario)
    return

@routerOpcion.delete("/generales/opciones/{IdOpcion}")
async def opciones_delete(IdOpcion):
    ret = OpcionModel.EliminarOpcion(IdOpcion)
    try:
        error = ret["OOPS"]
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "error":True,
                "mensaje":error
            }
        )
    except:
        return ret

@routerOpcion.post("/generales/opciones/{IdUsuario}/{IdOpcion}")
async def opciones_post(IdUsuario,IdOpcion,model:OpcionRequest):
    ret = OpcionModel.ActualizarOpcion(model,IdUsuario,IdOpcion)
    return ret


# Roles
routerRole = APIRouter(
    tags=["Roles"],
)

@routerRole.get('/generales/roles/{IdRole}')
async def roles_get(IdRole):
    roles = RoleModel.ObtenerUnicoRole(IdRole)
    return roles[0]

@routerRole.get('/generales/roles')
async def roles_get():
    roles = RoleModel.ObtenerTodosRoles()
    return roles

@routerRole.put("/generales/roles/{IdUsuario}")
async def roles_put(IdUsuario,model:RoleRequest):
    RoleModel.InsertarRole(model,IdUsuario)
    return

@routerRole.delete("/generales/roles/{IdRole}")
async def roles_delete(IdRole):
    ret = RoleModel.EliminarRole(IdRole)
    return ret

@routerRole.post("/generales/roles/{IdUsuario}/{IdRole}")
async def roles_post(IdUsuario,IdRole,model:RoleRequest):
    ret = RoleModel.ActualizarRole(model,IdUsuario,IdRole)
    return ret


# Role-Opciones
routerRoleOpcion = APIRouter(
    tags=["RoleOpciones"],
)

@routerRoleOpcion.get('/generales/rolesopcion/{IdRole}')
async def roles_get(IdRole):
    rolesopcion = RoleOpcionModel.ObtenerTodosRoleOpcion(IdRole)
    return rolesopcion

@routerRoleOpcion.put("/generales/rolesopcion/{IdUsuario}")
async def rolesopcion_put(IdUsuario,model:RoleOpcionRequest):
    RoleOpcionModel.InsertarRoleOpcion(model,IdUsuario)
    return

@routerRoleOpcion.delete("/generales/rolesopcion/{IdRole}/{IdOpcion}")
async def rolesopcion_delete(IdRole,IdOpcion):
    ret = RoleOpcionModel.EliminarRoleOpcion(IdRole,IdOpcion)
    return ret

@routerRoleOpcion.post("/generales/rolesopcion/{IdUsuario}/{IdRole}/{IdOpcion}")
async def rolesopcion_post(IdUsuario,IdRole,IdOpcion,model:RoleOpcionRequest):
    ret = RoleOpcionModel.ActualizarRoleOpcion(model,IdUsuario,IdRole,IdOpcion)
    return ret


# Usuarios
routerUsuario = APIRouter(
    tags=["Usuarios"],
)

#@routerUsuario.get("validar")
def validarPassword(pwd:str, idusuario:str):
    password = Cipher.vigenere_cipher(pwd,"analisisdesistemas","decrypt")
    empresa = EmpresaModel.ObtenerEmpresaUsuario(idusuario)[0]

    indice=0
    mayusculas=0
    minusculas=0
    numeros=0
    especiales=0
    longitud=0

    longitud = len(password)
    while indice < len(password):
        letra = password[indice]
        if letra.isupper() == True:
            mayusculas +=1
        elif letra.islower() == True:
            minusculas +=1
        elif letra.isnumeric() == True:
            numeros += 1
        else:
            especiales += 1
        
        indice += 1

    if (longitud >= empresa["PasswordLargo"] and 
        mayusculas >= empresa["PasswordCantidadMayusculas"] and
        minusculas >= empresa["PasswordCantidadMinusculas"] and
        numeros >= empresa["PasswordCantidadNumeros"] and
        especiales >= empresa["PasswordCantidadCaracteresEspeciales"]):
        return True
    else:
        return False

@routerUsuario.get('/generales/usuarios/{IdUsuarioTable}')
async def usuarios_get(IdUsuarioTable):
    usuarios = UsuarioTableModel.ObtenerUnicoUsuarios(IdUsuarioTable)
    return usuarios[0]

@routerUsuario.get('/generales/usuarios')
async def usuarios_get():
    usuarios = UsuarioTableModel.ObtenerTodosUsuarios()
    return usuarios

@routerUsuario.put("/generales/usuarios/{IdUsuario}")
async def usuarios_put(IdUsuario, request:Request):
    form = await request.form()

    #file = form.get("image0")
    data = form.get("data")
    dataObject = json.loads(data)
    model:UsuarioRequest = UsuarioRequest(
        IdUsuario=dataObject["IdUsuario"],
        Nombre=dataObject["Nombre"],
        Apellido=dataObject["Apellido"],
        FechaNacimiento=dataObject["FechaNacimiento"],
        IdStatusUsuario=dataObject["IdStatusUsuario"],
        IdGenero=dataObject["IdGenero"],
        IdSucursal=dataObject["IdSucursal"],
        TelefonoMovil=dataObject["TelefonoMovil"],
        CorreoElectronico=dataObject["CorreoElectronico"],
        Password=dataObject["Password"],
        Fotografia=dataObject["Fotografia"],
        UltimaFechaIngreso=dataObject["UltimaFechaIngreso"],
        IntentosDeAcceso=dataObject["IntentosDeAcceso"],
        UltimaFechaCambioPassword=dataObject["UltimaFechaCambioPassword"],
        RequiereCambiarPassword=dataObject["RequiereCambiarPassword"]
    )
    
    #if isinstance(file, UploadFile) or isinstance(file, upFile):                
    #    file_name = file.filename
    #    file_content = await file.read()
    #    file_length = len(file_content)
    #    file_content_type = file.content_type     
    #else:
    #    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Instancia de objeto no reconocido")
    #
    #guardar = ImagesUtil.guardarArchivoFisico(file_name,"/usuarios",file_content)
#
    #if(guardar == False):
    #    Exception("Error al guardar archivo")
    #else:
    #    model.Fotografia = "/usuarios/"+file_name
    #    ret = UsuarioTableModel.InsertarUsuarios(model,IdUsuario)
#
    #return ret
    ret = UsuarioTableModel.InsertarUsuarios(model,IdUsuario)
    return ret


@routerUsuario.delete("/generales/usuarios/{IdUsuarioTable}")
async def usuarios_delete(IdUsuarioTable):
    ret = UsuarioTableModel.EliminarUsuarios(IdUsuarioTable)
    return ret

@routerUsuario.post("/generales/usuarios/{IdUsuario}/{IdUsuarioTable}")
async def usuarios_post(IdUsuario,IdUsuarioTable,request:Request):
    form = await request.form()

    #file = form.get("image0")
    data = form.get("data")
    dataObject = json.loads(data)
    model:UsuarioRequest = UsuarioRequest(
        IdUsuario=dataObject["IdUsuario"],
        Nombre=dataObject["Nombre"],
        Apellido=dataObject["Apellido"],
        FechaNacimiento=dataObject["FechaNacimiento"],
        IdStatusUsuario=dataObject["IdStatusUsuario"],
        IdGenero=dataObject["IdGenero"],
        IdSucursal=dataObject["IdSucursal"],
        TelefonoMovil=dataObject["TelefonoMovil"],
        CorreoElectronico=dataObject["CorreoElectronico"],
        Password=dataObject["Password"],
        Fotografia=dataObject["Fotografia"],
        UltimaFechaIngreso=dataObject["UltimaFechaIngreso"],
        IntentosDeAcceso=dataObject["IntentosDeAcceso"],
        UltimaFechaCambioPassword=dataObject["UltimaFechaCambioPassword"],
        RequiereCambiarPassword=dataObject["RequiereCambiarPassword"]
    )

    #ret = UsuarioTableModel.ActualizarUsuarios(model,IdUsuario,IdUsuarioTable)
    #return ret

    passValid = validarPassword(dataObject["Password"],IdUsuarioTable)

    if passValid == True:
        ret = UsuarioTableModel.ActualizarUsuarios(model,IdUsuario,IdUsuarioTable)
        return ret
    else:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "error":True,
                "mensaje":"La contraseña no cumple con las características necesarias"
            }
        )



# Usuario-Roles
routerUsuarioRole = APIRouter(
    tags=["UsuarioRoles"],
)

@routerUsuarioRole.get('/generales/usuarioroles/{IdUsuarioTable}')
async def roles_get(IdUsuarioTable):
    usuarioroles = UsuarioRoleModel.ObtenerTodosUsuarioRole(IdUsuarioTable)
    return usuarioroles

@routerUsuarioRole.put("/generales/usuarioroles/{IdUsuario}")
async def usuarioroles_put(IdUsuario,model:UsuarioRoleRequest):
    UsuarioRoleModel.InsertarUsuarioRole(model,IdUsuario)
    return

@routerUsuarioRole.delete("/generales/usuarioroles/{IdUsuarioTable}/{IdRole}")
async def usuarioroles_delete(IdUsuarioTable,IdRole):
    ret = UsuarioRoleModel.EliminarUsuarioRole(IdUsuarioTable,IdRole)
    return ret



# Status Usuarios
routerStatusUsuario = APIRouter(
    tags=["Status Usuarios"],
)
@routerStatusUsuario.get('/generales/statususuario')
async def statusUsuarios_get():
    statususuario = StatusUsuarioModel.ObtenerStatusUsuario()
    return statususuario

@routerStatusUsuario.put("/generales/statususuario/{IdUsuario}")
async def statususuario_put(IdUsuario,model:StatusUsuarioRequest):
    StatusUsuarioModel.InsertarStatusUsuario(model,IdUsuario)
    return

@routerStatusUsuario.delete("/generales/statususuario/{IdStatusUsuario}")
async def statususuario_delete(IdStatusUsuario):
    ret = StatusUsuarioModel.EliminarStatusUsuario(IdStatusUsuario)
    return ret

@routerStatusUsuario.post("/generales/statususuario/{IdUsuario}/{IdStatusUsuario}")
async def statususuario_post(IdUsuario,IdStatusUsuario,model:StatusUsuarioRequest):
    ret = StatusUsuarioModel.ActualizarStatusUsuario(model,IdUsuario,IdStatusUsuario)
    return ret


# Generos
routerGenero = APIRouter(
    tags=["Generos"],
)
@routerGenero.get('/generales/genero')
async def generos_get():
    genero = GeneroModel.ObtenerGenero()
    return genero

@routerGenero.put("/generales/genero/{IdUsuario}")
async def genero_put(IdUsuario,model:GeneroRequest):
    GeneroModel.InsertarGenero(model,IdUsuario)
    return

@routerGenero.delete("/generales/genero/{IdGenero}")
async def genero_delete(IdGenero):
    ret = GeneroModel.EliminarGenero(IdGenero)
    return ret

@routerGenero.post("/generales/genero/{IdUsuario}/{IdGenero}")
async def genero_post(IdUsuario,IdGenero,model:GeneroRequest):
    ret = GeneroModel.ActualizarGenero(model,IdUsuario,IdGenero)
    return ret


# Sucursales
routerSucursal = APIRouter(
    tags=["Sucursales"],
)
@routerSucursal.get('/generales/sucursal')
async def sucursales_get():
    sucursal = SucursalModel.ObtenerSucursal()
    return sucursal

@routerSucursal.put("/generales/sucursal/{IdUsuario}")
async def sucursal_put(IdUsuario,model:SucursalRequest):
    SucursalModel.InsertarSucursal(model,IdUsuario)
    return

@routerSucursal.delete("/generales/sucursal/{IdSucursal}")
async def sucursal_delete(IdSucursal):
    ret = SucursalModel.EliminarSucursal(IdSucursal)
    return ret

@routerSucursal.post("/generales/sucursal/{IdUsuario}/{IdSucursal}")
async def sucursal_post(IdUsuario,IdSucursal,model:SucursalRequest):
    ret = SucursalModel.ActualizarSucursal(model,IdUsuario,IdSucursal)
    return ret


# Empresa
routerEmpresa = APIRouter(
    tags=['Empresas'],
)
@routerEmpresa.get('/generales/empresa')
async def empresa_get():
    empresa = EmpresaModel.ObtenerTodosEmpresas()
    return empresa

@routerEmpresa.get('/generales/empresausuario/{idusuario}')
async def empresausuario_get(idusuario):
    empresa = EmpresaModel.ObtenerEmpresaUsuario(idusuario)
    return empresa[0]

@routerEmpresa.put("/generales/empresa/{IdUsuario}")
async def empresa_put(IdUsuario,model:EmpresaRequest):
    EmpresaModel.InsertarEmpresa(model,IdUsuario)
    return

@routerEmpresa.delete("/generales/empresa/{IdEmpresa}")
async def empresa_delete(IdEmpresa):
    ret = EmpresaModel.EliminarEmpresa(IdEmpresa)
    return ret

@routerEmpresa.post("/generales/empresa/{IdUsuario}/{IdEmpresa}")
async def empresa_post(IdUsuario,IdEmpresa,model:EmpresaRequest):
    ret = EmpresaModel.ActualizarEmpresa(model,IdUsuario,IdEmpresa)
    return ret


# Usuario Pregunta
routerUsuarioPregunta = APIRouter(
    tags=['Usuario Preguntas'],
)
@routerUsuarioPregunta.get("/generales/usuariopregunta/{IdUsuario}")
async def routerUsuarioPregunta_get(IdUsuario):
    usuariopreguntas = UsuarioPreguntaModel.ObtenerTodosUsuarioPregunta(IdUsuario)
    return usuariopreguntas


# Bitacora Acceso
routerBitacoraAcceso = APIRouter(
    tags=['Bitacora Acceso'],
)
@routerBitacoraAcceso.get("/generales/bitacoraacceso")
async def bitacoraacceso_get():
    bitacoraacceso = BitacoraAccesoModel.ObtenerTodosBitacora()
    return bitacoraacceso


# TEST
routerTesting = APIRouter(
    tags=['Testing'],
)
@routerTesting.get('/')
def index(real_ip: str = Header(None, alias='X-Real-IP')):
    return real_ip

router.include_router(routerModulo)
router.include_router(routerMenu)
router.include_router(routerOpcion)
router.include_router(routerRole)
router.include_router(routerRoleOpcion)
router.include_router(routerUsuario)
router.include_router(routerUsuarioRole)
router.include_router(routerStatusUsuario)
router.include_router(routerGenero)
router.include_router(routerSucursal)
router.include_router(routerEmpresa)
router.include_router(routerUsuarioPregunta)
router.include_router(routerBitacoraAcceso)


router.include_router(routerTesting)