from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
import json
from models.EstadoCivilModel import EstadoCivilModel
from models.TipoDocumentoModel import TipoDocumentoModel
from models.DepartamentoModel import DepartamentoModel
from models.PuestoModel import PuestoModel
from models.DocumentosPersonaModel import DocumentosPersonaModel
from schemas.RRHHSchema import *



router = APIRouter(
    prefix="/rrhh",
    #tags=["RRHH"],
)


# EstadoCivil
routerEstadoCivil = APIRouter(
    tags=["EstadoCivil"],
)

@routerEstadoCivil.get('/estadocivil')
async def estadocivil_get():
    estadocivil = EstadoCivilModel.ObtenerTodosEstadoCivil()
    return estadocivil

@routerEstadoCivil.put("/estadocivil/{IdUsuario}")
async def estadocivil_put(IdUsuario,model:EstadoCivilRequest):
    EstadoCivilModel.InsertarEstadoCivil(model,IdUsuario)
    return

@routerEstadoCivil.delete("/estadocivil/{IdEstadoCivil}")
async def estadocivil_delete(IdEstadoCivil):
    ret = EstadoCivilModel.EliminarEstadoCivil(IdEstadoCivil)
    return ret

@routerEstadoCivil.post("/estadocivil/{IdUsuario}/{IdEstadoCivil}")
async def estadocivil_post(IdUsuario,IdEstadoCivil,model:EstadoCivilRequest):
    ret = EstadoCivilModel.ActualizarEstadoCivil(model,IdUsuario,IdEstadoCivil)

    try:
        error = ret["OOPS"]
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "error": True,
                "mensaje":error
            }
        )
    except:
        return ret



# TipoDocumento
routerTipoDocumento = APIRouter(
    tags=["TipoDocumento"],
)

@routerTipoDocumento.get('/tipodocumento')
async def tipodocumento_get():
    tipodocumento = TipoDocumentoModel.ObtenerTodosTipoDocumento()
    return tipodocumento

@routerTipoDocumento.put("/tipodocumento/{IdUsuario}")
async def tipodocumento_put(IdUsuario,model:TipoDocumentoRequest):
    TipoDocumentoModel.InsertarTipoDocumento(model,IdUsuario)
    return

@routerTipoDocumento.delete("/tipodocumento/{IdTipoDocumento}")
async def tipodocumento_delete(IdTipoDocumento):
    ret = TipoDocumentoModel.EliminarTipoDocumento(IdTipoDocumento)
    return ret

@routerTipoDocumento.post("/tipodocumento/{IdUsuario}/{IdTipoDocumento}")
async def tipodocumento_post(IdUsuario,IdTipoDocumento,model:TipoDocumentoRequest):
    ret = TipoDocumentoModel.ActualizarTipoDocumento(model,IdUsuario,IdTipoDocumento)
    return ret



# Departamento
routerDepartamento = APIRouter(
    tags=["Departamento"],
)

@routerDepartamento.get('/departamento')
async def departamento_get():
    departamento = DepartamentoModel.ObtenerTodosDepartamento()
    return departamento

@routerDepartamento.get('/departamentoporempresa/{idempresa}')
async def departamento_get(idempresa:int):
    departamento = DepartamentoModel.ObtenerDepartamentoPorEmpresa(idempresa)
    return departamento

@routerDepartamento.put("/departamento/{IdUsuario}")
async def departamento_put(IdUsuario,model:DepartamentoRequest):
    DepartamentoModel.InsertarDepartamento(model,IdUsuario)
    return

@routerDepartamento.delete("/departamento/{IdDepartamento}")
async def departamento_delete(IdDepartamento):
    ret = DepartamentoModel.EliminarDepartamento(IdDepartamento)
    return ret

@routerDepartamento.post("/departamento/{IdUsuario}/{IdDepartamento}")
async def departamento_post(IdUsuario,IdDepartamento,model:DepartamentoRequest):
    ret = DepartamentoModel.ActualizarDepartamento(model,IdUsuario,IdDepartamento)
    return ret



# Puesto
routerPuesto = APIRouter(
    tags=["Puesto"],
)

@routerPuesto.get('/puesto')
async def puesto_get():
    puesto = PuestoModel.ObtenerTodosPuesto()
    return puesto

@routerPuesto.get('/puestopordepto/{iddepto}')
async def puesto_get(iddepto:int):
    puesto = PuestoModel.ObtenerPuestoPorDepartamento(iddepto)
    return puesto

@routerPuesto.put("/puesto/{IdUsuario}")
async def puesto_put(IdUsuario,model:PuestoRequest):
    PuestoModel.InsertarPuesto(model,IdUsuario)
    return

@routerPuesto.delete("/puesto/{IdPuesto}")
async def puesto_delete(IdPuesto):
    ret = PuestoModel.EliminarPuesto(IdPuesto)
    return ret

@routerPuesto.post("/puesto/{IdUsuario}/{IdPuesto}")
async def puesto_post(IdUsuario,IdPuesto,model:PuestoRequest):
    ret = PuestoModel.ActualizarPuesto(model,IdUsuario,IdPuesto)
    return ret



# Documento Persona
routerDocumentosPersona = APIRouter(
    tags=["DocumentosPersona"],
)

@routerDocumentosPersona.get('/documentospersona/{idpersona}')
async def documentospersona_get(idpersona):
    documentospersona = DocumentosPersonaModel.ObtenerTodosDocumentosPersona(idpersona  )
    return documentospersona

@routerDocumentosPersona.put("/documentospersona/{IdUsuario}")
async def documentospersona_put(IdUsuario,model:DocumentosPersonaRequest):
    DocumentosPersonaModel.InsertarDocumentosPersona(model,IdUsuario)
    return

@routerDocumentosPersona.delete("/documentospersona/{IdTipoDocuemento}/{IdPersona}")
async def documentospersona_delete(IdTipoDocuemento,IdPersona):
    ret = DocumentosPersonaModel.EliminarDocumentosPersona(IdTipoDocuemento,IdPersona)
    return ret


router.include_router(routerEstadoCivil)
router.include_router(routerTipoDocumento)
router.include_router(routerDepartamento)
router.include_router(routerPuesto)
router.include_router(routerDocumentosPersona)