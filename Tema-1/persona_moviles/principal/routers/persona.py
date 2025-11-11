from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import random

# Router
router = APIRouter()

# Entidad Persona
class Persona(BaseModel):
    id: int
    dni: str
    nombre: str
    apellidos: str
    telefono: int
    correo: str


# Listas de nombres y apellidos
nombres = [
    "Carlos", "María", "José", "Ana", "Luis", "Laura",
    "Miguel", "Lucía", "Javier", "Sofía", "Diego", "Marta"
]

apellidos = [
    "García", "López", "Martínez", "Pérez", "Gómez",
    "Sánchez", "Romero", "Díaz", "Torres", "Ruiz", "Moreno", "Vargas"
]

# Lista de personas
lista_personas = [
    Persona(
        id=i+1,
        dni=f"{random.randint(10000000, 99999999)}{random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}",
        nombre=nombres[i % len(nombres)],
        apellidos=apellidos[i % len(apellidos)],
        telefono=random.randint(600000000, 699999999),
        correo=f"{nombres[i % len(nombres)].lower()}.{apellidos[i % len(apellidos)].lower()}@correo.com"
    )
    for i in range(20)
]

#region Métodos GET
# Obtener todas las personas
@router.get("/personas")
def personas():
    return lista_personas

# Obtener persona por id
@router.get("/personas/id/{id}")
def persona_id(id: int):
    return obtener_persona_por_id(id)

# Obtener persona por nombre
@router.get("/personas/nombre/{nombre}")
def persona_nombre(nombre: str):
    return obtener_personas_por_nombre(nombre)

# Obtener persona por apellidos
@router.get("/personas/apellidos/{apellidos}")
def persona_apellidos(apellidos: str):
    return obtener_personas_por_apellidos(apellidos)

# Obtener persona por teléfono
@router.get("/personas/telefono/{telefono}")
def persona_telefono(telefono: int):
    return obtener_persona_por_telefono(telefono)

# Obtener persona por correo
@router.get("/personas/correo/{correo}")
def persona_correo(correo: str):
    return obtener_persona_por_correo(correo)

#endregion

#region Métodos POST
# Añadir una persona
@router.post("/personas", status_code=201, response_model=Persona)
def add_persona(persona: Persona):
    persona.id = ultima_id()
    lista_personas.append(persona)
    return persona
#endregion

#region Métodos PUT
# Modificar persona
@router.put("/personas/id/{id}")
def modificar_persona(id: int, persona: Persona):
    for index, saved_persona in enumerate(lista_personas):
        if saved_persona.id == id:
            persona.id = id
            lista_personas[index] = persona
            return persona
    raise HTTPException(status_code=404, detail="Persona no encontrada")
#endregion

#region Métodos DELETE
# Eliminar persona
@router.delete("/personas/id/{id}")
def eliminar_persona(id: int):
    for saved_persona in lista_personas:
        if saved_persona.id == id:
            lista_personas.remove(saved_persona)
            return {}
    raise HTTPException(status_code=404, detail="Persona no encontrada.")
#endregion

#region Métodos internos
def obtener_persona_por_id(id: int):
    for persona in lista_personas:
        if persona.id == id:
            return persona
    return {"Error": f"No se ha encontrado ninguna persona por la id {id}"}

def obtener_personas_por_nombre(nombre: str):
    personas_encontradas = [p for p in lista_personas if p.nombre.lower() == nombre.lower()]
    return personas_encontradas if personas_encontradas else {"Error": f"No se han encontrado personas con el nombre {nombre}"}

def obtener_personas_por_apellidos(apellidos: str):
    personas_encontradas = [p for p in lista_personas if p.apellidos.lower() == apellidos.lower()]
    return personas_encontradas if personas_encontradas else {"Error": f"No se han encontrado personas con los apellidos {apellidos}"}

def obtener_persona_por_telefono(telefono: int):
    for persona in lista_personas:
        if persona.telefono == telefono:
            return persona
    return {"Error": f"No se ha encontrado ninguna persona con el teléfono {telefono}"}

def obtener_persona_por_correo(correo: str):
    for persona in lista_personas:
        if persona.correo.lower() == correo.lower():
            return persona
    return {"Error": f"No se ha encontrado ninguna persona con el correo {correo}"}

def ultima_id():
    return max(lista_personas, key=lambda x: x.id).id + 1
#endregion
