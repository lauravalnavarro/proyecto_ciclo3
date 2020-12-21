from pydantic import BaseModel
from datetime import datetime

class EgresoIn(BaseModel):
    tipo: str
    valor: float

class EgresoOut(BaseModel):
    id_egreso: int
    tipo: str
    valor: float
    fecha: datetime
