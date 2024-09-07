from pydantic import BaseModel
from datetime import datetime, date
from typing import Optional

class EstadoCivilRequest(BaseModel):
    Nombre:str


class TipoDocumentoRequest(BaseModel):
    Nombre:str


class DepartamentoRequest(BaseModel):
    Nombre:str
    IdEmpresa:int


class PuestoRequest(BaseModel):
    Nombre:str
    IdDepartamento:int


class DocumentosPersonaRequest(BaseModel):
    IdTipoDocumento:int
    IdPersona:int
    NoDocumento:str
    

class PersonaRequest(BaseModel):
    IdPersona:int
    Nombre:str
    Apellido:str
    FechaNacimiento:date
    IdGenero:int
    IdEstadoCivil:int
    Direccion:str
    Telefono:str
    CorreoElectronico:str
