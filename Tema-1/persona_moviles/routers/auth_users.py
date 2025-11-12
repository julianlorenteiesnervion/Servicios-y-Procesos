from pydantic import BaseModel
from datetime import *
import jwt
from jwt.exceptions import InvalidTokenError
from pwdlib import PasswordHash
from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer


oauth2 = OAuth2PasswordBearer(tokenUrl="login")

# Algoritmo de encriptación
ALGORITHM = "HS256"

# Duración del token
ACCESS_TOKEN_EXPIRE_MINUTES = 1

# Clave secreta
SECRET_KEY = "c0eb8d787d232548495488ded4aecda962e8fb6677d02dea465b2d62b5eebac7"

# Para generar/verificar contraseñas
password_hash = PasswordHash.recommended()

router = APIRouter()

# ---------------------------
# MODELOS
# ---------------------------
class User(BaseModel):
    username: str
    fullname: str
    email: str
    disabled: bool

class UserDB(User):
    password: str

# ---------------------------
# BASE DE DATOS FALSA
# ---------------------------
# Solo guardamos diccionarios, no objetos
users_db = {
    "elenarg": {
        "username": "elenarg",
        "fullname": "Elena Rivero",
        "email": "elena@prueba.es",
        "disabled": False,
        "password": password_hash.hash("123456")
    },
    "julianlorenteiesnervion": {
        "username": "julianlorenteiesnervion",
        "fullname": "Julián Lorente",
        "email": "julian.lorente@iesnervion.es",
        "disabled": False,
        "password": password_hash.hash("238904")
    }
}

# ---------------------------
# ENDPOINTS
# ---------------------------

@router.post("/register", status_code=201)
def register(user: UserDB):
    if user.username not in users_db:
        hashed_password = password_hash.hash(user.password)
        users_db[user.username] = {
            "username": user.username,
            "fullname": user.fullname,
            "email": user.email,
            "disabled": user.disabled,
            "password": hashed_password
        }
        return user
    else:
        raise HTTPException(status_code=409, detail="User already exists")
    

@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_data = users_db.get(form.username)

    if not user_data:
        raise HTTPException(status_code=401, detail="Invalid username or password")

    # Creamos el objeto UserDB dinámicamente a partir del diccionario
    user = UserDB(**user_data)

    try:
        if password_hash.verify(form.password, user.password):
            expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
            access_token = {"sub": user.username, "exp": expire}
            token = jwt.encode(access_token, SECRET_KEY, algorithm=ALGORITHM)
            return {"access_token": token, "token_type": "bearer"}
        else:
            raise HTTPException(status_code=401, detail="Invalid username or password")

    except Exception:
        raise HTTPException(status_code=401, detail="Error al verificar la contraseña")
