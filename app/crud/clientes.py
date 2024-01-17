from fastapi import APIRouter, HTTPException
from app.schemas import Cliente
from app.models import Cliente as ClienteModel
from core.config import Config
from core.database import Session
from sqlalchemy.exc import SQLAlchemyError

router = APIRouter()

@router.post("/clientes")
async def create_cliente(cliente: Cliente):
    session = Session(Config.SQLALCHEMY_DATABASE_URI)
    cliente_model = ClienteModel(**cliente.dict())
    try:
        session.add(cliente_model)
        session.commit()
    except SQLAlchemyError:
        session.rollback()
        raise HTTPException(status_code=500, detail="Database error")
    finally:
        session.close()
    return {"id": cliente_model.id}