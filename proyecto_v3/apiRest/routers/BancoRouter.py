from fastapi import APIRouter
from fastapi.responses import JSONResponse
import json
from models.BancoModel import BancoModel
from schemas.BancoSchema import *

router = APIRouter(
    prefix="/banco",
    #tags=["Banco"],
)

# Bancos
routerBanco = APIRouter(
    tags=["Bancos"],
)

@routerBanco.get('/bancos')
async def bancos_get():
    bancos = BancoModel.ObtenerTodosBancos()
    return bancos

@routerBanco.put("/bancos/{IdUsuario}")
async def bancos_put(IdUsuario,model:BancoRequest):
    BancoModel.InsertarBanco(model,IdUsuario)
    return

@routerBanco.delete("/bancos/{IdBanco}")
async def bancos_delete(IdBanco):
    ret = BancoModel.EliminarBanco(IdBanco)
    return ret

@routerBanco.post("/bancos/{IdUsuario}/{IdBanco}")
async def bancos_post(IdUsuario,IdBanco,model:BancoRequest):
    ret = BancoModel.ActualizarBanco(model,IdUsuario,IdBanco)
    return ret


router.include_router(routerBanco)