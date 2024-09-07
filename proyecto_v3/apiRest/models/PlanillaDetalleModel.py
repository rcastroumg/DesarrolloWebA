from repositories.mysql.mysql_db import MySqldb

class PlanillaDetalleModel:
    def ObtenerTodosPlanillaDetalle(anio,mes):
        query = f"""
select 
    a.IdPlanillaDetalle,
    a.Anio,
    a.Mes,
    a.IdEmpleado,
    CONCAT(c.Nombre,' ',c.Apellido) NombreEmpleado,
    a.FechaContratacion,
    a.IdPuesto,
    a.IdStatusEmpleado,
    a.IngresoSueldoBase,
    a.IngresoBonificacionDecreto,
    a.IngresoOtrosIngresos,
    a.DescuentoIgss,
    a.DescuentoIsr,
    a.DescuentoInasistencias,
    a.IngresoSueldoBase+a.IngresoBonificacionDecreto+a.IngresoOtrosIngresos TotalIngresos,
    a.DescuentoIgss+a.DescuentoIsr+a.DescuentoInasistencias TotalDescuentos,
    a.SalarioNeto
from 
    planilla_detalle a,
    empleado b,
    persona c
where
    a.IdEmpleado = b.IdEmpleado 
    and b.IdPersona = c.IdPersona 
    and a.Anio = {anio} 
    and a.Mes = {mes} 
"""
        ret = MySqldb().execute_query(query)
        
        return ret
    

    def InsertarPlanillaDetalle(data,data2,usuario):
        params = [
            {"nombre":"Anio","valor":data2.Anio,},            
            {"nombre":"Mes","valor":data2.Mes,},            
            {"nombre":"IdEmpleado","valor":data["IdEmpleado"],},            
            {"nombre":"FechaContratacion","valor":data["FechaContratacion"],},            
            {"nombre":"IdPuesto","valor":data["IdPuesto"],},            
            {"nombre":"IdStatusEmpleado","valor":data["IdStatusEmpleado"],},            
            {"nombre":"IngresoSueldoBase","valor":data["IngresoSueldoBase"],},            
            {"nombre":"IngresoBonificacionDecreto","valor":data["IngresoBonificacionDecreto"],},            
            {"nombre":"IngresoOtrosIngresos","valor":data["IngresoOtrosIngresos"],},                     
            {"nombre":"SalarioNeto","valor":float(data["IngresoSueldoBase"])+float(data["IngresoBonificacionDecreto"])+float(data["IngresoOtrosIngresos"]),},                     

            {
                "nombre":"UsuarioCreacion",
                "valor":usuario,
            }
        ]
        query = f"""
insert into planilla_detalle
(
    Anio,
    Mes,
    IdEmpleado,
    FechaContratacion,
    IdPuesto,
    IdStatusEmpleado,
    IngresoSueldoBase,
    IngresoBonificacionDecreto,
    IngresoOtrosIngresos,
    DescuentoIgss,
    DescuentoIsr,
    DescuentoInasistencias,
    SalarioNeto,
    FechaCreacion,
    UsuarioCreacion
)
values
(%s,%s,%s,%s,%s,%s,%s,%s,%s,0,0,0,%s,NOW(),%s)
"""
        ret = MySqldb().execute_insert(query,params=params)
        
        return ret
    

    def EliminarPlanillaDetalle(anio,mes):
        query = f"""
delete from planilla_detalle
where 
    Anio = {anio} 
    and Mes = {mes}
"""
        ret = MySqldb().execute_query(query)        
        return ret
    

    def ActualizarPlanillaDetalle(data,anio,mes,usuario):
        params = [
            {"nombre":"IngresoSueldoBase","valor":data["IngresoSueldoBase"],},
            {"nombre":"IngresoBonificacionDecreto","valor":data["IngresoBonificacionDecreto"],},
            {"nombre":"IngresoOtrosIngresos","valor":data["IngresoOtrosIngresos"],},
            {"nombre":"DescuentoIgss","valor":data["DescuentoIgss"],},
            {"nombre":"DescuentoIsr","valor":data["DescuentoIsr"],},
            {"nombre":"DescuentoInasistencias","valor":data["DescuentoInasistencias"],},
            {"nombre":"SalarioNeto","valor":data["SalarioNeto"],},
            {
                "nombre":"UsuarioCreacion",
                "valor":usuario,
            },
            {"nombre":"IdEmpleado","valor":data["IdEmpleado"],},            
            {"nombre":"Anio","valor":anio,},            
            {"nombre":"Mes","valor":mes,},            
        ]
        query = f"""
update planilla_detalle
set
    IngresoSueldoBase=%s,
    IngresoBonificacionDecreto=%s,
    IngresoOtrosIngresos=%s,
    DescuentoIgss=%s,
    DescuentoIsr=%s,
    DescuentoInasistencias=%s,
    SalarioNeto=%s,
    FechaModificacion=NOW(),
    UsuarioModificacion=%s
where 
    IdEmpleado = %s
    and Anio = %s
    and Mes = %s
"""
        ret = MySqldb().execute_insert(query,params=params)        
        return ret