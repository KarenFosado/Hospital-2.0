from fastapi import FastAPI
from routes.users import user
from routes.person import person

app = FastAPI()  # variable app
app.include_router(person)  # Luego agrega las rutas
app.include_router(user)

print("Bienvenido al servidor uvicorn")
