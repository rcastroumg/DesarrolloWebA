from repositories.mysql.mysql_db import MySqldb

class UsuarioPreguntaModel:
    def ObtenerTodosUsuarioPregunta(idusuario,numpregunta=50):
        query = f"""
    select 
        a.IdPregunta,
        a.IdUsuario,
        a.Pregunta,
        '' as Respuesta
    from 
        usuario_pregunta a
    where 
        a.IdUsuario = '{idusuario}' 
    order by OrdenPregunta asc 
    limit {numpregunta} 
    """
        ret = MySqldb().execute_query(query)            
        return ret
    

    def obtenerRespuesta(idusuario,idpregunta):
        query = f"""
    select 
        Respuesta
    from 
        usuario_pregunta
    where 
        IdUsuario = '{idusuario}' 
        and IdPregunta = {idpregunta}
    """
        ret = MySqldb().execute_query(query)            
        return ret