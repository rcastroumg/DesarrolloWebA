from repositories.mysql.mysql_db import MySqldb

class RoleOpcionModel:
    def ObtenerTodosRoleOpcion(idrole):
            query = f"""
    select 
        a.IdRole,
        b.Nombre Role,
        a.IdOpcion,
        c.Nombre Opcion,
        a.Alta,
        a.Baja,
        a.Cambio,
        a.Imprimir,
        a.Exportar
    from 
        role_opcion a, role b, opcion c
    where 
        a.IdRole = b.IdRole 
        and a.IdOpcion = c.IdOpcion  
        and a.IdRole = {idrole}
    """
            ret = MySqldb().execute_query(query)
            
            return ret
    
    def EliminarRoleOpcion(idrole:int,idopcion:int):
        query = f"""
delete
from role_opcion
where IdRole = {idrole} 
and IdOpcion = {idopcion}
"""
        ret = MySqldb().execute_query(query)
        
        return ret
    
    def InsertarRoleOpcion(data,usuario):

        params = [
            {
                "nombre":"IdRole",
                "valor":data.IdRole,
            },
            {
                "nombre":"IdOpcion",
                "valor":data.IdOpcion,
            },
            {
                "nombre":"Alta",
                "valor":data.Alta,
            },
            {
                "nombre":"Baja",
                "valor":data.Baja,
            },
            {
                "nombre":"Cambio",
                "valor":data.Cambio,
            },
            {
                "nombre":"Imprimir",
                "valor":data.Imprimir,
            },
            {
                "nombre":"Exportar",
                "valor":data.Exportar,
            },
            {
                "nombre":"UsuarioCreacion",
                "valor":usuario,
            }
        ]
        query = f"""
insert into role_opcion
(IdRole,IdOpcion,Alta,Baja,Cambio,Imprimir,Exportar,FechaCreacion,UsuarioCreacion)
values
(%s,%s,%s,%s,%s,%s,%s,NOW(),%s)
"""
        ret = MySqldb().execute_insert(query,params=params)
        
        return ret
    

    def ActualizarRoleOpcion(data,usuario,idrole,idopcion):

        params = [            
            {
                "nombre":"Alta",
                "valor":data.Alta,
            },
            {
                "nombre":"Baja",
                "valor":data.Baja,
            },
            {
                "nombre":"Cambio",
                "valor":data.Cambio,
            },
            {
                "nombre":"Imprimir",
                "valor":data.Imprimir,
            },
            {
                "nombre":"Exportar",
                "valor":data.Exportar,
            },
            {
                "nombre":"UsuarioModificacion",
                "valor":usuario,
            },
            {
                "nombre":"IdRole",
                "valor":idrole,
            },
            {
                "nombre":"IdOpcion",
                "valor":idopcion,
            }            
        ]
        query = f"""
update role_opcion
set 
Alta=%s,  
Baja=%s,  
Cambio=%s,  
Imprimir=%s,  
Exportar=%s,  
FechaModificacion=NOW(), 
UsuarioModificacion=%s
where IdRole=%s 
and IdOpcion=%s
"""
        ret = MySqldb().execute_insert(query,params=params)
        
        return ret