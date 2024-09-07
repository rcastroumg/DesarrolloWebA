from repositories.mysql.mysql_db import MySqldb

class GeneroModel:
    
    def ObtenerGenero():
        query = f"""
select 
    a.IdGenero,
    a.Nombre 
from 
    genero a 
"""
        ret = MySqldb().execute_query(query)
        
        return ret
    
    def EliminarGenero(id:int):
        query = f"""
delete
from genero
where IdGenero = {id}
"""
        ret = MySqldb().execute_query(query)
        
        return ret
    
    def InsertarGenero(data,usuario):
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
insert into genero
(Nombre,FechaCreacion,UsuarioCreacion)
values
(%s,NOW(),%s)
"""
        ret = MySqldb().execute_insert(query,params=params)
        
        return ret
    

    def ActualizarGenero(data,usuario,idgenero):
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
                "nombre":"IdGenero",
                "valor":idgenero,
            }            
        ]
        query = f"""
update genero 
set Nombre=%s, 
FechaModificacion=NOW(), 
UsuarioModificacion=%s
where IdGenero=%s
"""
        ret = MySqldb().execute_insert(query,params=params)
        
        return ret