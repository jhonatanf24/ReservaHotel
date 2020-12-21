from typing import Dict
from pydantic import BaseModel

class cliente(BaseModel):
    id: int 
    nombre: str
    cedula: int
    habitacion: int
    hospedado_act: bool
    no_reserva: float

database_clientes = Dict[int, cliente]

database_clientes = {100:cliente(**{"id": 100,
                                "nombre": "Juan Cardenas",
                                "cedula": 91265888,
                                "habitacion": 202,
                                "hospedado_act": True,
                                "no_reserva": 123}),
                     101:cliente(**{"id": 101,
                                "nombre": "Pedro Jaimes",
                                "cedula": 91265963,
                                "habitacion": 1002,
                                "hospedado_act": True,
                                "no_reserva": 124}),
                     102:cliente(**{"id": 102,
                                "nombre": "Jaime Diaz",
                                "cedula": 91265887,
                                "habitacion": 0,
                                "hospedado_act": False,
                                "no_reserva": 0}),    
                    }      

def get_cliente(llave: int):
    if llave in database_clientes.keys():
        return database_clientes[llave]
    else:
        return None

def update_cliente(cliente_hotel: cliente):
    database_clientes[cliente_hotel.id] = cliente_hotel
    return cliente_hotel

