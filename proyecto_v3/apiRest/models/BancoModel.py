from repositories.mysql.mysql_db import MySqldb

class BancoModel:
    def ObtenerTodosBancos():
        query = f"""
select 
    IdBanco,
    Nombre
from 
    banco
"""
        ret = MySqldb().execute_query(query)
        
        return ret
    
    def EliminarBanco(id:int):
        query = f"""
delete
from banco
where IdBanco = {id}
"""
        ret = MySqldb().execute_query(query)
        
        return ret
    
    def InsertarBanco(data,usuario):
        params = [
            {"nombre":"Nombre","valor":data.Nombre,},            

            {
                "nombre":"UsuarioCreacion",
                "valor":usuario,
            }
        ]
        query = f"""
insert into banco
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
    

    def ActualizarBanco(data,usuario,idbanco):
        params = [
            {"nombre":"Nombre","valor":data.Nombre,},            
            
            {
                "nombre":"UsuarioModificacion",
                "valor":usuario,
            },
            {
                "nombre":"IdBanco",
                "valor":idbanco,
            }            
        ]
        query = f"""
update banco 
set 
Nombre=%s, 
FechaModificacion=NOW(), 
UsuarioModificacion=%s
where IdBanco=%s
"""
        ret = MySqldb().execute_insert(query,params=params)
        
        return ret