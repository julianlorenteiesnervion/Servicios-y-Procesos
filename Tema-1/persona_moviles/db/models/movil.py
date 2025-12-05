from typing import Optional
from pydantic import BaseModel

# Entidad Móvil
class Movil(BaseModel):
    id: Optional[int] = None
    precio_coste: float
    precio_venta: float
    id_persona: int