from pydantic import BaseModel

class ReservaIn(BaseModel):
    adicionales: bool
    precio_adic: float

''' class ReservaInCreate(BaseModel):
    no_reserva: int
    hotel: str
    habitacion: int
    no_personas: int
    dias: int
    precio: float
    adicionales: bool
    pago: bool '''

class ReservaOut(BaseModel):
    no_reserva: int
    hotel: str
    dias: int
    precio: float    
    pago: bool