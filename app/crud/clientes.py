from fastapi import APIRouter, HTTPException
from app.schemas import Cliente
from core.config import Config
from core.database import Session

router = APIRouter()

@router.post("/clientes")
async def create_cliente(cliente: Cliente):
    """
    Cria um novo cliente.

    Args:
        cliente: O cliente a ser criado.

    Returns:
        O cliente criado.
    """
    session = Session(Config.SQLALCHEMY_DATABASE_URI)
    cliente_criado = session.add(cliente)
    session.commit()
    session.close()