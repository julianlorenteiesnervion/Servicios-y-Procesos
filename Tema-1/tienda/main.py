from fastapi import FastAPI
from routers import empleado, tienda

app = FastAPI()

# Routers
app.include_router(empleado.router)
app.include_router(tienda.router)



@app.get("/")
def inicio():
    return {"hello": "world"}