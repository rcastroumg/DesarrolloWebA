from repositories.mysql.mysql_db import MySqldb

class RoleModel:
    
    def ObtenerTodosRoles():
            query = f"""
    select 
        a.IdRole,
        a.Nombre
    from 
        role a
    """
            ret = MySqldb().execute_query(query)
            
            return ret
    
    def ObtenerUnicoRole(id):
            query = f"""
    select 
        a.IdRole,
        a.Nombre
    from 
        role a
    where
        a.IdRole = {id}
    """
            ret = MySqldb().execute_query(query)
            
            return ret
    
    def EliminarRole(id:int):
        query = f"""
delete
from role
where IdRole = {id}
"""
        ret = MySqldb().execute_query(query)
        
        return ret
    
    def InsertarRole(data,usuario):

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
insert into role
(Nombre,FechaCreacion,UsuarioCreacion)
values
(%s,NOW(),%s)
"""
        ret = MySqldb().execute_insert(query,params=params)
        
        return ret
    

    def ActualizarRole(data,usuario,id):

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
                "nombre":"IdRole",
                "valor":id,
            }            
        ]
        query = f"""
update role 
set Nombre=%s,  
FechaModificacion=NOW(), 
UsuarioModificacion=%s
where IdRole=%s
"""
        ret = MySqldb().execute_insert(query,params=params)
        
        return ret