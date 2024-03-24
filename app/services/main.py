import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.endpoints import pagamentos

ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS", "*").split(",")
ALLOWED_METHODS = os.getenv("ALLOWED_METHODS", "GET,POST,PUT,DELETE").split(",")
ALLOWED_HEADERS = os.getenv("ALLOWED_HEADERS", "*").split(",")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_methods=ALLOWED_METHODS,
    allow_headers=ALLOWED_HEADERS,
)

# Incluir roteadores
app.include_router(pagamentos.router)

if __name__ == "__main__":
    # Verificar se estamos em um ambiente de desenvolvimento
    if os.getenv("ENV", "development") == "development":
        app.run(debug=True)
    else:
        app.run(debug=False)import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routers import pagamentos


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

app.include_router(pagamentos.router)


if __name__ == "__main__":
    app.run(debug=True)