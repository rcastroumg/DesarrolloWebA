from repositories.mysql.mysql_db import MySqldb

class BitacoraAccesoModel:

    def ObtenerTodosBitacora():
        query = f"""
select 
    a.IdUsuario,
    b.Nombre TipoAcceso,
    a.FechaAcceso,
    a.DireccionIp,
    a.SistemaOperativo,
    a.Dispositivo,
    a.Browser 
from 
    bitacora_acceso a, 
    tipo_acceso b 
where 
    a.IdTipoAcceso = b.IdTipoAcceso 
order by 
    a.FechaAcceso desc
"""
        ret = MySqldb().execute_query(query)
        
        return ret