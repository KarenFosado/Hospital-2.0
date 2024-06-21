from fastapi import FastAPI
from routes.person import person
from routes.persona import persona

app = FastAPI()

# Incluyendo los routers
app.include_router(person)
app.include_router(persona)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")
