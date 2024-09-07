import decimal
from fastapi import status
from fastapi.responses import JSONResponse
from schemas.RRHHSchema import PersonaRequest
from schemas.NominaSchemas import *
from models.PersonaModel import PersonaModel
from models.EmpleadoModel import EmpleadoModel
from models.PlanillaCabeceraModel import PlanillaCabeceraModel
from models.PlanillaDetalleModel import PlanillaDetalleModel
from models.PeriodoPlanillaModel import PeriodoPlanillaModel
from models.InasistenciaModel import InasistenciaModel

class NominaUtil:
    def CrearEmpleado(idusuario,model:NuevoEmpleadoRequest):
        persona = PersonaRequest(
            IdPersona=0,
            Nombre=model.Nombre,
            Apellido=model.Apellido,
            FechaNacimiento=model.FechaNacimiento,
            IdGenero=model.IdGenero,
            IdEstadoCivil=model.IdEstadoCivil,
            Direccion=model.Direccion,
            Telefono=model.Telefono,
            CorreoElectronico=model.CorreoElectronico
        )

        try:
            ret = PersonaModel.InsertarPersona(persona,idusuario)
        except Exception as ex:
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={
                    "error":True,
                    "mensaje":str(ex)
                }
            )
        
        if ret is None:
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={
                    "error":True,
                    "mensaje":"Error al crear empleado"
                }
            )

        empleado = EmpleadoRequest(
            IdEmpleado=0,
            IdPersona=ret,
            IdSucursal=model.IdSucursal,
            FechaContratacion=model.FechaContratacion,
            IdPuesto=model.IdPuesto,
            IdStatusEmpleado=model.IdStatusEmpleado,
            IngresoSueldoBase=model.IngresoSueldoBase,
            IngresoBonificacionDecreto=model.IngresoBonificacionDecreto,
            IngresoOtrosIngresos=model.IngresoOtrosIngresos,
            DescuentoIgss=model.DescuentoIgss,
            DescuentoIsr=model.DescuentoIsr,
            DescuentoInasistencias=model.DescuentoInasistencias
        )

        try:
            retEmpl = EmpleadoModel.InsertarEmpleado(empleado,idusuario)            
        except Exception as ex:
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={
                    "error":True,
                    "mensaje":str(ex)
                }
            )

        return retEmpl
    


    def actualizarEmpleado(idusuario,model:EditarEmpleadoRequest):
        persona = PersonaRequest(
            IdPersona=model.IdPersona,
            Nombre=model.Nombre,
            Apellido=model.Apellido,
            FechaNacimiento=model.FechaNacimiento,
            IdGenero=model.IdGenero,
            IdEstadoCivil=model.IdEstadoCivil,
            Direccion=model.Direccion,
            Telefono=model.Telefono,
            CorreoElectronico=model.CorreoElectronico
        )

        try:
            ret = PersonaModel.ActualizarPersona(persona,idusuario)
        except Exception as ex:
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={
                    "error":True,
                    "mensaje":str(ex)
                }
            )
        
        if ret is None:
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={
                    "error":True,
                    "mensaje":"Error al actualizar empleado"
                }
            )

        empleado = EmpleadoRequest(
            IdEmpleado=model.IdEmpleado,
            IdPersona=model.IdPersona,
            IdSucursal=model.IdSucursal,
            FechaContratacion=model.FechaContratacion,
            IdPuesto=model.IdPuesto,
            IdStatusEmpleado=model.IdStatusEmpleado,
            IngresoSueldoBase=model.IngresoSueldoBase,
            IngresoBonificacionDecreto=model.IngresoBonificacionDecreto,
            IngresoOtrosIngresos=model.IngresoOtrosIngresos,
            DescuentoIgss=model.DescuentoIgss,
            DescuentoIsr=model.DescuentoIsr,
            DescuentoInasistencias=model.DescuentoInasistencias
        )

        try:
            retEmpl = EmpleadoModel.ActualizarEmpleado(empleado,idusuario)        
        except Exception as ex:
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={
                    "error":True,
                    "mensaje":str(ex)
                }
            )

        return retEmpl
    


    def CrearPlanilla(usuario,model:PlanillaCabeceraRequest):

        planilla = PlanillaCabeceraModel.BuscarPlanillaCabecera(model.Anio,model.Mes)

        if len(planilla) > 0:
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={
                    "error":True,
                    "mensaje":"Ya existe una planilla para el periodo de la fecha seleccionado"
                }
            )
        
        periodo = PeriodoPlanillaModel.BuscarPeriodoPlanilla(model.Anio,model.Mes)
        if len(periodo) == 0:
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={
                    "error":True,
                    "mensaje":"No existen periodos definidos para la fecha seleccionada"
                }
            )
        
        ret = PlanillaCabeceraModel.InsertarPlanillaCabecera(model,usuario)

        if ret != 0:
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={
                    "error":True,
                    "mensaje":"Hubo un error al crear la planilla"
                }
            )
        
        perido = PeriodoPlanillaModel.BuscarPeriodoPlanilla(model.Anio,model.Mes)[0]
        empleadosContratados = EmpleadoModel.ObtenerEmpleadoContratado()

        IngresoSalario:float = 0
        IngresoBono:float = 0
        IngresoOtros:float = 0
        DescuentoIgss:float = 0
        DescuentoIsr:float = 0
        DescuentoInasistencias:float = 0

        for empleado in empleadosContratados:
            empleadoUnico = EmpleadoModel.ObtenerEmpleadoUnico(empleado["IdEmpleado"])[0]

            IngresoSalario += empleadoUnico["IngresoSueldoBase"]
            IngresoBono += empleadoUnico["IngresoBonificacionDecreto"]
            IngresoOtros += empleadoUnico["IngresoOtrosIngresos"]
            DescuentoIgss += empleadoUnico["DescuentoIgss"]
            DescuentoIsr += empleadoUnico["DescuentoIsr"]
            DescuentoInasistencias += empleadoUnico["DescuentoInasistencias"]

            if empleadoUnico["FechaContratacion"] <= perido["FechaFin"]:
                ret = PlanillaDetalleModel.InsertarPlanillaDetalle(empleadoUnico,model,usuario)

        return

    
    def ReCrearPlanilla(usuario,model:PlanillaCabeceraRequest):
        perido = PeriodoPlanillaModel.BuscarPeriodoPlanilla(model.Anio,model.Mes)[0]

        ret = PlanillaDetalleModel.EliminarPlanillaDetalle(model.Anio,model.Mes)

        empleadosContratados = EmpleadoModel.ObtenerEmpleadoContratado()

        for empleado in empleadosContratados:
            empleadoUnico = EmpleadoModel.ObtenerEmpleadoUnico(empleado["IdEmpleado"])[0]
            if empleadoUnico["FechaContratacion"] <= perido["FechaFin"]:
                ret = PlanillaDetalleModel.InsertarPlanillaDetalle(empleadoUnico,model,usuario)

        PlanillaCabeceraModel.ActualizarFechaCreado(model,usuario)
        return
    

    def calcularEmpleado(anio,mes,IdEmpleado,FechaContratacion,SueldoBase,BonoDecreto,Otros,usuario):
        diasLaborados = NominaUtil.calcularDias(anio,mes,FechaContratacion)

        sueldoPorDia = SueldoBase / 30
        sueldoCalculado = sueldoPorDia * diasLaborados
        bonoPorDia = BonoDecreto / 30
        bonoCalculado = bonoPorDia * diasLaborados

        totalIngresos = round(sueldoCalculado,2)+round(bonoCalculado,2)+round(Otros,2)

        diasInasistencia = NominaUtil.calcularDiasInasistencia(anio,mes,IdEmpleado)

        InasistenciaCalculado = sueldoPorDia * diasInasistencia
        igssCalculado = decimal.Decimal(sueldoCalculado-InasistenciaCalculado) * decimal.Decimal(0.0483)
        # formula de Proyeccion: Sueldo 12 meses - Monto fijo exento (48000) => * %5  => /12
        rentaBruta = (SueldoBase * 12) + (BonoDecreto * 12)
        rentaNeta = (rentaBruta - 48000 - (igssCalculado * 12))
        if rentaNeta > 0:
            isrCalculado = (rentaNeta * decimal.Decimal(0.05) ) / 12
        else:
            isrCalculado = 0

        totalDescuentos = round(InasistenciaCalculado,2) + round(igssCalculado,2) + round(isrCalculado,2)

        params = {
            "IdEmpleado": IdEmpleado,
            "IngresoSueldoBase": round(sueldoCalculado,2),
            "IngresoBonificacionDecreto": round(bonoCalculado,2),
            "IngresoOtrosIngresos": round(Otros,2),
            "DescuentoIgss": round(igssCalculado,2),            
            "DescuentoIsr": round(isrCalculado,2),            
            "DescuentoInasistencias": round(InasistenciaCalculado,2),            
            "TotalIngresos": round(totalIngresos,2),            
            "TotalDescuentos": round(totalDescuentos,2),    
            "SalarioNeto": totalIngresos - totalDescuentos        
        }
        ret = PlanillaDetalleModel.ActualizarPlanillaDetalle(params,anio,mes,usuario)
        return
    
    def calcularDias(anio,mes,FechaContratacion):
        diasPeriodo = 30
        periodo = PeriodoPlanillaModel.BuscarPeriodoPlanilla(anio,mes)[0]
        fini = periodo["FechaInicio"]
        fend = periodo["FechaFin"]
        fempl = FechaContratacion

        if fempl >= fini and fempl <= fend:
            dias = diasPeriodo - (fempl - fini).days
            return dias
        else:
            return diasPeriodo
        

    def calcularDiasInasistencia(anio,mes,IdEmpleado):
        periodo = PeriodoPlanillaModel.BuscarPeriodoPlanilla(anio,mes)[0]
        inasistencias = InasistenciaModel.BuscaInasistenciaEmpleado(periodo,IdEmpleado)

        dias = 0
        if(len(inasistencias) > 0):
            for inasistencia in inasistencias:
                dias += (inasistencia["FechaFinal"]-inasistencia["FechaInicial"]).days + 1

        return dias
        
        

    def CalcularPlanilla(usuario,model:PlanillaCabeceraRequest):

        empleados = PlanillaDetalleModel.ObtenerTodosPlanillaDetalle(model.Anio,model.Mes)

        for empleado in empleados:
            empleadoTable = EmpleadoModel.ObtenerEmpleadoUnico(empleado["IdEmpleado"])[0]
            NominaUtil.calcularEmpleado(
                model.Anio,
                model.Mes,
                empleado["IdEmpleado"],
                empleadoTable["FechaContratacion"],
                empleadoTable["IngresoSueldoBase"],
                empleadoTable["IngresoBonificacionDecreto"],
                empleadoTable["IngresoOtrosIngresos"],
                usuario
            )
        PlanillaCabeceraModel.ActualizarFechaCalculo(model,usuario)
        return


    def PagarPlanilla(usuario,model:PlanillaCabeceraRequest):
        PlanillaCabeceraModel.ActualizarFechaPagado(model,usuario)