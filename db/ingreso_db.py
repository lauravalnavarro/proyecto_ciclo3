from pydantic.types import ConstrainedStr
from models import egreso
from pydantic import BaseModel
from typing import Dict

class IngresoInDB(BaseModel):
    id_ingreso: int = 0
    tipo: str
    valor: int
    constante: bool


tipos_validos = ['salario', 'ocasional', 'inversion']

database_ingresos = {
    "salario": IngresoInDB(**{"id_ingreso": 101,
                        "tipo": "salario",
                        "valor": 100000,
                        "constante": False}),
    "ocasional": IngresoInDB(**{"id_ingreso": 102,
                        "tipo": "ocasional",
                        "valor": 0,
                        "constante": False}),
    "inversion": IngresoInDB(**{"id_ingreso": 103,
                            "tipo": "inversion",
                            "valor": 0,
                            "constante": False}),
}

generator = {'id': 102}


print( database_ingresos["salario"].valor)

def save_ingresos(ingreso_in_db: IngresoInDB):
    database_ingresos[ingreso_in_db.tipo].valor += ingreso_in_db.valor

    return ingreso_in_db

def get_ingresos(id: str):
    if id in database_ingresos.keys():
        return database_ingresos[id]
    else: 
        return None

def update_ingresos(ingreso_in_db: IngresoInDB, database_ingresos: dict):
    ingreso_in_db[ingreso_in_db.id_ingreso] = ingreso_in_db
    return ingreso_in_db
