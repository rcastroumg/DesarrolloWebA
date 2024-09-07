from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
import json
from models.StatusEmpleadoModel import StatusEmpleadoModel
from models.InasistenciaModel import InasistenciaModel
from models.PeriodoPlanillaModel import PeriodoPlanillaModel
from models.EmpleadoModel import EmpleadoModel
from models.CuentaBancariaEmpleadoModel import CuentaBancariaEmpleadoModel
from models.PlanillaCabeceraModel import PlanillaCabeceraModel
from models.PlanillaDetalleModel import PlanillaDetalleModel
from schemas.NominaSchemas import *
from utils.NominaUtil import NominaUtil


router = APIRouter(
    prefix="/nomina",
    #tags=["Nomina"],
)



# StatusEmpleado
routerStatusEmpleado = APIRouter(
    tags=["StatusEmpleado"],
)

@routerStatusEmpleado.get('/statusempleado')
async def statusempleado_get():
    statusempleado = StatusEmpleadoModel.ObtenerTodosStatusEmpleado()
    return statusempleado

@routerStatusEmpleado.put("/statusempleado/{IdUsuario}")
async def statusempleado_put(IdUsuario,model:StatusEmpleadoRequest):
    StatusEmpleadoModel.InsertarStatusEmpleado(model,IdUsuario)
    return

@routerStatusEmpleado.delete("/statusempleado/{IdStatusEmpleado}")
async def statusempleado_delete(IdStatusEmpleado):
    ret = StatusEmpleadoModel.EliminarStatusEmpleado(IdStatusEmpleado)
    return ret

@routerStatusEmpleado.post("/statusempleado/{IdUsuario}/{IdStatusEmpleado}")
async def statusempleado_post(IdUsuario,IdStatusEmpleado,model:StatusEmpleadoRequest):
    ret = StatusEmpleadoModel.ActualizarStatusEmpleado(model,IdUsuario,IdStatusEmpleado)
    return ret



# Inasistencia
routerInasistencia = APIRouter(
    tags=["Inasistencia"],
)

@routerInasistencia.get('/inasistencia')
async def inasistencia_get():
    inasistencia = InasistenciaModel.ObtenerTodosInasistencia()
    return inasistencia

@routerInasistencia.put("/inasistencia/{IdUsuario}")
async def inasistencia_put(IdUsuario,model:InasistenciaRequest):
    if(model.FechaInicial.month != model.FechaFinal.month):
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "error":True,
                "mensaje":f"La fecha inicial y final deben ser del mismo mes"
            }
        )
    
    traslapes = InasistenciaModel.BuscaTraslape(model)
    if(len(traslapes) > 0):
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "error":True,
                "mensaje":f"El registro se traslapa con la inasistencia { traslapes[0]['IdInasistencia'] }"
            }
        )
    
    InasistenciaModel.InsertarInasistencia(model,IdUsuario)
    return

@routerInasistencia.delete("/inasistencia/{IdInasistencia}")
async def inasistencia_delete(IdInasistencia):
    ret = InasistenciaModel.EliminarInasistencia(IdInasistencia)
    return ret

@routerInasistencia.post("/inasistencia/{IdUsuario}/{IdInasistencia}")
async def inasistencia_post(IdUsuario,IdInasistencia,model:InasistenciaRequest):
    ret = InasistenciaModel.ActualizarInasistencia(model,IdUsuario,IdInasistencia)
    return ret



# PeriodoPlanilla
routerPeriodoPlanilla = APIRouter(
    tags=["PeriodoPlanilla"],
)

@routerPeriodoPlanilla.get('/periodoplanilla')
async def periodoplanilla_get():
    periodoplanilla = PeriodoPlanillaModel.ObtenerTodosPeriodoPlanilla()
    return periodoplanilla

@routerPeriodoPlanilla.put("/periodoplanilla/{IdUsuario}")
async def periodoplanilla_put(IdUsuario,model:PeriodoPlanillaRequest):
    count = 1
    for _ in range(model.Cantidad): 
        model.Mes = count       
        PeriodoPlanillaModel.InsertarPeriodoPlanilla(model,IdUsuario)
        count = count + 1
    return

@routerPeriodoPlanilla.delete("/periodoplanilla/{Anio}/{Mes}")
async def periodoplanilla_delete(Anio:int,Mes:int):
    ret = PeriodoPlanillaModel.EliminarPeriodoPlanilla(Anio,Mes)
    return ret

#@routerPeriodoPlanilla.post("/periodoplanilla/{IdUsuario}/{IdPeriodoPlanilla}")
#async def periodoplanilla_post(IdUsuario,IdPeriodoPlanilla,model:PeriodoPlanillaRequest):
#    ret = PeriodoPlanillaModel.ActualizarPeriodoPlanilla(model,IdUsuario,IdPeriodoPlanilla)
#    return ret



# Empleado
routerEmpleado = APIRouter(
    tags=["Empleado"],
)

@routerEmpleado.get('/empleado')
async def empleado_get():
    empleado = EmpleadoModel.ObtenerTodosEmpleado()
    return empleado

@routerEmpleado.get('/empleado/{idempleado}')
async def empleadocontratado_get(idempleado):
    empleado = EmpleadoModel.ObtenerEmpleadoUnico(idempleado)[0]
    return empleado

@routerEmpleado.get('/empleadocontratado')
async def empleadocontratado_get():
    empleado = EmpleadoModel.ObtenerEmpleadoContratado()
    return empleado

@routerEmpleado.put('/empleado/{idusuario}')
async def empleado_put(idusuario,model:NuevoEmpleadoRequest):
    return NominaUtil.CrearEmpleado(idusuario,model)

@routerEmpleado.post('/empleado/{idusuario}/{idempleado}')
async def empleado_post(idusuario,idempleado,model:EditarEmpleadoRequest):
    return NominaUtil.actualizarEmpleado(idusuario,model)


# Cuenta Bancaria Empleado
routerCuentaBancariaEmpleado = APIRouter(
    tags=["CuentaBancariaEmpleado"],
)

@routerCuentaBancariaEmpleado.get('/cuentabancariaempleado/{idempelado}')
async def cuentabancariaempleado_get(idempelado):
    cuentabancariaempleado = CuentaBancariaEmpleadoModel.ObtenerTodosCuentaBancariaEmpleado(idempelado  )
    return cuentabancariaempleado

@routerCuentaBancariaEmpleado.put("/cuentabancariaempleado/{IdUsuario}")
async def cuentabancariaempleado_put(IdUsuario,model:CuentaBancariaEmpleadoRequest):
    CuentaBancariaEmpleadoModel.InactivarUltimaCuentaBancaria(model.IdEmpleado)
    CuentaBancariaEmpleadoModel.InsertarCuentaBancariaEmpleado(model,IdUsuario)
    return

@routerCuentaBancariaEmpleado.delete("/cuentabancariaempleado/{idcuenta}")
async def cuentabancariaempleado_delete(idcuenta):
    ret = CuentaBancariaEmpleadoModel.EliminarCuentaBancariaEmpleado(idcuenta)
    return ret



# Planilla Cabecera
routerPlanillaCabecera = APIRouter(
    tags=["PlanillaCabecera"],
)

@routerPlanillaCabecera.get('/planillacabecera')
async def planillacabecera_get():
    planillacabecera = PlanillaCabeceraModel.ObtenerTodosPlanillaCabecera()
    return planillacabecera

@routerPlanillaCabecera.get('/planillacabecera/{anio}/{mes}')
async def planillacabecera_get(anio,mes):
    planillacabecera = PlanillaCabeceraModel.BuscarPlanillaCabecera(anio,mes)[0]
    return planillacabecera

@routerPlanillaCabecera.put("/planillacabecera/{IdUsuario}")
async def planillacabecera_put(IdUsuario,model:PlanillaCabeceraRequest):
    return NominaUtil.CrearPlanilla(IdUsuario,model)

@routerPlanillaCabecera.delete("/planillacabecera/{anio}/{mes}")
async def planillacabecera_delete(anio,mes):
    planilla = PlanillaCabeceraModel.BuscarPlanillaCabecera(anio,mes)

    if(len(planilla) == 0):
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "error":True,
                "mensaje":"Planilla no encontrada'"
            }
        )
    plan = planilla[0]
    if not plan["FechaHoraCalculada"] is None:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "error":True,
                "mensaje":"Solo se puede eliminar planillas en Estado 'Creado'"
            }
        )
    retDet = PlanillaDetalleModel.EliminarPlanillaDetalle(anio,mes)
    ret = PlanillaCabeceraModel.EliminarPlanillaCabecera(anio,mes)
    return ret



# Planilla Detalle
routerPlanillaDetalle = APIRouter(
    tags=["PlanillaDetalle"],
)

@routerPlanillaDetalle.get('/planilladetalle/{anio}/{mes}')
async def planilladetalle_get(anio,mes):
    planilladetalle = PlanillaDetalleModel.ObtenerTodosPlanillaDetalle(anio,mes)
    return planilladetalle

@routerPlanillaDetalle.post('/planilladetalle/crear/{IdUsuario}')
async def planilladetalle_post(IdUsuario,model:PlanillaCabeceraRequest):
    return NominaUtil.ReCrearPlanilla(IdUsuario,model)

@routerPlanillaDetalle.post('/planilladetalle/calcular/{IdUsuario}')
async def planilladetalle_post(IdUsuario,model:PlanillaCabeceraRequest):
    return NominaUtil.CalcularPlanilla(IdUsuario,model)

@routerPlanillaDetalle.post('/planilladetalle/pagar/{IdUsuario}')
async def planilladetalle_post(IdUsuario,model:PlanillaCabeceraRequest):
    return NominaUtil.PagarPlanilla(IdUsuario,model)



router.include_router(routerStatusEmpleado)
router.include_router(routerInasistencia)
router.include_router(routerPeriodoPlanilla)
router.include_router(routerEmpleado)
router.include_router(routerCuentaBancariaEmpleado)
router.include_router(routerPlanillaCabecera)
router.include_router(routerPlanillaDetalle)