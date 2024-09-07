from repositories.mysql.mysql_db import MySqldb

class SucursalModel:
    
    def ObtenerSucursal():
        query = f"""
select 
    a.IdSucursal,
    a.Nombre,
    a.Direccion, 
    a.IdEmpresa, 
    b.Nombre Empresa
from 
    sucursal a 
    inner join empresa b on a.IdEmpresa = b.IdEmpresa
"""
        ret = MySqldb().execute_query(query)
        
        return ret
    
    def EliminarSucursal(id:int):
        query = f"""
delete
from sucursal
where IdSucursal = {id}
"""
        ret = MySqldb().execute_query(query)
        
        return ret
    
    def InsertarSucursal(data,usuario):
        params = [
            {
                "nombre":"Nombre",
                "valor":data.Nombre,
            },
            {
                "nombre":"Direccion",
                "valor":data.Direccion,
            },
            {
                "nombre":"IdEmpresa",
                "valor":data.IdEmpresa,
            },
            {
                "nombre":"UsuarioCreacion",
                "valor":usuario,
            }
        ]
        query = f"""
insert into sucursal
(Nombre,Direccion,IdEmpresa,FechaCreacion,UsuarioCreacion)
values
(%s,%s,%s,NOW(),%s)
"""
        ret = MySqldb().execute_insert(query,params=params)
        
        return ret
    

    def ActualizarSucursal(data,usuario,idsucursal):
        params = [
            {
                "nombre":"Nombre",
                "valor":data.Nombre,
            },
            {
                "nombre":"Direccion",
                "valor":data.Direccion,
            },
            {
                "nombre":"IdEmpresa",
                "valor":data.IdEmpresa,
            },
            {
                "nombre":"UsuarioModificacion",
                "valor":usuario,
            },
            {
                "nombre":"IdSucursal",
                "valor":idsucursal,
            }            
        ]
        query = f"""
update sucursal 
set 
Nombre=%s, 
Direccion=%s,
IdEmpresa=%s,
FechaModificacion=NOW(), 
UsuarioModificacion=%s
where IdSucursal=%s
"""
        ret = MySqldb().execute_insert(query,params=params)
        
        return ret