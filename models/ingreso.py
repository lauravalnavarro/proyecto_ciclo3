from pydantic import BaseModel

class IngresoIn(BaseModel):
    tipo: str
    valor: float
    constante: bool

class IngresoOut(BaseModel):
    id_ingreso: int
    tipo: str
    valor: float
