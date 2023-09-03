import os

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