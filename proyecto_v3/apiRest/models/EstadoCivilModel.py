from repositories.mysql.mysql_db import MySqldb

class EstadoCivilModel:
    def ObtenerTodosEstadoCivil():
        query = f"""
select 
    IdEstadoCivil,
    Nombre
from 
    estado_civil
"""
        ret = MySqldb().execute_query(query)
        
        return ret
    
    def EliminarEstadoCivil(id:int):
        query = f"""
delete
from estado_civil
where IdEstadoCivil = {id}
"""
        ret = MySqldb().execute_query(query)
        
        return ret
    
    def InsertarEstadoCivil(data,usuario):
        params = [
            {"nombre":"Nombre","valor":data.Nombre,},            

            {
                "nombre":"UsuarioCreacion",
                "valor":usuario,
            }
        ]
        query = f"""
insert into estado_civil
(
    Nombre,
    FechaCreacion,
    UsuarioCreacion
)
values
(%s,NOW(),%s)
"""
        ret = MySqldb().execute_insert(query,params=params)
        
        return ret
    

    def ActualizarEstadoCivil(data,usuario,IdEstadoCivil):
        params = [
            {"nombre":"Nombre","valor":data.Nombre,},            
            
            {
                "nombre":"UsuarioModificacion",
                "valor":usuario,
            },
            {
                "nombre":"IdEstadoCivil",
                "valor":IdEstadoCivil,
            }            
        ]
        query = f"""
update estado_civil 
set 
Nombre=%s, 
FechaModificacion=NOW(), 
UsuarioModificacion=%s
where IdEstadoCivil=%s
"""
        ret = MySqldb().execute_insert(query,params=params)
        
        return ret