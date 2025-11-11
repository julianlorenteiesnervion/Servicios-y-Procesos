from fastapi import FastAPI
from routers import persona, movil
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Routers
app.include_router(persona.router)
app.include_router(movil.router)

# Carpeta estática
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def inicio():
    return {"hello": "world"}
