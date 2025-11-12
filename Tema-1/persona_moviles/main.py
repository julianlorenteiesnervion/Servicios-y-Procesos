from fastapi import FastAPI
from routers import persona, movil, auth_users
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Routers
app.include_router(persona.router)
app.include_router(movil.router)
app.include_router(auth_users.router)

@app.get("/")
def inicio():
    return {"hello": "world"}
