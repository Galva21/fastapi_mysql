from fastapi import FastAPI
from routes.user import user

app = FastAPI(
    title= "PROYECTO DE GRADO API",
    description="Estudiante Alvaro Ruben Gonzales Vilte",
    version="1.0",
    openapi_tags=[
        {"name": "Users",
         "description": "Rutas de usuarios"}
    ]
)

app.include_router(user)