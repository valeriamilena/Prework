from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Dict

router = APIRouter(prefix="", tags=["auth"])

class AuthPayload(BaseModel):
    correo: str
    contraseña: str

usuarios_db: List[Dict] = []

@router.post("/register")
def register(payload: AuthPayload):
    usuario = payload.dict()
    usuarios_db.append(usuario)
    return {"mensaje": "Registro exitoso", "usuario": usuario}

@router.post("/login")
def login(payload: AuthPayload):
    intento = payload.dict()
    encontrado = next((u for u in usuarios_db if u["correo"] == intento["correo"] and u["contraseña"] == intento["contraseña"]), None)
    if not encontrado:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    return {"mensaje": "Login exitoso", "usuario": encontrado}
