from repositories.mysql.mysql_db import MySqldb

class InasistenciaModel:
    def ObtenerTodosInasistencia():
        query = f"""
select 
    a.IdInasistencia,
    a.IdEmpleado,
    concat(c.Nombre,' ',c.Apellido) Empleado,
    a.FechaInicial,
    a.FechaFinal,
    a.MotivoInasistencia
from 
    inasistencia a,
    empleado b,
    persona c
where
    a.IdEmpleado = b.IdEmpleado
    and b.IdPersona = c.IdPersona
"""
        ret = MySqldb().execute_query(query)
        
        return ret
    
    def EliminarInasistencia(id:int):
        query = f"""
delete
from inasistencia
where IdInasistencia = {id}
"""
        ret = MySqldb().execute_query(query)
        
        return ret
    
    def InsertarInasistencia(data,usuario):
        params = [
            {"nombre":"IdEmpleado","valor":data.IdEmpleado,},            
            {"nombre":"FechaInicial","valor":data.FechaInicial,},            
            {"nombre":"FechaFinal","valor":data.FechaFinal,},            
            {"nombre":"MotivoInasistencia","valor":data.MotivoInasistencia,},            

            {
                "nombre":"UsuarioCreacion",
                "valor":usuario,
            }
        ]
        query = f"""
insert into inasistencia
(
    IdEmpleado,
    FechaInicial,
    FechaFinal,
    MotivoInasistencia,
    FechaCreacion,
    UsuarioCreacion
)
values
(%s,%s,%s,%s,NOW(),%s)
"""
        ret = MySqldb().execute_insert(query,params=params)
        
        return ret
    

    def ActualizarInasistencia(data,usuario,IdInasistencia):
        params = [
            {"nombre":"IdEmpleado","valor":data.IdEmpleado,},            
            {"nombre":"FechaInicial","valor":data.FechaInicial,},            
            {"nombre":"FechaFinal","valor":data.FechaFinal,},            
            {"nombre":"MotivoInasistencia","valor":data.MotivoInasistencia,},           
            
            {
                "nombre":"UsuarioModificacion",
                "valor":usuario,
            },
            {
                "nombre":"IdInasistencia",
                "valor":IdInasistencia,
            }            
        ]
        query = f"""
update inasistencia 
set 
IdEmpleado=%s,
FechaInicial=%s,
FechaFinal=%s,
MotivoInasistencia=%s,
FechaModificacion=NOW(), 
UsuarioModificacion=%s
where IdInasistencia=%s
"""
        ret = MySqldb().execute_insert(query,params=params)
        
        return ret
    

    def BuscaTraslape(data):
        params = [
            #{"nombre":"IdEmpleado","valor":data.IdEmpleado,},            
            {"nombre":"FechaFinal","valor":data.FechaFinal,},                  
            {"nombre":"FechaInicial","valor":data.FechaInicial,},            
        ]
        query = f"""
select * from inasistencia a
where
    a.IdEmpleado={data.IdEmpleado}
    and a.FechaInicial <= %s and a.FechaFinal >= %s
"""
        ret = MySqldb().execute_insert(query,params=params)
        
        return ret
    

    def BuscaInasistenciaEmpleado(data,IdEmpleado):
        params = [
            #{"nombre":"IdEmpleado","valor":data.IdEmpleado,},            
            {"nombre":"FechaInicial","valor":data["FechaInicio"],},            
            {"nombre":"FechaFinal","valor":data["FechaFin"],},                  
        ]
        query = f"""
select * from inasistencia a
where
    a.IdEmpleado={IdEmpleado}
    and a.FechaInicial >= %s and a.FechaFinal <= %s
"""
        ret = MySqldb().execute_insert(query,params=params)
        
        return ret