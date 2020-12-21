from fastapi import FastAPI
from pydantic import BaseModel

from models.cliente_model import ClienteIn, ClienteOut
from db.clientes_db import cliente
from db.clientes_db import get_cliente, update_cliente

from models.reserva_model import ReservaIn, ReservaOut, ReservaInCreate
from db.reserva_db import reserva
from db.reserva_db import get_reserva, update_reserva

from fastapi import HTTPException

app = FastAPI()

##READ CLIENTE
@app.get("/cliente/{cliente_id}")
async def cliente_get(cliente_id: int):
    cliente_in = get_cliente(cliente_id)
    if cliente_in == None:
        raise HTTPException(status_code=404,
                detail= "El cliente no se encuentra hospedado ni con reserva")
    cliente_out = ClienteOut(**cliente_in.dict())
    return cliente_out

##READ RESERVA
@app.get("/reserva/{reserva_id}")
async def reserva_get(reserva_id: int):
    reserva_in = get_reserva(reserva_id)
    if reserva_in == None:
        raise HTTPException(status_code=404,
                detail= "La reversa no existe")
    reserva_out = ReservaOut(**reserva_in.dict())
    return reserva_out

##UPDATE CLIENTE
@app.put("/cliente/{cliente_id}")
async def cliente_update(cliente_id: int, cliente: ClienteIn):
    cliente_in = get_cliente(cliente_id)
    if cliente_in == None:
        raise HTTPException(status_code=404,
                detail= "El cliente no se encuentra hospedado ni con reserva")
    
    if cliente_in.hospedado_act == False and cliente.hospedado_act == True:
        cliente_in.habitacion = cliente.habitacion
        cliente_in.hospedado_act = cliente.hospedado_act
    
    if cliente_in.hospedado_act == True and cliente.hospedado_act == False:
        cliente_in.habitacion = 0
        cliente_in.hospedado_act = False
    
    update_cliente(cliente_in)
    cliente_out = ClienteOut(**cliente_in.dict())
    return cliente_out

##UPDATE RESERVA
@app.put("/reserva/{reserva_id}")
async def reserva_update(reserva_id: int, reserva: ReservaIn):
    reserva_in = get_reserva(reserva_id)
    if reserva_in == None:
        raise HTTPException(status_code=404,
                detail= "La reserva no existe")
    
    if reserva_in.adicionales == False and reserva.adicionales == True:
        reserva_in.adicionales = reserva.adicionales
        reserva_in.precio = reserva_in.precio + reserva.precio_adic
       
    update_reserva(reserva_in)
    reserva_out = ReservaOut(**reserva_in.dict())
    return reserva_out

''' ##CREATE RESERVA
@app.post("/reserva/")
async def reserva_create(reserva: ReservaInCreate):
    return ReservaInCreate '''
