from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import random

app = FastAPI()

# Entidad empleado
class Empleado(BaseModel):
    id: int
    nombre: str
    apellidos: str
    telefono: int
    correo: str
    num_cuenta: str
    id_tienda: int

# Listas de nombres y apellidos
nombres = [
    "Carlos", "María", "José", "Ana", "Luis", "Laura", "Miguel", "Lucía", "Javier", "Sofía",
    "Andrés", "Elena", "Pedro", "Marta", "Diego", "Clara", "Raúl", "Irene", "David", "Patricia"
]

apellidos = [
    "García", "López", "Martínez", "Hernández", "Pérez", "Gómez", "Sánchez", "Romero", "Díaz", "Torres",
    "Ruiz", "Flores", "Vargas", "Moreno", "Castro", "Suárez", "Navarro", "Ortega", "Delgado", "Ramos"
]

# Lista de empleados
lista_empleados = [
    Empleado(
        id=i+1,
        nombre=nombres[i],
        apellidos=apellidos[i],
        telefono=random.randint(600000000, 699999999),
        correo=f"{nombres[i].lower()}.{apellidos[i].lower()}@correo.com",
        num_cuenta=f"ES{random.randint(1000, 9999)}{random.randint(1000, 9999)}{random.randint(1000, 9999)}{random.randint(1000, 9999)}",
        id_tienda=random.randint(1, 20)
    )
    for i in range(20)
]

#region Métodos get
# Obtener todos los empleados
@app.get("/empleados")
def empleados():
    return lista_empleados

# Obtener empleado por id
@app.get("/empleados/id/{id}")
def empleado_id(id: int):
    return obtener_empleado_por_id(id)

# Obtener empleado por nombre
@app.get("/empleados/nombre/{nombre}")
def empleado_nombre(nombre: str):
    return obtener_empleados_por_nombre(nombre)

# Obtener empleado por apellidos
@app.get("/empleados/apellidos/{apellidos}")
def empleado_apellidos(apellidos: str):
    return obtener_empleados_por_apellidos(apellidos)

# Obtener empleado por teléfono
@app.get("/empleados/telefono/{telefono}")
def empleado_telefono(telefono: int):
    return obtener_empleado_por_telefono(telefono)

# Obtener empleado por correo
@app.get("/empleados/correo/{correo}")
def empleado_correo(correo: str):
    return obtener_empleado_por_correo(correo)

# Obtener empleados por IdTienda
@app.get("/empleados/id_tienda/{id_tienda}")
def empleados_por_tienda(id_tienda: int):
    return obtener_empleados_por_id_tienda(id_tienda)

#endregion

#region Métodos post
# Añadir un empleado
@app.post("/empleados", status_code = 201, response_model = Empleado)
def add_empleado(empleado: Empleado):

    # Calculamos la siguiente id y machacamos la que llegó en el empleado por parámetro de entrada
    empleado.id = ultima_id()

    # Añadimos el empleado con su nueva id a la lista de empleados
    lista_empleados.append(empleado)

    # Devolvemos el empleado
    return empleado

#endregion

#region Métodos put
# Método para modificar un empleado
@app.put("/empleados/id/{id}")
def modificar_empleado(id: int, empleado: Empleado):
    for index, saved_empleado in enumerate(lista_empleados):
        if saved_empleado.id == id:
            empleado.id = id
            lista_empleados[index] = empleado
            return empleado
        
    raise HTTPException(status_code = 404, detail = "Empleado no encontrado")

#endregion

#region Métodos delete
# Método para eliminar un empleado
@app.delete("/empleados/id/{id}")
def eliminar_empleado(id: int):
    for saved_empleado in lista_empleados:
        if saved_empleado.id == id:
            lista_empleados.remove(saved_empleado)
            return {}
    raise HTTPException(status_code = 404, detail = "Empleado no encontrado.")

#endregion

#region Métodos internos
# Método para la búsqueda de empleados por id
def obtener_empleado_por_id(id: int):
    for empleado in lista_empleados:
        if empleado.id == id:
            return empleado
    
    return {"Error": "No se ha encontrado ningún empleado por la id " + str(id)}

# Método para obtener empleados por nombre
def obtener_empleados_por_nombre(nombre: str):
    empleados_encontrados = [empleado for empleado in lista_empleados if empleado.nombre.lower() == nombre.lower()]
    return empleados_encontrados if empleados_encontrados else {"Error": "No se han encontrado empleados con el nombre " + nombre}

# Método para obtener empleados por apellidos
def obtener_empleados_por_apellidos(apellidos: str):
    empleados_encontrados = [empleado for empleado in lista_empleados if empleado.apellidos.lower() == apellidos.lower()]
    return empleados_encontrados if empleados_encontrados else {"Error": "No se han encontrado empleados con los apellidos " + apellidos}

# Método para obtener empleado por teléfono
def obtener_empleado_por_telefono(telefono: int):
    for empleado in lista_empleados:
        if empleado.telefono == telefono:
            return empleado
    
    return {"Error": "No se ha encontrado ningún empleado por el teléfono " + str(telefono)}

# Método para obtener empleado por correo
def obtener_empleado_por_correo(correo: str):
    for empleado in lista_empleados:
        if empleado.correo.lower() == correo.lower():
            return empleado
    
    return {"Error": "No se ha encontrado ningún empleado con el correo " + correo}

# Método para obtener empleados por id_tienda
def obtener_empleados_por_id_tienda(id_tienda: int):
    empleados_por_tienda = [empleado for empleado in lista_empleados if empleado.id_tienda == id_tienda]
    return empleados_por_tienda if empleados_por_tienda else {"Error": "No se han encontrado empleados para la tienda con id " + str(id_tienda)}

# Método para obtener la última id
def ultima_id():
    return (max(lista_empleados, key = id).id + 1)

#endregion
