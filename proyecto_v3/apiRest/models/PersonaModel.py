from repositories.mysql.mysql_db import MySqldb

class PersonaModel:
    def InsertarPersona(data,usuario):
        params = [
            {"nombre":"Nombre","valor":data.Nombre,},            
            {"nombre":"Apellido","valor":data.Apellido,},          
            {"nombre":"FechaNacimiento","valor":data.FechaNacimiento,},          
            {"nombre":"IdGenero","valor":data.IdGenero,},          
            {"nombre":"Direccion","valor":data.Direccion,},          
            {"nombre":"Telefono","valor":data.Telefono,},          
            {"nombre":"CorreoElectronico","valor":data.CorreoElectronico,},          
            {"nombre":"IdEstadoCivil","valor":data.IdEstadoCivil,},          

            {
                "nombre":"UsuarioCreacion",
                "valor":usuario,
            }
        ]
        query = f"""
insert into persona
(
    Nombre,
    Apellido,
    FechaNacimiento,
    IdGenero,
    Direccion,
    Telefono,
    CorreoElectronico,
    IdEstadoCivil,
    FechaCreacion,
    UsuarioCreacion
)
values
(%s,%s,%s,%s,%s,%s,%s,%s,NOW(),%s)
"""
        ret = MySqldb().execute_insert(query,params=params)
        
        return ret
    

    def ActualizarPersona(data,usuario):
        params = [
            {"nombre":"Nombre","valor":data.Nombre,},            
            {"nombre":"Apellido","valor":data.Apellido,},          
            {"nombre":"FechaNacimiento","valor":data.FechaNacimiento,},          
            {"nombre":"IdGenero","valor":data.IdGenero,},          
            {"nombre":"Direccion","valor":data.Direccion,},          
            {"nombre":"Telefono","valor":data.Telefono,},          
            {"nombre":"CorreoElectronico","valor":data.CorreoElectronico,},          
            {"nombre":"IdEstadoCivil","valor":data.IdEstadoCivil,},          

            {
                "nombre":"UsuarioCreacion",
                "valor":usuario,
            }
        ]
        query = f"""
update persona
set
    Nombre=%s,
    Apellido=%s,
    FechaNacimiento=%s,
    IdGenero=%s,
    Direccion=%s,
    Telefono=%s,
    CorreoElectronico=%s,
    IdEstadoCivil=%s,
    FechaModificacion=NOW(),
    UsuarioModificacion=%s
where
    IdPersona = {data.IdPersona}
"""
        ret = MySqldb().execute_insert(query,params=params)
        
        return ret