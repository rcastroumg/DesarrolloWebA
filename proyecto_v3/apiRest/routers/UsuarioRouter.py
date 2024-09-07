from fastapi import APIRouter, Depends, HTTPException, status, Request, WebSocket
from fastapi.responses import JSONResponse
from datetime import datetime, timedelta
import time
import json
from schemas.UsuarioSchema import LoginRequest
from models.UsuarioModel import UsuarioModel
from models.ModuloModel import ModuloModel
from models.MenuModel import MenuModel
from models.OpcionModel import OpcionModel
from models.EmpresaModel import EmpresaModel
from models.UsuarioPreguntaModel import UsuarioPreguntaModel
from utils.UsuarioUtil import UsuarioUtil


router = APIRouter(
    prefix="/User",
    tags=["User"],
)

@router.post('/login')
async def login(request:Request):
    try:
        userAgent = request.headers.get("User-Agent")
        #userAgent = websocket.headers.get("User-Agent")
        #ip = f"{request.client.host}:{request.client.port}"    
        #ip = request.headers.get("Origin")
        ip = request.headers.get("X-Forwarded-For", "").split(",")[0]
        #ip = websocket.client.host

        form = await request.form()

        data = form.get("data")
        log = form.get('log')

        dataObject = json.loads(data)
        logObject = json.loads(log)

        model:LoginRequest = LoginRequest(
            IdUsuario=dataObject["IdUsuario"],
            Password=dataObject["Password"]
        )      

        ret = UsuarioModel.BuscarUsuario(model.IdUsuario)    
        if ret is None:
            ret2=UsuarioModel.InsertaBitacora(model.IdUsuario,4,userAgent,ip,"",logObject["os"],logObject["device"],logObject["browser"])
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={
                    "error":True,
                    "mensaje":"Usuario y/o contraseña no son válidos"
                }
            )
        
        if ret["IdStatusUsuario"] != 1:
            UsuarioModel.InsertaBitacora(model.IdUsuario,ret["IdStatusUsuario"],userAgent,ip,"",logObject["os"],logObject["device"],logObject["browser"])
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={
                    "error":True,
                    "mensaje":f"Usuario {ret['Status']}"
                }
            )
        
        empresa = EmpresaModel.ObtenerEmpresaUsuario(model.IdUsuario)[0]
        if ret["Password"] != model.Password:
            # CAMBIAR POR LA CANTIDAD CONFIGURADA DE INTENTOS
            if ret["IntentosDeAcceso"] < (int(empresa["PasswordIntentosAntesDeBloquear"])-1):
                UsuarioModel.ActualizaIntentoSesion(model.IdUsuario)
            else:
                UsuarioModel.ActualizaIntentoSesion(model.IdUsuario)
                UsuarioModel.BloquearUsuario(model.IdUsuario)
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={
                    "error":True,
                    "mensaje":"Usuario y/o contraseña no son válidos"
                }
            )

        if ret["IntentosDeAcceso"] != 0:
            UsuarioModel.ReiniciaIntentoSesion(model.IdUsuario)

        UsuarioModel.InsertaBitacora(model.IdUsuario,1,userAgent,ip,"",logObject["os"],logObject["device"],logObject["browser"])
        UsuarioModel.ActualizaUltimaSesion(model.IdUsuario)
        
        expiresAt = datetime.now() + timedelta(days=1)
        respuesta = {
            "error":False,
            "token":"",
            "expires_at":int(time.mktime(expiresAt.timetuple())) * 1000,
            "id_user":ret["IdUsuario"],
            "user":ret
        }
        return respuesta
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "error":True,
                "mensaje":e
            }
        )


@router.get('/menu/{IdUsuario}')
async def menu(IdUsuario):
    modulos = ModuloModel.ObtenerModulos(IdUsuario)
    menuAll = []

    for modulo in modulos:
        idModulo:int = int(modulo["IdModulo"])
        menus = MenuModel.ObtenerMenus(IdUsuario,idModulo)

        menuLst = []

        for menu in menus:
            idMenu = int(menu["IdMenu"])
            opciones = OpcionModel.ObtenerOpciones(IdUsuario,idModulo,idMenu)

            menus_obj = {
                "id":menu["IdMenu"],
                "nombre":menu["Menu"],
                "submenu":opciones
            }

            menuLst.append(menus_obj)

        modulos_obj = {
            "id":modulo["IdModulo"],
            "nombre":modulo["Nombre"],
            "submenu":menuLst
        }

        menuAll.append(modulos_obj)
    
    return {
        "error":False,
        "opciones":menuAll
    }


@router.post("/recover")
async def recover(request:Request):
    form = await request.form()

    data = form.get("data")
    dataObject = json.loads(data)

    model:LoginRequest = LoginRequest(
        IdUsuario=dataObject["IdUsuario"],
        Password=""
    )

    ret = UsuarioModel.BuscarUsuario(model.IdUsuario)    
    if ret is None:        
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "error":True,
                "mensaje":"El usuario proporcionado no existe en nuestra base de datos"
            }
        )
    
    if ret["IdStatusUsuario"] != 1:        
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "error":True,
                "mensaje":f"Usuario {ret['Status']}"
            }
        )
    
    empresa = EmpresaModel.ObtenerEmpresaUsuario(model.IdUsuario)[0]
    preguntas = UsuarioPreguntaModel.ObtenerTodosUsuarioPregunta(model.IdUsuario,int(empresa['PasswordCantidadPreguntasValidar']))
    if preguntas is None or len(preguntas) == 0:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "error":True,
                "mensaje":f"El usuario proporcionado no tiene metodos de recuperación. Consulte con el administrador del sistema"
            }
        )
    
    return preguntas


@router.post('/valida_pregunta')
async def valida_pregunta(request: Request):
    form = await request.form()

    data = form.get("data")
    dataObject = json.loads(data)
    
    model:LoginRequest = LoginRequest(
        IdUsuario=dataObject["IdUsuario"],
        Password=""
    )

    quest = form.get("question")
    questObject = json.loads(quest)

    preguntasValidas:bool = True

    for numTest in questObject:
        idpregunta = str(numTest).replace("pregunta","")
        respuesta = UsuarioPreguntaModel.obtenerRespuesta(model.IdUsuario,int(idpregunta))
        respuestaBase = respuesta[0]["Respuesta"].upper()
        respuestaUser = str(questObject[numTest]).upper()
        # Quitar acentos

        if respuestaBase != respuestaUser:
            preguntasValidas = False

    if preguntasValidas == False:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "error":True,
                "mensaje":f"Las respuestas no coinciden"
            }
        )
    
    return preguntasValidas


@router.post("/cambiar_contrasena")
async def cambiar_contrasena(request:Request):
    form = await request.form()

    data = form.get("data")
    dataObject = json.loads(data)
    
    model:LoginRequest = LoginRequest(
        IdUsuario=dataObject["IdUsuario"],
        Password=""
    )

    passwords = form.get("pass")
    passwordsObject = json.loads(passwords)

    if passwordsObject["Password"] != passwordsObject["ConfirmPassword"]:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "error":True,
                "mensaje":f"La contraseña no coincide"
            }
        )
    
    isValid = UsuarioUtil.validarPassword(passwordsObject["Password"],model.IdUsuario)
    if isValid == False:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "error":True,
                "mensaje":f"La contraseña no cumple con las características necesarias"
            }
        )
    
    UsuarioModel.CambiarContrasena(model.IdUsuario,passwordsObject["Password"]) 
    
    ret = UsuarioModel.BuscarUsuario(model.IdUsuario)
    UsuarioModel.ActualizaUltimaSesion(model.IdUsuario)
        
    respuesta = {
        "error":False,
        "token":"",
        "expires_at":"",
        "id_user":ret["IdUsuario"],
        "user":ret
    }
    return respuesta
        


