from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import random
from db.models.movil import Movil
from db.schemas.movil import movil_schema, movil_schema_list

# Router
router = APIRouter()

# Lista de móviles
lista_moviles = [
    Movil(
        id=i+1,
        precio_coste=round(random.uniform(100, 700), 2),
        precio_venta=round(random.uniform(701, 1200), 2),
        id_persona=random.randint(1, 20)
    )
    for i in range(20)
]

#region Métodos GET
# Obtener todos los móviles
@router.get("/moviles")
def moviles():
    return lista_moviles

# Obtener móvil por id
@router.get("/moviles/id/{id}")
def movil_id(id: int):
    return obtener_movil_por_id(id)

# Obtener móviles por IdPersona
@router.get("/moviles/id_persona/{id_persona}")
def moviles_por_persona(id_persona: int):
    return obtener_moviles_por_id_persona(id_persona)

# Obtener móviles por precio de coste
@router.get("/moviles/precio_coste/{precio_coste}")
def moviles_por_coste(precio_coste: float):
    return obtener_moviles_por_precio_coste(precio_coste)

# Obtener móviles por precio de venta
@router.get("/moviles/precio_venta/{precio_venta}")
def moviles_por_venta(precio_venta: float):
    return obtener_moviles_por_precio_venta(precio_venta)
#endregion

#region Métodos POST
# Añadir un móvil
@router.post("/moviles", status_code=201, response_model=Movil)
def add_movil(movil: Movil):
    movil.id = ultima_id()
    lista_moviles.append(movil)
    return movil
#endregion

#region Métodos PUT
# Modificar móvil
@router.put("/moviles/id/{id}")
def modificar_movil(id: int, movil: Movil):
    for index, saved_movil in enumerate(lista_moviles):
        if saved_movil.id == id:
            movil.id = id
            lista_moviles[index] = movil
            return movil
    raise HTTPException(status_code=404, detail="Móvil no encontrado")
#endregion

#region Métodos DELETE
# Eliminar móvil
@router.delete("/moviles/id/{id}")
def eliminar_movil(id: int):
    for saved_movil in lista_moviles:
        if saved_movil.id == id:
            lista_moviles.remove(saved_movil)
            return {}
    raise HTTPException(status_code=404, detail="Móvil no encontrado.")
#endregion

#region Métodos internos
def obtener_movil_por_id(id: int):
    for movil in lista_moviles:
        if movil.id == id:
            return movil
    return {"Error": f"No se ha encontrado ningún móvil por la id {id}"}

def obtener_moviles_por_id_persona(id_persona: int):
    moviles_encontrados = [m for m in lista_moviles if m.id_persona == id_persona]
    return moviles_encontrados if moviles_encontrados else {"Error": f"No se han encontrado móviles para la persona con id {id_persona}"}

def obtener_moviles_por_precio_coste(precio_coste: float):
    moviles_encontrados = [m for m in lista_moviles if m.precio_coste == precio_coste]
    return moviles_encontrados if moviles_encontrados else {"Error": f"No se han encontrado móviles con precio de coste {precio_coste}"}

def obtener_moviles_por_precio_venta(precio_venta: float):
    moviles_encontrados = [m for m in lista_moviles if m.precio_venta == precio_venta]
    return moviles_encontrados if moviles_encontrados else {"Error": f"No se han encontrado móviles con precio de venta {precio_venta}"}

def ultima_id():
    return max(lista_moviles, key=lambda x: x.id).id + 1
#endregion
