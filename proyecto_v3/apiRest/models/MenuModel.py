from repositories.mysql.mysql_db import MySqldb

class MenuModel:
    
    def ObtenerMenus(usr:str,modulo:int):
        query = f"""
select 
    b.IdMenu,
    b.Nombre Menu
from 
    modulo a 
    inner join menu b on a.IdModulo = b.IdModulo 
    inner join opcion c on b.IdMenu = c.IdMenu 
    inner join role_opcion ro on c.IdOpcion = ro.IdOpcion 
    inner join role r on ro.IdRole = r.IdRole 
    inner join usuario_role ur on r.IdRole = ur.IdRole 
where 
    ur.IdUsuario = '{usr}' 
    and b.IdModulo = {modulo}
group by a.IdModulo, a.Nombre, b.IdMenu,b.Nombre
order by b.OrdenMenu asc
"""
        ret = MySqldb().execute_query(query)
        
        return ret
    
    def ObtenerTodosMenus():
            query = f"""
    select 
        a.IdMenu,
        a.IdModulo,
        b.Nombre Modulo,
        a.Nombre,
        a.OrdenMenu
    from 
        menu a, modulo b
    where a.IdModulo = b.IdModulo
    """
            ret = MySqldb().execute_query(query)
            
            return ret
    
    def EliminarMenu(id:int):
        query = f"""
delete
from menu
where IdMenu = {id}
"""
        ret = MySqldb().execute_query(query)
        
        return ret
    
    def InsertarMenu(data,usuario):
        params = [
            {
                "nombre":"IdModulo",
                "valor":data.IdModulo,
            },
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
insert into menu
(IdModulo,Nombre,OrdenMenu,FechaCreacion,UsuarioCreacion)
values
(%s,%s,%s,NOW(),%s)
"""
        ret = MySqldb().execute_insert(query,params=params)
        
        return ret
    

    def ActualizarMenu(data,usuario,id):
        params = [
            {
                "nombre":"IdModulo",
                "valor":data.IdModulo,
            },
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
                "nombre":"IdMenu",
                "valor":id,
            }            
        ]
        query = f"""
update menu 
set IdModulo=%s, 
Nombre=%s, 
OrdenMenu=%s, 
FechaModificacion=NOW(), 
UsuarioModificacion=%s
where IdMenu=%s
"""
        ret = MySqldb().execute_insert(query,params=params)
        
        return ret