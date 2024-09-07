from repositories.mysql.mysql_db import MySqldb

class UsuarioRoleModel:
    def ObtenerTodosUsuarioRole(idusuario):
            query = f"""
    select 
        a.IdUsuario,
        a.IdRole,
        c.Nombre Role
    from 
        usuario_role a, usuario b, role c
    where 
        a.IdUsuario = b.IdUsuario 
        and a.IdRole = c.IdRole  
        and a.IdUsuario = '{idusuario}'
    """
            ret = MySqldb().execute_query(query)
            
            return ret
    
    def EliminarUsuarioRole(idusuario:int,idrole:int):
        query = f"""
delete
from usuario_role
where IdUsuario = '{idusuario}' 
and IdRole = {idrole}
"""
        ret = MySqldb().execute_query(query)
        
        return ret
    
    def InsertarUsuarioRole(data,usuario):

        params = [
            {
                "nombre":"IdUsuario",
                "valor":data.IdUsuario,
            },
            {
                "nombre":"IdRole",
                "valor":data.IdRole,
            },
            {
                "nombre":"UsuarioCreacion",
                "valor":usuario,
            }
        ]
        query = f"""
insert into usuario_role
(IdUsuario,IdRole,FechaCreacion,UsuarioCreacion)
values
(%s,%s,NOW(),%s)
"""
        ret = MySqldb().execute_insert(query,params=params)
        
        return ret
    