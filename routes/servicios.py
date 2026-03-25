from fastapi import APIRouter
from typing import List, Dict

router = APIRouter(prefix="/servicios", tags=["servicios"])

servicios_db: List[Dict] = [
    {"nombre": "consulta", "precio": 50},
    {"nombre": "baño", "precio": 60},
    {"nombre": "corte", "precio": 100},
]

@router.get("/")
def listar_servicios():
    return {"servicios": servicios_db}

@router.post("/")
def agregar_servicio(nuevo: Dict):
    servicios_db.append(nuevo)
    return {"mensaje": "¡Servicio guardado!", "servicio": nuevo}
