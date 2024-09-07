from repositories.mysql.mysql_db import MySqldb

class StatusUsuarioModel:
    
    def ObtenerStatusUsuario():
        query = f"""
select 
    a.IdStatusUsuario,
    a.Nombre 
from 
    status_usuario a 
"""
        ret = MySqldb().execute_query(query)
        
        return ret
    
    def EliminarStatusUsuario(id:int):
        query = f"""
delete
from status_usuario
where IdStatusUsuario = {id}
"""
        ret = MySqldb().execute_query(query)
        
        return ret
    
    def InsertarStatusUsuario(data,usuario):
        params = [
            {
                "nombre":"Nombre",
                "valor":data.Nombre,
            },
            {
                "nombre":"UsuarioCreacion",
                "valor":usuario,
            }
        ]
        query = f"""
insert into status_usuario
(Nombre,FechaCreacion,UsuarioCreacion)
values
(%s,NOW(),%s)
"""
        ret = MySqldb().execute_insert(query,params=params)
        
        return ret
    

    def ActualizarStatusUsuario(data,usuario,idstatususuario):
        params = [
            {
                "nombre":"Nombre",
                "valor":data.Nombre,
            },
            {
                "nombre":"UsuarioModificacion",
                "valor":usuario,
            },
            {
                "nombre":"IdStatusUsuario",
                "valor":idstatususuario,
            }            
        ]
        query = f"""
update status_usuario 
set Nombre=%s, 
FechaModificacion=NOW(), 
UsuarioModificacion=%s
where IdStatusUsuario=%s
"""
        ret = MySqldb().execute_insert(query,params=params)
        
        return ret