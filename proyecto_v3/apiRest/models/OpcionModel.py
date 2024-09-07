from repositories.mysql.mysql_db import MySqldb

class OpcionModel:
    
    def ObtenerOpciones(usr:str,modulo:int,menu:int):
        query = f"""
select 
    c.IdOpcion,
    c.Nombre Opcion,
    c.Pagina Ruta
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
    and c.IdMenu = {menu}
group by a.IdModulo, a.Nombre, b.IdMenu,b.Nombre,c.IdOpcion,c.Nombre,c.Pagina 
order by c.OrdenMenu asc
"""
        ret = MySqldb().execute_query(query)
        
        return ret
    

    def ObtenerTodosOpciones():
            query = f"""
    select 
        a.IdOpcion,
        a.IdMenu,
        b.Nombre Menu,
        a.Nombre,
        a.OrdenMenu,
        a.Pagina
    from 
        opcion a, menu b
    where 
        a.IdMenu = b.IdMenu
    order by
        a.IdMenu,a.OrdenMenu
    """
            ret = MySqldb().execute_query(query)
            
            return ret
    
    def EliminarOpcion(id:int):
        query = f"""
delete
from opcion
where IdOpcion = {id}
"""
        ret = MySqldb().execute_query(query)
        return ret
    
    def InsertarOpcion(data,usuario):
        params = [
            {
                "nombre":"IdMenu",
                "valor":data.IdMenu,
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
                "nombre":"Pagina",
                "valor":data.Pagina,
            },
            {
                "nombre":"UsuarioCreacion",
                "valor":usuario,
            }
        ]
        query = f"""
insert into opcion
(IdMenu,Nombre,OrdenMenu,Pagina,FechaCreacion,UsuarioCreacion)
values
(%s,%s,%s,%s,NOW(),%s)
"""
        ret = MySqldb().execute_insert(query,params=params)
        
        return ret
    

    def ActualizarOpcion(data,usuario,id):
        params = [
            {
                "nombre":"IdMenu",
                "valor":data.IdMenu,
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
                "nombre":"Pagina",
                "valor":data.Pagina,
            },
            {
                "nombre":"UsuarioModificacion",
                "valor":usuario,
            },
            {
                "nombre":"IdOpcion",
                "valor":id,
            }            
        ]
        query = f"""
update opcion 
set IdMenu=%s, 
Nombre=%s, 
OrdenMenu=%s,
Pagina=%s, 
FechaModificacion=NOW(), 
UsuarioModificacion=%s
where IdOpcion=%s
"""
        ret = MySqldb().execute_insert(query,params=params)
        
        return ret
    

    def findOpcionByRoute(strRoute):
        query = f"""
    select 
        IdOpcion,
        Nombre,
        Pagina 
    from 
        opcion 
    where 
    '{strRoute}' like CONCAT(REPLACE(Pagina,'/','-'),'%')
    """
        ret = MySqldb().execute_query(query)
        
        return ret
    
    def tieneAcceso(IdUsuario,IdOpcion):
        query = f"""
select 
    a.IdModulo,
    a.Nombre Modulo,
    b.IdMenu, 
    b.Nombre Menu,
    c.IdOpcion,
    c.Nombre Opcion,
    r.IdRole,
    r.Nombre Role,
    ro.Alta,
    ro.Baja,
    ro.Cambio,
    ro.Imprimir,
    ro.Exportar
from 
    modulo a 
    inner join menu b on a.IdModulo = b.IdModulo 
    inner join opcion c on b.IdMenu = c.IdMenu 
    inner join role_opcion ro on c.IdOpcion = ro.IdOpcion 
    inner join role r on ro.IdRole = r.IdRole 
    inner join usuario_role ur on r.IdRole = ur.IdRole 
where ur.IdUsuario = '{IdUsuario}' 
and c.IdOpcion = {IdOpcion}
order by a.OrdenMenu asc
"""
        ret = MySqldb().execute_query(query)

        return ret
        """ try:
            registro = ret[0]
            return True
        except:
            return False """