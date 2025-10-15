from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()

# Entidad tienda
class Tienda(BaseModel):
    id:int
    domicilio:str
    telefono:int
    precio_alquiler:int

# Direcciones de domicilios
domicilios = [
    "Av. Reforma 123", "Calle Juárez 45", "Boulevard Insurgentes 678",
    "Calle Hidalgo 12", "Av. Universidad 234", "Calle Morelos 56",
    "Av. Central 789", "Calle Independencia 90", "Boulevard Benito Juárez 321",
    "Calle Zaragoza 67", "Av. Madero 101", "Calle 5 de Mayo 202",
    "Boulevard López Mateos 303", "Calle Allende 404", "Av. Las Palmas 505",
    "Calle Matamoros 606", "Boulevard Miguel Alemán 707", "Calle Victoria 808",
    "Av. Constitución 909", "Calle Lerdo 100"
]

# Lista de tiendas
lista_tiendas = [
    Tienda(
        id=i+1,
        domicilio=domicilios[i],
        telefono=random.randint(5500000000, 5599999999),
        precio_alquiler=random.randint(5000, 25000)
    )
    for i in range(20)
]

# Métodos get
# Obtener todas las tiendas
@app.get("/tiendas")
def tiendas():
    return lista_tiendas

# Obtener tienda por id
@app.get("/tiendas/id/{id}")
def tiendaId(id: int):
    return obtenerTiendaPorId(id)

# Obtener tienda por domicilio
@app.get("/tiendas/domicilio/{domicilio}")
def tiendaDomicilio(domicilio: str):
    return obtenerTiendaPorDomicilio(domicilio)

# Obtener tienda por telefono
@app.get("/tiendas/telefono/{telefono}")
def tiendaTelefono(telefono: int):
    return obtenerTiendaPorTelefono(telefono)

# Obtener tiendas por precio de alquiler
@app.get("/tiendas/precio_alquiler/{precio_alquiler}")
def tiendaPrecioAlquiler(precio_alquiler: int):
    return obtenerTiendasPorPrecioAlquiler(precio_alquiler)

# Métodos internos
# Método para la búsqueda de tiendas por id
def obtenerTiendaPorId(id: int):
    for tienda in lista_tiendas:
        if tienda.id == id:
            return tienda
    
    return {"Error": "No se ha encontrado ninguna tienda por la id " + id}

# Método para obtener tiendas por domicilio
def obtenerTiendaPorDomicilio(domicilio: str):
    for tienda in lista_tiendas:
        if tienda.domicilio == domicilio:
            return tienda
        
    return {"Error": "No se ha encontrado ninguna tienda por el domicilio " + domicilio}

# Método para obtener tiendas por teléfono
def obtenerTiendaPorTelefono(telefono: int):
    for tienda in lista_tiendas:
        if tienda.telefono == telefono:
            return tienda
    
    return {"Error": "No se ha encontrado ninguna tienda por el teléfono " + telefono}

# Método para obtener tiendas por el precio del alquiler
def obtenerTiendasPorPrecioAlquiler(precio_alquiler: int):
    tiendasPorPrecioAlquiler = []

    for tienda in lista_tiendas:
        if tienda.precio_alquiler == precio_alquiler:
            tiendasPorPrecioAlquiler.append(tienda)
    
    return tiendasPorPrecioAlquiler
