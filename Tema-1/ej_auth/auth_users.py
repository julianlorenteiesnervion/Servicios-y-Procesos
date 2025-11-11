from pydantic import BaseModel
from fastapi import APIRouter, HTTPException

import jwt

from jwt.exceptions import InvalidTokenError
from pwdlib import PasswordHash
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

# Definimos el algoritmo de encriptación
ALGORITHM = "HS256"

# Duracion del token
ACCESS_TOKEN_EXPIRE_MINUTES = 1

# Clvae que se utilizará como semilla para generar el token
# openssl rand -hex 32
SECRET_KEY = "c0eb8d787d232548495488ded4aecda962e8fb6677d02dea465b2d62b5eebac7"

# Objeto que se utilizará para el cálculo del hash y la verificación de las contraseñas
password_hash = PasswordHash.recommended()

router = APIRouter()

class User(BaseModel):
    username: str
    fullname: str
    email: str
    disabled: bool

class UserDB(User):
    password: str

users_db = {
    "elenarg": {
        "username" : "elenarg",
        "fullname" : "Elena Rivero",
        "email" : "elena@prueba.es",
        "disabled" : False,
        "password" : "123456"
    },
    "julian": {
        "username" : "julianlorenteiesnervion",
        "fullname" : "Julián Lorente",
        "email" : "julian.lorente@iesnervion.es",
        "disabled" : False,
        "password" : "238904"
    }
}

@router.post("/register", status_code=201)
def register(user: UserDB):
    if user.username not in users_db:
        hashed_password = password_hash.hash(user.password)
        user.password = hashed_password
        users_db[user.username] = user
        return user
    else:
        raise HTTPException(status_code=409, detail="User already exists")
    
@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user = users_db.get(form.username)
    
    if user:
        if password_hash.verify(form.password, user['password']):
            expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
            access_token = {"sub": user.username, "exp": expire}

            token = jwt.encode(access_token, SECRET_KEY, algorithm=ALGORITHM)
            return {"access_token": token, "token_type": "bearer"}
    raise HTTPException(status_code=401, detail="Invalid username or password")
