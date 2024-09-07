from repositories.mysql.mysql_db import MySqldb

class ModuloModel:
    
    def ObtenerModulos(usr:str):
        query = f"""
select 
    a.IdModulo,
    a.Nombre 
from 
    modulo a 
    inner join menu b on a.IdModulo = b.IdModulo 
    inner join opcion c on b.IdMenu = c.IdMenu 
    inner join role_opcion ro on c.IdOpcion = ro.IdOpcion 
    inner join role r on ro.IdRole = r.IdRole 
    inner join usuario_role ur on r.IdRole = ur.IdRole 
where ur.IdUsuario = '{usr}' 
group by a.IdModulo, a.Nombre
order by a.OrdenMenu asc
"""
        ret = MySqldb().execute_query(query)
        
        return ret
    
    
    def ObtenerTodosModulos():
        query = f"""
select 
    IdModulo,
    Nombre,
    OrdenMenu
from 
    modulo
"""
        ret = MySqldb().execute_query(query)
        
        return ret
    

    def EliminarModulo(id:int):
        query = f"""
delete
from modulo
where IdModulo = {id}
"""
        ret = MySqldb().execute_query(query)
        
        return ret
    
    def InsertarModulo(data,usuario):
        params = [
            {
                "nombre":"Nombre",
                "valor":data.Nombre,
            },
            {
                "nombre":"OrdenMenu",
                "valor":data.OrdenMenu,
            },
            {
                "nombre":"UsuarioCreacion",
                "valor":usuario,
            }
        ]
        query = f"""
insert into modulo
(Nombre,OrdenMenu,FechaCreacion,UsuarioCreacion)
values
(%s,%s,NOW(),%s)
"""
        ret = MySqldb().execute_insert(query,params=params)
        
        return ret
    

    def ActualizarModulo(data,usuario,idmodulo):
        params = [
            {
                "nombre":"Nombre",
                "valor":data.Nombre,
            },
            {
                "nombre":"OrdenMenu",
                "valor":data.OrdenMenu,
            },
            {
                "nombre":"UsuarioModificacion",
                "valor":usuario,
            },
            {
                "nombre":"IdModulo",
                "valor":idmodulo,
            }            
        ]
        query = f"""
update modulo 
set Nombre=%s, 
OrdenMenu=%s, 
FechaModificacion=NOW(), 
UsuarioModificacion=%s
where IdModulo=%s
"""
        ret = MySqldb().execute_insert(query,params=params)
        
        return ret
        