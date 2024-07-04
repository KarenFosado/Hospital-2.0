from fastapi import FastAPI
from routes.persona import persona
from routes.user import user
app = FastAPI()  # variable app
app.include_router(persona)  # Luego agrega las rutas
app.include_router(user)

print("Bienvenido al servidor uvicorn")
