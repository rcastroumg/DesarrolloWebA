from repositories.mysql.mysql_db import MySqldb
from utils.Cipher import vigenere_cipher
class UsuarioModel:
    # YA NO SE USA
    def ComprobarCredenciales(usr:str, pwd:str):
        #new_pwd = vigenere_cipher(pwd,"analisisdesistemas")
        new_pwd = pwd
        query = f"select * from usuario where IdUsuario = '{usr}' and Password = '{new_pwd}'"
        ret = MySqldb().execute_query(query)
        try:
            Usuario = ret[0]
            return Usuario
        except Exception:
            return None
        

    def BuscarUsuario(usr:str):
        query = f"""
select 
    a.*,
    b.Nombre Status
from usuario a,
status_usuario b 
where a.IdStatusUsuario = b.IdStatusUsuario 
and a.IdUsuario = '{usr}'"""
        ret = MySqldb().execute_query(query)
        try:
            Usuario = ret[0]
            return Usuario
        except Exception:
            return None
        

    def ActualizaUltimaSesion(usr:str):
        params = [
            {"nombre":"UsuarioModificacion","valor":usr,},
            {"nombre":"IdUsuario","valor":usr,}            
        ]
        query = f"""
update usuario 
set 
UltimaFechaIngreso=NOW(), 
FechaModificacion=NOW(), 
UsuarioModificacion=%s 
where IdUsuario=%s 
"""
        ret = MySqldb().execute_insert(query,params=params)        
        return ret
    

    def ActualizaIntentoSesion(usr:str):
        params = [
            {"nombre":"UsuarioModificacion","valor":usr,},
            {"nombre":"IdUsuario","valor":usr,}            
        ]
        query = f"""
update usuario 
set 
IntentosDeAcceso=IntentosDeAcceso+1, 
FechaModificacion=NOW(), 
UsuarioModificacion=%s 
where IdUsuario=%s 
"""
        ret = MySqldb().execute_insert(query,params=params)        
        return ret
    

    def ReiniciaIntentoSesion(usr:str):
        params = [
            {"nombre":"UsuarioModificacion","valor":usr,},
            {"nombre":"IdUsuario","valor":usr,}            
        ]
        query = f"""
update usuario 
set 
IntentosDeAcceso=0, 
FechaModificacion=NOW(), 
UsuarioModificacion=%s 
where IdUsuario=%s 
"""
        ret = MySqldb().execute_insert(query,params=params)        
        return ret
    

    def BloquearUsuario(usr:str):
        params = [
            {"nombre":"UsuarioModificacion","valor":usr,},
            {"nombre":"IdUsuario","valor":usr,}            
        ]
        query = f"""
update usuario 
set 
IdStatusUsuario=2, 
FechaModificacion=NOW(), 
UsuarioModificacion=%s 
where IdUsuario=%s 
"""
        ret = MySqldb().execute_insert(query,params=params)        
        return ret
    

    def CambiarContrasena(usr,password):
        params = [
            {"nombre":"Password","valor":password,},
            {"nombre":"UsuarioModificacion","valor":usr,},
            {"nombre":"IdUsuario","valor":usr,}            
        ]
        query = f"""
update usuario 
set 
Password=%s, 
FechaModificacion=NOW(), 
UsuarioModificacion=%s 
where IdUsuario=%s 
"""
        ret = MySqldb().execute_insert(query,params=params)        
        return ret

    
    def InsertaBitacora(usuario,tipo_acceso,userAgent,host,accion,os,device,browser):
        params = [
            {"nombre":"IdUsuario","valor":usuario,},            
            {"nombre":"IdTipoAcceso","valor":tipo_acceso,},
            {"nombre":"HttpUserAgent","valor":userAgent,},
            {"nombre":"DireccionIp","valor":host,},
            {"nombre":"Accion","valor":accion,},
            {"nombre":"SistemaOperativo","valor":os,},
            {"nombre":"Dispositivo","valor":device,},
            {"nombre":"Browser","valor":browser,}
        ]
        query = f"""
insert into bitacora_acceso 
(
IdUsuario,
IdTipoAcceso,
FechaAcceso,
HttpUserAgent,
DireccionIp,
Accion,
SistemaOperativo,
Dispositivo,
Browser
) 
values 
(%s,%s,NOW(),%s,%s,%s,%s,%s,%s)
"""
        ret = MySqldb().execute_insert(query,params=params)        
        return ret
        
    