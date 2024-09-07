from pydantic import BaseModel
from datetime import datetime, date
from typing import Optional

class StatusEmpleadoRequest(BaseModel):
    Nombre:str


class InasistenciaRequest(BaseModel):
    IdEmpleado:int
    FechaInicial:datetime
    FechaFinal:datetime
    MotivoInasistencia:str


class PeriodoPlanillaRequest(BaseModel):
    Anio:int
    Mes:int
    Cantidad:int


class CuentaBancariaEmpleadoRequest(BaseModel):
    IdEmpleado:int
    IdBanco:int
    NumeroDeCuenta:str


class NuevoEmpleadoRequest(BaseModel):
    Nombre:str
    Apellido:str
    FechaNacimiento:date
    IdGenero:int
    IdEstadoCivil:int
    Direccion:str
    Telefono:str
    CorreoElectronico:str
    IdSucursal:int
    IdPuesto:int
    FechaContratacion:date
    IdStatusEmpleado:int
    IngresoSueldoBase:float
    IngresoBonificacionDecreto:float
    IngresoOtrosIngresos:float
    DescuentoIgss:float
    DescuentoIsr:float
    DescuentoInasistencias:float

class EditarEmpleadoRequest(BaseModel):
    IdEmpleado:int
    IdPersona:int
    Nombre:str
    Apellido:str
    FechaNacimiento:date
    IdGenero:int
    IdEstadoCivil:int
    Direccion:str
    Telefono:str
    CorreoElectronico:str
    IdSucursal:int
    IdPuesto:int
    FechaContratacion:date
    IdStatusEmpleado:int
    IngresoSueldoBase:float
    IngresoBonificacionDecreto:float
    IngresoOtrosIngresos:float
    DescuentoIgss:float
    DescuentoIsr:float
    DescuentoInasistencias:float

class EmpleadoRequest(BaseModel):
    IdEmpleado:int
    IdPersona:int
    IdSucursal:int
    FechaContratacion:date
    IdPuesto:int
    IdStatusEmpleado:int
    IngresoSueldoBase:float
    IngresoBonificacionDecreto:float
    IngresoOtrosIngresos:float
    DescuentoIgss:float
    DescuentoIsr:float
    DescuentoInasistencias:float


class PlanillaCabeceraRequest(BaseModel):
    Anio:int
    Mes:int