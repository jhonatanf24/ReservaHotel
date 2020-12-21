from pydantic import BaseModel

class ClienteIn(BaseModel):
    hospedado_act : bool
    habitacion: int 

class ClienteOut(BaseModel):
    nombre: str
    hospedado_act: bool
    habitacion: int