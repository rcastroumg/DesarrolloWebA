from repositories.mysql.mysql_db import MySqldb

class DocumentosPersonaModel:
    def ObtenerTodosDocumentosPersona(idpersona):
        query = f"""
select 
    a.IdTipoDocumento,
    b.Nombre TipoDocumento,
    a.IdPersona,
    a.NoDocumento 
from 
    documento_persona a, 
    tipo_documento b 
where 
    a.IdTipoDocumento = b.IdTipoDocumento
    and a.IdPersona = {idpersona} 
"""
        ret = MySqldb().execute_query(query)
        
        return ret
    

    def EliminarDocumentosPersona(idtipodoc:int,idpersona):
        query = f"""
delete
from documento_persona
where IdTipoDocumento = {idtipodoc} 
and IdPersona = {idpersona}
"""
        ret = MySqldb().execute_query(query)
        
        return ret
    
    
    def InsertarDocumentosPersona(data,usuario):
        params = [
            {"nombre":"IdTipoDocumento","valor":data.IdTipoDocumento,},            
            {"nombre":"IdPersona","valor":data.IdPersona,},            
            {"nombre":"NoDocumento","valor":data.NoDocumento,},            

            {
                "nombre":"UsuarioCreacion",
                "valor":usuario,
            }
        ]
        query = f"""
insert into documento_persona
(
    IdTipoDocumento,
    IdPersona,
    NoDocumento,
    FechaCreacion,
    UsuarioCreacion
)
values
(%s,%s,%s,NOW(),%s)
"""
        ret = MySqldb().execute_insert(query,params=params)
        
        return ret