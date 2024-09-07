from pydantic import BaseModel

class LoginRequest(BaseModel):
    IdUsuario:str
    Password:str