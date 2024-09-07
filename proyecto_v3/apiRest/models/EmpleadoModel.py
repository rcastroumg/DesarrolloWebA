from repositories.mysql.mysql_db import MySqldb

class EmpleadoModel:
    def ObtenerTodosEmpleado():
        query = f"""
select 
    a.IdEmpleado,
    b.Nombre,
    b.Apellido,
    a.FechaContratacion,
    c.Nombre Status
from 
    empleado a,
    persona b,
    status_empleado c
where 
    a.IdPersona = b.IdPersona
    and a.IdStatusEmpleado = c.IdStatusEmpleado
"""
        ret = MySqldb().execute_query(query)
        
        return ret
    
    def ObtenerEmpleadoUnico(idempleado):
        query = f"""
select 
    a.IdEmpleado,
    a.IdPersona,
    b.Nombre,
    b.Apellido,
    b.FechaNacimiento,
    b.IdGenero,
    b.IdEstadoCivil,
    b.Direccion,
    b.Telefono,
    b.CorreoElectronico,
    a.IdSucursal,
    c.IdDepartamento,
    a.IdPuesto,
    a.FechaContratacion,
    a.IdStatusEmpleado,
    a.IngresoSueldoBase,
    a.IngresoBonificacionDecreto,
    a.IngresoOtrosIngresos,
    a.DescuentoIgss,
    a.DescuentoIsr,
    a.DescuentoInasistencias
from 
    empleado a,
    persona b,
    puesto c
where 
    a.IdPersona = b.IdPersona
    and a.IdPuesto = c.IdPuesto
    and a.IdEmpleado = {idempleado}
"""
        ret = MySqldb().execute_query(query)        
        return ret
    
    def ObtenerEmpleadoContratado():
        query = f"""
select 
    a.IdEmpleado,
    b.Nombre,
    b.Apellido,
    c.Nombre Status
from 
    empleado a,
    persona b,
    status_empleado c
where 
    a.IdPersona = b.IdPersona
    and a.IdStatusEmpleado = c.IdStatusEmpleado
    and c.IdStatusEmpleado in (1,2,3)
"""
        ret = MySqldb().execute_query(query)
        
        return ret
    

    def ObtenerEmpleadoActivo():
        query = f"""
select 
    a.IdEmpleado,
    b.Nombre,
    b.Apellido,
    c.Nombre Status
from 
    empleado a,
    persona b,
    status_empleado c
where 
    a.IdPersona = b.IdPersona
    and a.IdStatusEmpleado = c.IdStatusEmpleado
    and c.IdStatusEmpleado = 1
"""
        ret = MySqldb().execute_query(query)
        
        return ret
    

    def InsertarEmpleado(data,usuario):
        params = [
            {"nombre":"IdPersona","valor":data.IdPersona,},            
            {"nombre":"IdSucursal","valor":data.IdSucursal,},          
            {"nombre":"FechaContratacion","valor":data.FechaContratacion,},          
            {"nombre":"IdPuesto","valor":data.IdPuesto,},          
            {"nombre":"IdStatusEmpleado","valor":data.IdStatusEmpleado,},          
            {"nombre":"IngresoSueldoBase","valor":data.IngresoSueldoBase,},          
            {"nombre":"IngresoBonificacionDecreto","valor":data.IngresoBonificacionDecreto,},          
            {"nombre":"IngresoOtrosIngresos","valor":data.IngresoOtrosIngresos,},          
            {"nombre":"DescuentoIgss","valor":data.DescuentoIgss,},          
            {"nombre":"DescuentoIsr","valor":data.DescuentoIsr,},          
            {"nombre":"DescuentoInasistencias","valor":data.DescuentoInasistencias,},          

            {
                "nombre":"UsuarioCreacion",
                "valor":usuario,
            }
        ]
        query = f"""
insert into empleado
(
    IdPersona,
    IdSucursal,
    FechaContratacion,
    IdPuesto,
    IdStatusEmpleado,
    IngresoSueldoBase,
    IngresoBonificacionDecreto,
    IngresoOtrosIngresos,
    DescuentoIgss,
    DescuentoIsr,
    DescuentoInasistencias,
    FechaCreacion,
    UsuarioCreacion
)
values
(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,NOW(),%s)
"""
        ret = MySqldb().execute_insert(query,params=params)
        
        return ret
    

    def ActualizarEmpleado(data,usuario):
        params = [           
            {"nombre":"IdSucursal","valor":data.IdSucursal,},          
            {"nombre":"FechaContratacion","valor":data.FechaContratacion,},          
            {"nombre":"IdPuesto","valor":data.IdPuesto,},          
            {"nombre":"IdStatusEmpleado","valor":data.IdStatusEmpleado,},          
            {"nombre":"IngresoSueldoBase","valor":data.IngresoSueldoBase,},          
            {"nombre":"IngresoBonificacionDecreto","valor":data.IngresoBonificacionDecreto,},          
            {"nombre":"IngresoOtrosIngresos","valor":data.IngresoOtrosIngresos,},          
            {"nombre":"DescuentoIgss","valor":data.DescuentoIgss,},          
            {"nombre":"DescuentoIsr","valor":data.DescuentoIsr,},          
            {"nombre":"DescuentoInasistencias","valor":data.DescuentoInasistencias,},          

            {
                "nombre":"UsuarioCreacion",
                "valor":usuario,
            }
        ]
        query = f"""
update empleado
set 
    IdSucursal=%s,
    FechaContratacion=%s,
    IdPuesto=%s,
    IdStatusEmpleado=%s,
    IngresoSueldoBase=%s,
    IngresoBonificacionDecreto=%s,
    IngresoOtrosIngresos=%s,
    DescuentoIgss=%s,
    DescuentoIsr=%s,
    DescuentoInasistencias=%s,
    FechaModificacion=NOW(),
    UsuarioModificacion=%s
where 
    IdEmpleado = {data.IdEmpleado}
"""
        ret = MySqldb().execute_insert(query,params=params)
        
        return ret