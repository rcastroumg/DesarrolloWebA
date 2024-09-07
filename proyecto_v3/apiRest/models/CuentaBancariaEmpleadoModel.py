from repositories.mysql.mysql_db import MySqldb

class CuentaBancariaEmpleadoModel:
    def ObtenerTodosCuentaBancariaEmpleado(idempleado):
        query = f"""
select 
    a.IdCuentaBancaria,
    a.IdEmpleado,
    a.IdBanco,
    b.Nombre Banco,
    a.NumeroDeCuenta,
    a.Activa 
from 
    cuenta_bancaria_empleado a, 
    banco b 
where 
    a.IdBanco = b.IdBanco
    and a.IdEmpleado = {idempleado} 
"""
        ret = MySqldb().execute_query(query)
        
        return ret
    

    def EliminarCuentaBancariaEmpleado(id:int):
        query = f"""
delete
from cuenta_bancaria_empleado
where IdCuentaBancaria = {id}
"""
        ret = MySqldb().execute_query(query)
        
        return ret
    
    
    def InsertarCuentaBancariaEmpleado(data,usuario):
        params = [
            {"nombre":"IdEmpleado","valor":data.IdEmpleado,},            
            {"nombre":"IdBanco","valor":data.IdBanco,},            
            {"nombre":"NumeroDeCuenta","valor":data.NumeroDeCuenta,},     

            {
                "nombre":"UsuarioCreacion",
                "valor":usuario,
            }
        ]
        query = f"""
insert into cuenta_bancaria_empleado
(
    IdEmpleado,
    IdBanco,
    NumeroDeCuenta,
    Activa,
    FechaCreacion,
    UsuarioCreacion
)
values
(%s,%s,%s,'1',NOW(),%s)
"""
        ret = MySqldb().execute_insert(query,params=params)
        
        return ret
    
    def InactivarUltimaCuentaBancaria(idempleado):
        query = f"""
update cuenta_bancaria_empleado
set
Activa = '0'
where Activa = '1'  
and IdEmpleado = {idempleado}
"""
        ret = MySqldb().execute_query(query)
        
        return ret