# Pétalos Pet Grooming API 🐾

API FastAPI modular para gestionar servicios de grooming para mascotas, con autenticación de usuarios y registro de servicios.

---

## 📋 Descripción

Este proyecto implementa una arquitectura modular con **APIRouter** de FastAPI, permitiendo:
- ✅ Registro e login de usuarios
- ✅ Gestión de servicios de grooming
- ✅ Registro de mascotas por usuario
- ✅ Reporte de gastos por usuario

---

## 🗂️ Estructura del Proyecto

```
├── main.py                    # Aplicación principal FastAPI
├── README.md                  # Este archivo
├── requirements.txt           # Dependencias del proyecto
└── routes/
    ├── auth.py               # Rutas de autenticación (login, register)
    └── servicios.py          # Rutas de servicios y mascotas
```

---

## 🚀 Instalación

### 1. Clonar el repositorio
```bash
git clone https://github.com/valeriamilena/Prework.git
cd Prework
```

### 2. Crear ambiente virtual
```bash
python -m venv venv
```

### 3. Activar ambiente virtual
**En Windows (PowerShell):**
```powershell
.\venv\Scripts\Activate.ps1
```

**En macOS/Linux:**
```bash
source venv/bin/activate
```

### 4. Instalar dependencias
```bash
pip install -r requirements.txt
```

---

## ▶️ Ejecutar el servidor

```bash
uvicorn main:app --reload
```

La API estará disponible en: `http://127.0.0.1:8000`

**Documentación interactiva:**
- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

---

## 📚 Endpoints Disponibles

### 🔐 Autenticación (`/auth`)

#### POST /register
Registrar un nuevo usuario.

**Body:**
```json
{
  "correo": "usuario@ejemplo.com",
  "contraseña": "micontraseña123"
}
```

**Response:**
```json
{
  "mensaje": "Registro exitoso",
  "usuario": {
    "correo": "usuario@ejemplo.com",
    "contraseña": "micontraseña123"
  }
}
```

---

#### POST /login
Autenticar usuario existente.

**Body:**
```json
{
  "correo": "usuario@ejemplo.com",
  "contraseña": "micontraseña123"
}
```

**Response:**
```json
{
  "mensaje": "Login exitoso",
  "usuario": {
    "correo": "usuario@ejemplo.com",
    "contraseña": "micontraseña123"
  }
}
```

---

### 🛠️ Servicios (`/servicios`)

#### GET /servicios
Listar todos los servicios disponibles.

**Response:**
```json
{
  "servicios": [
    {"nombre": "consulta", "precio": 50},
    {"nombre": "baño", "precio": 60},
    {"nombre": "corte", "precio": 100}
  ]
}
```

---

#### POST /servicios
Agregar un nuevo servicio.

**Body:**
```json
{
  "nombre": "peluqueria",
  "precio": 80
}
```

**Response:**
```json
{
  "mensaje": "¡Servicio guardado!",
  "servicio": {
    "nombre": "peluqueria",
    "precio": 80
  }
}
```

---

#### DELETE /servicios/{nombre}
Eliminar un servicio por nombre.

**Response:**
```json
{
  "mensaje": "Servicio eliminado",
  "servicio": {
    "nombre": "peluqueria",
    "precio": 80
  }
}
```

---

### 🐱 Mascotas

#### POST /registrar-mascota
Registrar una mascota para un usuario.

**Body:**
```json
{
  "correo": "usuario@ejemplo.com",
  "nombre_mascota": "Pelusa",
  "tipo_servicio": "baño",
  "fecha": "2026-03-26"
}
```

**Response:**
```json
{
  "mensaje": "Mascota registrada correctamente",
  "mascota": {
    "correo": "usuario@ejemplo.com",
    "nombre_mascota": "Pelusa",
    "tipo_servicio": "baño",
    "fecha": "2026-03-26"
  }
}
```

---

#### GET /mascotas/{correo}
Listar todas las mascotas de un usuario.

**Response:**
```json
{
  "correo": "usuario@ejemplo.com",
  "mascotas": [
    {
      "correo": "usuario@ejemplo.com",
      "nombre_mascota": "Pelusa",
      "tipo_servicio": "baño",
      "fecha": "2026-03-26"
    }
  ]
}
```

---

#### GET /reporte/{correo}
Obtener reporte de gastos y servicios de un usuario.

**Response:**
```json
{
  "correo": "usuario@ejemplo.com",
  "cantidad_servicios": 1,
  "servicios": ["baño"],
  "total_gastado": 60,
  "detalle": [
    {
      "mascota": "Pelusa",
      "servicio": "baño",
      "fecha": "2026-03-26",
      "precio": 60
    }
  ]
}
```

---

### 👋 Rutas Iniciales

#### GET /
Saludo de bienvenida.

**Response:**
```json
{
  "mensaje": "¡Hola! Bienvenido a mi API"
}
```

---

#### GET /bienvenido/{nombre}
Saludo personalizado.

**Response:**
```json
{
  "mensaje": "Hola Juan, ¡qué bueno verte por aquí!"
}
```

---

## 🧪 Flujo de Uso Típico

1. **Registrar usuario:**
   ```bash
   POST /register
   ```

2. **Iniciar sesión:**
   ```bash
   POST /login
   ```

3. **Ver servicios disponibles:**
   ```bash
   GET /servicios
   ```

4. **Registrar una mascota:**
   ```bash
   POST /registrar-mascota
   ```

5. **Listar mascotas del usuario:**
   ```bash
   GET /mascotas/{correo}
   ```

6. **Ver reporte de gastos:**
   ```bash
   GET /reporte/{correo}
   ```

---

## 📦 Dependencias

- **fastapi**: Framework web rápido para construir APIs
- **uvicorn**: Servidor ASGI para ejecutar FastAPI
- **pydantic**: Validación de datos y configuración

Instalación:
```bash
pip install fastapi uvicorn pydantic
```

---

## 🔧 Tecnologías Usadas

- **Python 3.x**
- **FastAPI**
- **Pydantic** (Validación de datos)
- **APIRouter** (Arquitectura modular)

---

## 📝 Notas

- Los datos se almacenan en memoria (listas). Para producción, usar una base de datos real.
- Las contraseñas se guardan sin encriptar. En producción, usar hash de contraseña (bcrypt).
- La API permite múltiples usuarios sin validación básica de permisos.

---

## 👨‍💻 Autor

Valeria Milena

---

## 📄 Licencia

Este proyecto está bajo la licencia MIT.

---

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o pull request.

---

**¡Gracias por usar Pétalos Pet Grooming API! 🐾**
