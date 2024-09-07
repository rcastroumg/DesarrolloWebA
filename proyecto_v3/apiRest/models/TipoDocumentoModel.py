from repositories.mysql.mysql_db import MySqldb

class TipoDocumentoModel:
    def ObtenerTodosTipoDocumento():
        query = f"""
select 
    IdTipoDocumento,
    Nombre
from 
    tipo_documento
"""
        ret = MySqldb().execute_query(query)
        
        return ret
    
    def EliminarTipoDocumento(id:int):
        query = f"""
delete
from tipo_documento
where IdTipoDocumento = {id}
"""
        ret = MySqldb().execute_query(query)
        
        return ret
    
    def InsertarTipoDocumento(data,usuario):
        params = [
            {"nombre":"Nombre","valor":data.Nombre,},            

            {
                "nombre":"UsuarioCreacion",
                "valor":usuario,
            }
        ]
        query = f"""
insert into tipo_documento
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
    

    def ActualizarTipoDocumento(data,usuario,IdTipoDocumento):
        params = [
            {"nombre":"Nombre","valor":data.Nombre,},            
            
            {
                "nombre":"UsuarioModificacion",
                "valor":usuario,
            },
            {
                "nombre":"IdTipoDocumento",
                "valor":IdTipoDocumento,
            }            
        ]
        query = f"""
update tipo_documento 
set 
Nombre=%s, 
FechaModificacion=NOW(), 
UsuarioModificacion=%s
where IdTipoDocumento=%s
"""
        ret = MySqldb().execute_insert(query,params=params)
        
        return ret