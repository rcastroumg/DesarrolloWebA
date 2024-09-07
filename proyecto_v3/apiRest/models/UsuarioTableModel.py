from repositories.mysql.mysql_db import MySqldb

class UsuarioTableModel:
    
    def ObtenerTodosUsuarios():
            query = f"""
    select 
        a.IdUsuario,
        a.Nombre,
        a.Apellido,
        a.FechaNacimiento,
        a.IdStatusUsuario,
        b.Nombre Status,
        a.IdGenero,
        c.Nombre Genero,
        a.UltimaFechaIngreso,
        a.IntentosDeAcceso,
        a.SesionActual,
        a.UltimaFechaCambioPassword,
        a.CorreoElectronico,
        a.RequiereCambiarPassword,
        a.Fotografia,
        a.TelefonoMovil,
        a.IdSucursal,
        d.Nombre Sucursal,
        a.Password
    from 
        usuario a,
        status_usuario b, 
        genero c, 
        sucursal d 
    where
        a.IdStatusUsuario = b.IdStatusUsuario
        and a.IdGenero = c.IdGenero
        and a.IdSucursal = d.IdSucursal
    """
            ret = MySqldb().execute_query(query)
            
            return ret
    
    def ObtenerUnicoUsuarios(id):
            query = f"""
    select 
        a.IdUsuario,
        a.Nombre,
        a.Apellido,
        a.FechaNacimiento,
        a.IdStatusUsuario,
        a.IdGenero,
        a.UltimaFechaIngreso,
        a.IntentosDeAcceso,
        a.SesionActual,
        a.UltimaFechaCambioPassword,
        a.CorreoElectronico,
        a.RequiereCambiarPassword,
        a.Fotografia,
        a.TelefonoMovil,
        a.IdSucursal
    from 
        usuario a
    where
        a.IdUsuario = '{id}'
    """
            ret = MySqldb().execute_query(query)
            
            return ret
    
    def EliminarUsuarios(id:int):
        query = f"""
delete
from usuario
where IdUsuario = '{id}'
"""
        ret = MySqldb().execute_query(query)
        
        return ret
    
    def InsertarUsuarios(data,usuario):
        params = [
            {"nombre":"IdUsuario","valor":data.IdUsuario,},
            {"nombre":"Nombre","valor":data.Nombre,},
            {"nombre":"Apellido","valor":data.Apellido,},
            {"nombre":"FechaNacimiento","valor":data.FechaNacimiento,},
            {"nombre":"IdStatusUsuario","valor":data.IdStatusUsuario,},
            {"nombre":"IdGenero","valor":data.IdGenero,},
            {"nombre":"CorreoElectronico","valor":data.CorreoElectronico,},
            {"nombre":"RequiereCambiarPassword","valor":data.RequiereCambiarPassword,},
            {"nombre":"Fotografia","valor":data.Fotografia,},
            {"nombre":"TelefonoMovil","valor":data.TelefonoMovil,},
            {"nombre":"IdSucursal","valor":data.IdSucursal,},
            {"nombre":"Passwrod","valor":data.Password,},
            {
                "nombre":"UsuarioCreacion",
                "valor":usuario,
            }
        ]
        query = f"""
insert into usuario
(
IdUsuario,
Nombre, 
Apellido, 
FechaNacimiento, 
IdStatusUsuario, 
IdGenero, 
CorreoElectronico, 
RequiereCambiarPassword, 
Fotografia, 
TelefonoMovil, 
IdSucursal,
Password,
IntentosDeAcceso,
FechaCreacion,UsuarioCreacion)
values
(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,0,NOW(),%s)
"""
        ret = MySqldb().execute_insert(query,params=params)
        
        return ret
    

    def ActualizarUsuarios(data,usuario,idusuario):

        params = [
            {"nombre":"Nombre","valor":data.Nombre,},
            {"nombre":"Apellido","valor":data.Apellido,},
            {"nombre":"FechaNacimiento","valor":data.FechaNacimiento,},
            {"nombre":"IdStatusUsuario","valor":data.IdStatusUsuario,},
            {"nombre":"IdGenero","valor":data.IdGenero,},
            {"nombre":"IntentosDeAcceso","valor":data.IntentosDeAcceso,},
            {"nombre":"CorreoElectronico","valor":data.CorreoElectronico,},
            {"nombre":"RequiereCambiarPassword","valor":data.RequiereCambiarPassword,},
            {"nombre":"Fotografia","valor":data.Fotografia,},
            {"nombre":"TelefonoMovil","valor":data.TelefonoMovil,},
            {"nombre":"IdSucursal","valor":data.IdSucursal,},
            {"nombre":"Password","valor":data.Password,},


            {"nombre":"UsuarioModificacion","valor":usuario,},
            {"nombre":"IdUsuario","valor":idusuario,}            
        ]
        query = f"""
update usuario 
set 
Nombre=%s, 
Apellido=%s, 
FechaNacimiento=%s, 
IdStatusUsuario=%s, 
IdGenero=%s, 
IntentosDeAcceso=%s, 
CorreoElectronico=%s, 
RequiereCambiarPassword=%s, 
Fotografia=%s, 
TelefonoMovil=%s, 
IdSucursal=%s,  
Password=%s,
FechaModificacion=NOW(), 
UsuarioModificacion=%s 
where IdUsuario=%s 
"""
        ret = MySqldb().execute_insert(query,params=params)
        
        return ret