from datetime import date, datetime
from pydantic.types import ConstrainedStr
from models import egreso
from pydantic import BaseModel
from typing import Dict

class EgresoInDB(BaseModel):
    id_egreso: int = 0
    tipo: str
    valor: int
    fecha: datetime = datetime.now()


tipos_validos = ['emergencias', 'alimentacion', 'ocio', 'vivienda', 'comunicacion', 
                 'vehiculo', 'transporte', 'compras', 'salud', 'impuestos']

database_egresos = {
    1: EgresoInDB(**{"id_egreso": 1,
                     "tipo": "transporte",
                     "valor": 2400,
                     "fecha": datetime.today()})
}
generator = {'id': 1}

def save_egresos(egreso_in_db: EgresoInDB):
    generator['id'] = generator['id'] + 1
    egreso_in_db.id_egreso = generator['id']
    database_egresos[generator['id']] = egreso_in_db
    return egreso_in_db

def get_egresos(id: int):
    if id in database_egresos.keys():
        return database_egresos[id]
    else: 
        return None

def update_egresos(egreso_in_db: EgresoInDB, database_egresos: dict):
    egreso_in_db[egreso_in_db.id_egreso] = egreso_in_db
    return egreso_in_db


