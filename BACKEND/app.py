from fastapi import FastAPI
from routes.user import user
from routes.person import person
from routes.rol import rol
from routes.userrol import userrol
from routes.tbc_organos import tbc_organos  # Importar el enrutador de organos
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()  # variable app

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
app.include_router(person)  # Luego agrega las rutas
app.include_router(user)
app.include_router(rol)
app.include_router(userrol)
app.include_router(tbc_organos)  # Agregar el enrutador de organos



app

print("Bienvenido al servidor uvicorn")
