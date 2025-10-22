from fastapi import FastAPI, HTTPException
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

#region Métodos get
# Obtener todas las tiendas
@app.get("/tiendas")
def tiendas():
    return lista_tiendas

# Obtener tienda por id
@app.get("/tiendas/id/{id}")
def tienda_id(id: int):
    return obtener_tienda_por_id(id)

# Obtener tienda por domicilio
@app.get("/tiendas/domicilio/{domicilio}")
def tienda_domicilio(domicilio: str):
    return obtener_tienda_por_domicilio(domicilio)

# Obtener tienda por telefono
@app.get("/tiendas/telefono/{telefono}")
def tienda_telefono(telefono: int):
    return obtener_tienda_por_telefono(telefono)

# Obtener tiendas por precio de alquiler
@app.get("/tiendas/precio_alquiler/{precio_alquiler}")
def tienda_precio_alquiler(precio_alquiler: int):
    return obtener_tiendas_por_precio_alquiler(precio_alquiler)

#endregion

#region Métodos post
# Añadir una tienda
@app.post("/tiendas", status_code = 201, response_model = Tienda)
def add_tienda(tienda: Tienda):

    # Calculamos la siguiente id y machacamos la que llegó en la tienda por parámetro de entrada
    tienda.id = ultima_id()

    # Añadimos la tienda con su nueva id a la lista de tiendas
    lista_tiendas.append(tienda)

    # Devolvemos la tienda
    return tienda

#endregion

#region Métodos put
# Método para modificar una tienda
@app.put("/tiendas/id/{id}")
def modificar_tienda(id: int, tienda: Tienda):
    for index, saved_tienda in enumerate(lista_tiendas):
        if saved_tienda.id == id:
            tienda.id = id
            lista_tiendas[index] = tienda
            return tienda
        
    raise HTTPException(status_code = 404, detail = "Tienda no encontrada")

#endregion

#region Métodos delete
# Método para eliminar una tienda
@app.delete("/tiendas/id/{id}")
def eliminar_tienda(id: int):
    for saved_tienda in lista_tiendas:
        if saved_tienda.id == id:
            lista_tiendas.remove(saved_tienda)
            return {}
    raise HTTPException(status_code = 404, detail = "Tienda no encontrada.")

#endregion

#region Métodos internos
# Método para la búsqueda de tiendas por id
def obtener_tienda_por_id(id: int):
    for tienda in lista_tiendas:
        if tienda.id == id:
            return tienda
    
    return {"Error": "No se ha encontrado ninguna tienda por la id " + id}

# Método para obtener tiendas por domicilio
def obtener_tienda_por_domicilio(domicilio: str):
    for tienda in lista_tiendas:
        if tienda.domicilio == domicilio:
            return tienda
        
    return {"Error": "No se ha encontrado ninguna tienda por el domicilio " + domicilio}

# Método para obtener tiendas por teléfono
def obtener_tienda_por_telefono(telefono: int):
    for tienda in lista_tiendas:
        if tienda.telefono == telefono:
            return tienda
    
    return {"Error": "No se ha encontrado ninguna tienda por el teléfono " + telefono}

# Método para obtener tiendas por el precio del alquiler
def obtener_tiendas_por_precio_alquiler(precio_alquiler: int):
    tiendas_por_precio_alquiler = []

    for tienda in lista_tiendas:
        if tienda.precio_alquiler == precio_alquiler:
            tiendas_por_precio_alquiler.append(tienda)
    
    return tiendas_por_precio_alquiler

# Método para obtener la última id
def ultima_id():
    return (max(lista_tiendas, key = id).id + 1)

#endregion
