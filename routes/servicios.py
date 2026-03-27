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

@router.post("/registrar-mascota")
def registrar_mascota(payload: MascotaRegistro):
    data = payload.dict()
    mascotas_db.append(data)
    return {"mensaje": "Mascota registrada correctamente", "mascota": data}

@router.get("/mascotas/{correo}")
def listar_mascotas(correo: str):
    mascotas = [m for m in mascotas_db if m["correo"] == correo]
    return {"correo": correo, "mascotas": mascotas}

@router.get("/reporte/{correo}")
def reporte_por_usuario(correo: str):
    mascotas = [m for m in mascotas_db if m["correo"] == correo]
    if not mascotas:
        raise HTTPException(status_code=404, detail="No se encontraron mascotas para ese correo")

    servicios = [m["tipo_servicio"] for m in mascotas]
    total_gastado = 0.0
    detalle = []

    for m in mascotas:
        servicio_encontrado = next((s for s in servicios_db if s["nombre"] == m["tipo_servicio"]), None)
        precio = servicio_encontrado["precio"] if servicio_encontrado else 0.0
        total_gastado += precio
        detalle.append({
            "mascota": m["nombre_mascota"],
            "servicio": m["tipo_servicio"],
            "fecha": m["fecha"],
            "precio": precio,
        })

    return {
        "correo": correo,
        "cantidad_servicios": len(mascotas),
        "servicios": servicios,
        "total_gastado": total_gastado,
        "detalle": detalle,
    }

