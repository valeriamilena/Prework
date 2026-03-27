from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Dict

router = APIRouter(tags=["servicios"])

servicios_db: List[Dict] = [
    {"nombre": "consulta", "precio": 50},
    {"nombre": "baño", "precio": 60},
    {"nombre": "corte", "precio": 100},
]

mascotas_db: List[Dict] = []

class ServicioItem(BaseModel):
    nombre: str
    precio: float

class MascotaRegistro(BaseModel):
    correo: str
    nombre_mascota: str
    tipo_servicio: str
    fecha: str

@router.get("/servicios")
def listar_servicios():
    return {"servicios": servicios_db}

@router.post("/servicios")
def agregar_servicio(nuevo: ServicioItem):
    servicio = nuevo.dict()
    servicios_db.append(servicio)
    return {"mensaje": "¡Servicio guardado!", "servicio": servicio}

