from repositories.mysql.mysql_db import MySqldb

class EmpresaModel:
    
    def ObtenerTodosEmpresas():
        query = f"""
select 
    IdEmpresa,
    Nombre,
    Direccion,
    Nit,
    PasswordCantidadMayusculas,
    PasswordCantidadMinusculas,
    PasswordCantidadCaracteresEspeciales,
    PasswordCantidadCaducidadDias,
    PasswordLargo,
    PasswordIntentosAntesDeBloquear,
    PasswordCantidadNumeros,
    PasswordCantidadPreguntasValidar
from 
    empresa
"""
        ret = MySqldb().execute_query(query)
        
        return ret
    

    def ObtenerEmpresaUsuario(idusuario):
        query = f"""
select 
    a.IdEmpresa,
    a.Nombre,
    a.Direccion,
    a.Nit,
    a.PasswordCantidadMayusculas,
    a.PasswordCantidadMinusculas,
    a.PasswordCantidadCaracteresEspeciales,
    a.PasswordCantidadCaducidadDias,
    a.PasswordLargo,
    a.PasswordIntentosAntesDeBloquear,
    a.PasswordCantidadNumeros,
    a.PasswordCantidadPreguntasValidar
from 
    empresa a
    inner join sucursal b on a.IdEmpresa = b.IdEmpresa
    inner join usuario c on b.IdSucursal = c.IdSucursal
where
    c.IdUsuario = '{idusuario}'
"""
        ret = MySqldb().execute_query(query)
        
        return ret
    

    def EliminarEmpresa(id:int):
        query = f"""
delete
from empresa
where IdEmpresa = {id}
"""
        ret = MySqldb().execute_query(query)
        
        return ret
    
    def InsertarEmpresa(data,usuario):
        params = [
            {"nombre":"Nombre","valor":data.Nombre,},
            {"nombre":"Direccion","valor":data.Direccion,},
            {"nombre":"Nit","valor":data.Nit,},
            {"nombre":"PasswordCantidadMayusculas","valor":data.PasswordCantidadMayusculas,},
            {"nombre":"PasswordCantidadMinusculas","valor":data.PasswordCantidadMinusculas,},
            {"nombre":"PasswordCantidadCaracteresEspeciales","valor":data.PasswordCantidadCaracteresEspeciales,},
            {"nombre":"PasswordCantidadCaducidadDias","valor":data.PasswordCantidadCaducidadDias,},
            {"nombre":"PasswordLargo","valor":data.PasswordLargo,},
            {"nombre":"PasswordIntentosAntesDeBloquear","valor":data.PasswordIntentosAntesDeBloquear,},
            {"nombre":"PasswordCantidadNumeros","valor":data.PasswordCantidadNumeros,},
            {"nombre":"PasswordCantidadPreguntasValidar","valor":data.PasswordCantidadPreguntasValidar,},

            {
                "nombre":"UsuarioCreacion",
                "valor":usuario,
            }
        ]
        query = f"""
insert into empresa
(
    Nombre,
    Direccion,
    Nit,
    PasswordCantidadMayusculas,
    PasswordCantidadMinusculas,
    PasswordCantidadCaracteresEspeciales,
    PasswordCantidadCaducidadDias,
    PasswordLargo,
    PasswordIntentosAntesDeBloquear,
    PasswordCantidadNumeros,
    PasswordCantidadPreguntasValidar,
    FechaCreacion,
    UsuarioCreacion
)
values
(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,NOW(),%s)
"""
        ret = MySqldb().execute_insert(query,params=params)
        
        return ret
    

    def ActualizarEmpresa(data,usuario,idempresa):
        params = [
            {"nombre":"Nombre","valor":data.Nombre,},
            {"nombre":"Direccion","valor":data.Direccion,},
            {"nombre":"Nit","valor":data.Nit,},
            {"nombre":"PasswordCantidadMayusculas","valor":data.PasswordCantidadMayusculas,},
            {"nombre":"PasswordCantidadMinusculas","valor":data.PasswordCantidadMinusculas,},
            {"nombre":"PasswordCantidadCaracteresEspeciales","valor":data.PasswordCantidadCaracteresEspeciales,},
            {"nombre":"PasswordCantidadCaducidadDias","valor":data.PasswordCantidadCaducidadDias,},
            {"nombre":"PasswordLargo","valor":data.PasswordLargo,},
            {"nombre":"PasswordIntentosAntesDeBloquear","valor":data.PasswordIntentosAntesDeBloquear,},
            {"nombre":"PasswordCantidadNumeros","valor":data.PasswordCantidadNumeros,},
            {"nombre":"PasswordCantidadPreguntasValidar","valor":data.PasswordCantidadPreguntasValidar,},
            
            {
                "nombre":"UsuarioModificacion",
                "valor":usuario,
            },
            {
                "nombre":"IdEmpresa",
                "valor":idempresa,
            }            
        ]
        query = f"""
update empresa 
set 
Nombre=%s, 
Direccion=%s, 
Nit=%s, 
PasswordCantidadMayusculas=%s, 
PasswordCantidadMinusculas=%s, 
PasswordCantidadCaracteresEspeciales=%s, 
PasswordCantidadCaducidadDias=%s, 
PasswordLargo=%s, 
PasswordIntentosAntesDeBloquear=%s, 
PasswordCantidadNumeros=%s, 
PasswordCantidadPreguntasValidar=%s, 
FechaModificacion=NOW(), 
UsuarioModificacion=%s
where IdEmpresa=%s
"""
        ret = MySqldb().execute_insert(query,params=params)
        
        return ret