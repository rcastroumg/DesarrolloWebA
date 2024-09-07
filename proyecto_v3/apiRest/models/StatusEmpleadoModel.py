from repositories.mysql.mysql_db import MySqldb

class StatusEmpleadoModel:
    def ObtenerTodosStatusEmpleado():
        query = f"""
select 
    IdStatusEmpleado,
    Nombre
from 
    status_empleado
"""
        ret = MySqldb().execute_query(query)
        
        return ret
    
    def EliminarStatusEmpleado(id:int):
        query = f"""
delete
from status_empleado
where IdStatusEmpleado = {id}
"""
        ret = MySqldb().execute_query(query)
        
        return ret
    
    def InsertarStatusEmpleado(data,usuario):
        params = [
            {"nombre":"Nombre","valor":data.Nombre,},            

            {
                "nombre":"UsuarioCreacion",
                "valor":usuario,
            }
        ]
        query = f"""
insert into status_empleado
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
    

    def ActualizarStatusEmpleado(data,usuario,IdStatusEmpleado):
        params = [
            {"nombre":"Nombre","valor":data.Nombre,},            
            
            {
                "nombre":"UsuarioModificacion",
                "valor":usuario,
            },
            {
                "nombre":"IdStatusEmpleado",
                "valor":IdStatusEmpleado,
            }            
        ]
        query = f"""
update status_empleado 
set 
Nombre=%s, 
FechaModificacion=NOW(), 
UsuarioModificacion=%s
where IdStatusEmpleado=%s
"""
        ret = MySqldb().execute_insert(query,params=params)
        
        return ret