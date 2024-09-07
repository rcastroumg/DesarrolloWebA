from repositories.mysql.mysql_db import MySqldb

class DepartamentoModel:
    def ObtenerTodosDepartamento():
        query = f"""
select 
    a.IdDepartamento,
    a.Nombre,
    a.IdEmpresa,
    b.Nombre Empresa
from 
    departamento a,
    empresa b
where
    a.IdEmpresa = b.IdEmpresa
"""
        ret = MySqldb().execute_query(query)
        
        return ret
    
    def ObtenerDepartamentoPorEmpresa(idempresa):
        query = f"""
select 
    a.IdDepartamento,
    a.Nombre,
    a.IdEmpresa,
    b.Nombre Empresa
from 
    departamento a,
    empresa b
where
    a.IdEmpresa = b.IdEmpresa 
    and a.IdEmpresa = {idempresa}
"""
        ret = MySqldb().execute_query(query)        
        return ret
    
    def EliminarDepartamento(id:int):
        query = f"""
delete
from departamento
where IdDepartamento = {id}
"""
        ret = MySqldb().execute_query(query)
        
        return ret
    
    def InsertarDepartamento(data,usuario):
        params = [
            {"nombre":"Nombre","valor":data.Nombre,},            
            {"nombre":"IdEmpresa","valor":data.IdEmpresa,},            

            {
                "nombre":"UsuarioCreacion",
                "valor":usuario,
            }
        ]
        query = f"""
insert into departamento
(
    Nombre,
    IdEmpresa,
    FechaCreacion,
    UsuarioCreacion
)
values
(%s,%s,NOW(),%s)
"""
        ret = MySqldb().execute_insert(query,params=params)
        
        return ret
    

    def ActualizarDepartamento(data,usuario,IdDepartamento):
        params = [
            {"nombre":"Nombre","valor":data.Nombre,}, 
            {"nombre":"IdEmpresa","valor":data.IdEmpresa,},           
            
            {
                "nombre":"UsuarioModificacion",
                "valor":usuario,
            },
            {
                "nombre":"IdDepartamento",
                "valor":IdDepartamento,
            }            
        ]
        query = f"""
update departamento 
set 
Nombre=%s, 
IdEmpresa=%s,
FechaModificacion=NOW(), 
UsuarioModificacion=%s
where IdDepartamento=%s
"""
        ret = MySqldb().execute_insert(query,params=params)
        
        return ret