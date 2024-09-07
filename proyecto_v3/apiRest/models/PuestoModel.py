from repositories.mysql.mysql_db import MySqldb

class PuestoModel:
    def ObtenerTodosPuesto():
        query = f"""
select 
    a.IdPuesto,
    a.Nombre,
    a.IdDepartamento,
    b.Nombre Departamento
from 
    puesto a,
    departamento b
where
    a.IdDepartamento = b.IdDepartamento
"""
        ret = MySqldb().execute_query(query)
        
        return ret
    
    def ObtenerPuestoPorDepartamento(iddepartamento):
        query = f"""
select 
    a.IdPuesto,
    a.Nombre,
    a.IdDepartamento,
    b.Nombre Departamento
from 
    puesto a,
    departamento b
where
    a.IdDepartamento = b.IdDepartamento 
    and a.IdDepartamento = {iddepartamento}
"""
        ret = MySqldb().execute_query(query)
        
        return ret
    
    def EliminarPuesto(id:int):
        query = f"""
delete
from puesto
where IdPuesto = {id}
"""
        ret = MySqldb().execute_query(query)
        
        return ret
    
    def InsertarPuesto(data,usuario):
        params = [
            {"nombre":"Nombre","valor":data.Nombre,},            
            {"nombre":"IdDepartamento","valor":data.IdDepartamento,},            

            {
                "nombre":"UsuarioCreacion",
                "valor":usuario,
            }
        ]
        query = f"""
insert into puesto
(
    Nombre,
    IdDepartamento,
    FechaCreacion,
    UsuarioCreacion
)
values
(%s,%s,NOW(),%s)
"""
        ret = MySqldb().execute_insert(query,params=params)
        
        return ret
    

    def ActualizarPuesto(data,usuario,IdPuesto):
        params = [
            {"nombre":"Nombre","valor":data.Nombre,}, 
            {"nombre":"IdDepartamento","valor":data.IdDepartamento,},           
            
            {
                "nombre":"UsuarioModificacion",
                "valor":usuario,
            },
            {
                "nombre":"IdPuesto",
                "valor":IdPuesto,
            }            
        ]
        query = f"""
update puesto 
set 
Nombre=%s, 
IdDepartamento=%s,
FechaModificacion=NOW(), 
UsuarioModificacion=%s
where IdPuesto=%s
"""
        ret = MySqldb().execute_insert(query,params=params)
        
        return ret