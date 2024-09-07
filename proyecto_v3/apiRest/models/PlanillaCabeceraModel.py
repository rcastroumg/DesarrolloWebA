from repositories.mysql.mysql_db import MySqldb

class PlanillaCabeceraModel:
    def ObtenerTodosPlanillaCabecera():
        query = f"""
select 
    a.Anio,
    a.Mes,
    b.FechaInicio,
    b.FechaFin,
    a.TotalIngresos,
    a.TotalDescuentos,
    a.SalarioNeto,
    a.FechaHoraCalculada,
    c.Empleados,
    a.FechaHoraProcesada
from 
    planilla_cabecera a,
    periodo_planilla b,
    (
        select 
            pd.Anio,
            pd.Mes,
            count(*) Empleados 
        from 
            planilla_detalle pd 
        group by
            pd.Anio, pd.Mes
    ) c
where
    a.Anio = b.Anio
    and a.Mes = b.Mes
    and a.Anio = c.Anio
    and a.Mes = c.Mes
order by
    a.Anio desc, a.Mes desc
"""
        ret = MySqldb().execute_query(query)
        
        return ret
    
    def BuscarPlanillaCabecera(anio,mes):
        query = f"""
select 
    a.Anio,
    a.Mes,
    b.FechaInicio,
    b.FechaFin,
    c.TotalIngresos,
    c.TotalDescuentos,
    c.TotalIngresos-c.TotalDescuentos SalarioNeto,
    a.FechaHoraCalculada,
    c.Empleados,
    a.FechaHoraProcesada
from 
    planilla_cabecera a,
    periodo_planilla b,
    (
        select 
            pd.Anio,
            pd.Mes,
            count(*) Empleados,
            sum(IngresoSueldoBase) SueldoBase,
            sum(IngresoBonificacionDecreto) BonoDecreto,
            sum(IngresoOtrosIngresos) OtrosIngresos,
            sum(DescuentoIgss) Igss,
            sum(DescuentoIsr) Isr,
            sum(DescuentoInasistencias) Inasistencias,
            sum(IngresoSueldoBase)+sum(IngresoBonificacionDecreto)+sum(IngresoOtrosIngresos) TotalIngresos,
            sum(DescuentoIgss)+sum(DescuentoIsr)+sum(DescuentoInasistencias) TotalDescuentos
        from 
            planilla_detalle pd 
        group by
            pd.Anio, pd.Mes
    ) c
where
    a.Anio = b.Anio
    and a.Mes = b.Mes
    and a.Anio = c.Anio
    and a.Mes = c.Mes
    and a.Anio = {anio} 
    and a.Mes = {mes}
"""
        ret = MySqldb().execute_query(query)        
        return ret
    

    def InsertarPlanillaCabecera(data,usuario):
        params = [
            {"nombre":"Anio","valor":data.Anio,},            
            {"nombre":"Mes","valor":data.Mes,},            

            {
                "nombre":"UsuarioCreacion",
                "valor":usuario,
            }
        ]
        query = f"""
insert into planilla_cabecera
(
    Anio,
    Mes,
    FechaCreacion,
    UsuarioCreacion
)
values
(%s,%s,NOW(),%s)
"""
        ret = MySqldb().execute_insert(query,params=params)
        
        return ret
    


    def EliminarPlanillaCabecera(anio,mes):
        query = f"""
delete
from planilla_cabecera
where 
    anio = {anio} 
    and mes = {mes}
"""
        ret = MySqldb().execute_query(query)
        return ret
    


    def ActualizarFechaCalculo(data,usuario):
        params = [
            {"nombre":"UsuarioCreacion","valor":usuario,},
            {"nombre":"Anio","valor":data.Anio,},            
            {"nombre":"Mes","valor":data.Mes,},            
        ]
        query = f"""
update planilla_cabecera
set
    FechaHoraCalculada=NOW(),
    FechaModificacion=NOW(),
    UsuarioCreacion=%s
where
    Anio=%s 
    and Mes=%s
"""
        ret = MySqldb().execute_insert(query,params=params)        
        return ret
    

    def ActualizarFechaCreado(data,usuario):
        params = [
            {"nombre":"UsuarioCreacion","valor":usuario,},
            {"nombre":"Anio","valor":data.Anio,},            
            {"nombre":"Mes","valor":data.Mes,},            
        ]
        query = f"""
update planilla_cabecera
set
    FechaHoraCalculada=NULL,
    FechaModificacion=NOW(),
    UsuarioCreacion=%s
where
    Anio=%s 
    and Mes=%s
"""
        ret = MySqldb().execute_insert(query,params=params)        
        return ret
    

    def ActualizarFechaPagado(data,usuario):
        params = [
            {"nombre":"UsuarioCreacion","valor":usuario,},
            {"nombre":"Anio","valor":data.Anio,},            
            {"nombre":"Mes","valor":data.Mes,},            
        ]
        query = f"""
update planilla_cabecera
set
    FechaHoraProcesada=NOW(),
    FechaModificacion=NOW(),
    UsuarioCreacion=%s
where
    Anio=%s 
    and Mes=%s
"""
        ret = MySqldb().execute_insert(query,params=params)        
        return ret
    
