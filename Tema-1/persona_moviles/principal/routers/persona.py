from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/personas",
                   tags=["personas"])

# Entidad persona
class Persona(BaseModel):
    id: int
    dni: str
    nombre: str
    apellidos: str
    telefono: int
    correo: str

# Lista de personas
lista_personas = [
    Persona(id=1, dni="12345678A", nombre="Carlos", apellidos="García López", telefono=612345678, correo="carlos.garcia@example.com"),
    Persona(id=2, dni="23456789B", nombre="María", apellidos="Pérez Sánchez", telefono=622345679, correo="maria.perez@example.com"),
    Persona(id=3, dni="34567890C", nombre="Lucía", apellidos="Martínez Díaz", telefono=632345680, correo="lucia.martinez@example.com"),
    Persona(id=4, dni="45678901D", nombre="Javier", apellidos="Fernández Gómez", telefono=642345681, correo="javier.fernandez@example.com"),
    Persona(id=5, dni="56789012E", nombre="Ana", apellidos="Ruiz Romero", telefono=652345682, correo="ana.ruiz@example.com"),
    Persona(id=6, dni="67890123F", nombre="David", apellidos="Santos Ortega", telefono=662345683, correo="david.santos@example.com"),
    Persona(id=7, dni="78901234G", nombre="Laura", apellidos="Navarro Molina", telefono=672345684, correo="laura.navarro@example.com"),
    Persona(id=8, dni="89012345H", nombre="Miguel", apellidos="Torres Castillo", telefono=682345685, correo="miguel.torres@example.com"),
    Persona(id=9, dni="90123456I", nombre="Sofía", apellidos="Jiménez León", telefono=692345686, correo="sofia.jimenez@example.com"),
    Persona(id=10, dni="01234567J", nombre="Alejandro", apellidos="Vázquez Cruz", telefono=602345687, correo="alejandro.vazquez@example.com"),
    Persona(id=11, dni="11234568K", nombre="Paula", apellidos="Morales Herrera", telefono=613456788, correo="paula.morales@example.com"),
    Persona(id=12, dni="21234569L", nombre="Raúl", apellidos="Domínguez Castro", telefono=623456789, correo="raul.dominguez@example.com"),
    Persona(id=13, dni="31234570M", nombre="Elena", apellidos="Gil Serrano", telefono=633456790, correo="elena.gil@example.com"),
    Persona(id=14, dni="41234571N", nombre="Andrés", apellidos="Reyes Nieto", telefono=643456791, correo="andres.reyes@example.com"),
    Persona(id=15, dni="51234572O", nombre="Carmen", apellidos="Ortega Ramos", telefono=653456792, correo="carmen.ortega@example.com"),
    Persona(id=16, dni="61234573P", nombre="Hugo", apellidos="López Cabrera", telefono=663456793, correo="hugo.lopez@example.com"),
    Persona(id=17, dni="71234574Q", nombre="Natalia", apellidos="Flores Marín", telefono=673456794, correo="natalia.flores@example.com"),
    Persona(id=18, dni="81234575R", nombre="Sergio", apellidos="Ramos Vega", telefono=683456795, correo="sergio.ramos@example.com"),
    Persona(id=19, dni="91234576S", nombre="Isabel", apellidos="Cano Blanco", telefono=693456796, correo="isabel.cano@example.com"),
    Persona(id=20, dni="02134577T", nombre="Pablo", apellidos="Romero Navarro", telefono=603456797, correo="pablo.romero@example.com"),
]

#region Métodos get
# Método get para obtener todas las personas
@router.get("/")
def personas():
    return lista_personas

# Método get para obtener una persona mediante su id
@router.get("/id/{id}")
def personas_id(id: int):
    return obtener_persona_id(id)

# Método get para obtener una persona mediante su DNI
@router.get("/dni/{dni}")
def personas_dni(dni: str):
    return obtener_persona_dni(dni)

# Método get para obtener personas mediante un nombre
@router.get("/nombre/{nombre}")
def personas_nombre(nombre: str):
    return obtener_personas_nombre(nombre)

# Método get para obtener personas mediante los apellidos
@router.get("/apellidos/{apellidos}")
def personas_apellidos(apellidos: str):
    return obtener_personas_apellidos(apellidos)

# Método get para obtener una persona mediante su teléfono
@router.get("/telefono/{telefono}")
def personas_telefono(telefono: int):
    return obtener_persona_telefono(telefono)

@router.get("/correo/{correo}")
def personas_correo(correo: str):
    return obtener_persona_correo(correo)

#endregion

#region Métodos internos
# Método para obtener una persona mediante su id
def obtener_persona_id(id: int):
    for persona in lista_personas:
        if persona.id == id:
            return persona
        
    raise HTTPException(status_code=404, detail=f"No se ha encontrado ninguna persona con la id {id}")

# Método para obtener una persona mediante su DNI
def obtener_persona_dni(dni: int):
    for persona in lista_personas:
        if persona.dni == dni:
            return persona
        
    raise HTTPException(status_code=404, detail=f"No se ha encontrado ninguna persona con el DNI {dni}")

# Método para obtener personas mediante el nombre
def obtener_personas_nombre(nombre: str):
    personas = []

    for persona in lista_personas:
        if persona.nombre == nombre:
            personas.append(persona)
    
    if not personas:
        raise HTTPException(status_code=404, detail=f"No se ha encontrado ninguna persona con el nombre {nombre}")

    return personas

# Método para obtener personas mediante los apellidos
def obtener_personas_apellidos(apellidos: str):
    personas = []

    for persona in lista_personas:
        if persona.apellidos == apellidos:
            personas.append(persona)
    
    if not personas:
        raise HTTPException(status_code=404, detail=f"No se ha encontrado ninguna persona con los apellidos {apellidos}")

    return personas

# Método para obtener una persona mediante su teléfono
def obtener_persona_telefono(telefono: int):
    for persona in lista_personas:
        if persona.telefono == telefono:
            return persona
        
    raise HTTPException(status_code=404, detail=f"No se ha encontrado ninguna persona con el teléfono {telefono}")

# Método para obtener una persona mediante su correo electrónico
def obtener_persona_correo(correo: str):
    for persona in lista_personas:
        if persona.correo == correo:
            return persona
        
    raise HTTPException(status_code=404, detail=f"No se ha encontrado ninguna persona con el correo {correo}")

#endregion