from repositories.mysql.mysql_db import MySqldb

class PeriodoPlanillaModel:
    def ObtenerTodosPeriodoPlanilla():
        query = f"""
select 
    Anio,
    Mes,
    FechaInicio,
    FechaFin
from 
    periodo_planilla
order by
    Anio, Mes
"""
        ret = MySqldb().execute_query(query)
        
        return ret
    
    def EliminarPeriodoPlanilla(anio:int,mes:int):
        query = f"""
delete
from periodo_planilla
where Anio = {anio}
and Mes = {mes}
"""
        ret = MySqldb().execute_query(query)
        
        return ret
    
    def InsertarPeriodoPlanilla(data,usuario):
        params = [
            {"nombre":"Nombre","valor":data.Anio,},            
            {"nombre":"IdDepartamento","valor":data.Mes,},            

            {
                "nombre":"UsuarioCreacion",
                "valor":usuario,
            }
        ]
        query = f"""
insert into periodo_planilla
(
    Anio,
    Mes,
    FechaInicio,
    FechaFin,
    FechaCreacion,
    UsuarioCreacion
)
values
(%s,%s,DATE('{data.Anio}-{data.Mes}-01 00:00:00'),LAST_DAY(DATE('{data.Anio}-{data.Mes}-01 00:00:00')),NOW(),%s)
"""
        ret = MySqldb().execute_insert(query,params=params)
        
        return ret
    

    def BuscarPeriodoPlanilla(anio,mes):
        query = f"""
select 
    Anio,
    Mes,
    FechaInicio,
    FechaFin
from 
    periodo_planilla
where
    Anio = {anio} 
    and Mes = {mes} 
order by
    Anio, Mes
"""
        ret = MySqldb().execute_query(query)
        
        return ret

