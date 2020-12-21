from typing import Dict
from pydantic import BaseModel

class reserva(BaseModel):
    id: int 
    no_reserva: int
    hotel: str
    habitacion: int
    no_personas: int
    dias: int
    precio: float
    adicionales: bool
    pago: bool

database_reservas = Dict[int, reserva]

database_reservas = {10:reserva(**{"id": 100,
                                "no_reserva": 1,
                                "hotel": "Ciudad Bonita",
                                "habitacion": 302,
                                "no_personas": 2,
                                "dias": 1,
                                "precio": 100000,
                                "adicionales": False,
                                "pago": True}),
                     11:reserva(**{"id": 101,
                                "no_reserva": 2,
                                "hotel": "Dan Carton",
                                "habitacion": 1001,
                                "no_personas": 1,
                                "dias": 5,
                                "precio": 150000,
                                "adicionales": True,
                                "pago": True}),
                     12:reserva(**{"id": 102,
                                "no_reserva": 3,
                                "hotel": "Holyday Inn",
                                "habitacion": 205,
                                "no_personas": 3,
                                "dias": 2,
                                "precio": 180000,
                                "adicionales": False,
                                "pago": False}),
                    }      

def get_reserva(llave: int):
    if llave in database_reservas.keys():
        return database_reservas[llave]
    else:
        return None

def update_reserva(reserva_no: reserva):
    database_reservas[reserva_no.id] = reserva_no
    return reserva_no


''' def create_reserva(new_reserva: reserva):
    new_reserva.id = reservaID,
    new_reserva.no_reserva = reservaRESERVA,
    new_reserva.hotel = reservaHOTEL,
    new_reserva.habitacion = reservaHABITACION,
    new_reserva.no_personas = reservaPERSONAS,
    new_reserva.dias = reservaDIAS,
    new_reserva.precio = reservaPRECIO,
    new_reserva.adicionales = reservaADICIONALES,
    new_reserva.pago = reservaPAGO

    database_reservas.append(new_reserva)

    return new_reserva '''
