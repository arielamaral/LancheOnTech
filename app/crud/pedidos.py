from fastapi import APIRouter, HTTPException
from app.schemas import Pedido
from core.config import Config
from core.database import Session

router = APIRouter()


@router.post("/pedidos")
async def create_pedido(pedido: Pedido):
    """
    Cria um novo pedido.

    Args:
        pedido: O pedido a ser criado.

    Returns:
        O pedido criado.
    """
    session = Session(Config.SQLALCHEMY_DATABASE_URI)
    pedido_criado = session.add(pedido)
    session.commit()
    session.close()
    return pedido_criado

@router.get("/pedidos")
async def get_pedidos():
    """
    Listagem de pedidos.

    Returns:
        Uma lista com todos os pedidos.
    """
    session = Session(Config.SQLALCHEMY_DATABASE_URI)
    pedidos = session.query(Pedido).all()
    session.close()
    return pedidos

@router.get("/pedidos/{id}")
async def get_pedido_by_id(id: int):
    """
    Busca um pedido por ID.

    Args:
        id: O ID do pedido a ser buscado.

    Returns:
        O pedido encontrado.
    """
    session = Session(Config.SQLALCHEMY_DATABASE_URI)
    pedido = session.query(Pedido).get(id)
    session.close()
    if pedido is None:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    return pedido

@router.put("/pedidos/{id}")
async def update_pedido(id: int, pedido: Pedido):
    """
    Atualizar um pedido.

    Args:
        id: O ID do pedido a ser atualizado.
        pedido: O pedido com as alterações.

    Returns:
        O pedido atualizado.
    """
    session = Session(Config.SQLALCHEMY_DATABASE_URI)
    pedido_atual = session.query(Pedido).get(id)
    if pedido_atual is None:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    pedido_atual.id = id
    pedido_atual.data = pedido.data
    pedido_atual.valor_total = pedido.valor_total
    pedido_atual.cliente = pedido.cliente
    pedido_atual.produtos = pedido.produtos
    session.commit()
    session.close()
    return pedido_atual

@router.delete("/pedidos/{id}")
async def delete_pedido(id: int):
    """
    Exclui um pedido.

    Args:
        id: O ID do pedido a ser excluído.

    Returns:
        Um objeto vazio.
    """
    session = Session(Config.SQLALCHEMY_DATABASE_URI)
    pedido = session.query(Pedido).get(id)
    if pedido is None:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    session.delete(pedido)
    session.commit()
    session.close()
    return {}