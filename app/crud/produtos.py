from fastapi import APIRouter, HTTPException
from app.schemas import Produto
from core.config import Config
from core.database import Session

router = APIRouter()

@router.post("/produtos")
async def create_produto(produto: Produto):
    """
    Cria um novo produto.

    Args:
        produto: O produto a ser criado.

    Returns:
        O produto criado.
    """
    session = Session(Config.SQLALCHEMY_DATABASE_URI)
    produto_criado = session.add(produto)
    session.commit()
    session.close()
    return produto_criado

@router.get("/produtos")
async def get_produtos():
    """
    Listagem de produtos.

    Returns:
        Uma lista com todos os produtos.
    """
    session = Session(Config.SQLALCHEMY_DATABASE_URI)
    produtos = session.query(Produto).all()
    session.close()
    return produtos

@router.get("/produtos/{id}")
async def get_produto_by_id(id: int):
    """
    Busca um produto por ID.

    Args:
        id: O ID do produto a ser buscado.

    Returns:
        O produto encontrado.
    """
    session = Session(Config.SQLALCHEMY_DATABASE_URI)
    produto = session.query(Produto).get(id)
    session.close()
    if produto is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto

@router.put("/produtos/{id}")
async def update_produto(id: int, produto: Produto):
    """
    Atualizar um produto.

    Args:
        id: O ID do produto a ser atualizado.
        produto: O produto com as alterações.

    Returns:
        O produto atualizado.
    """
    session = Session(Config.SQLALCHEMY_DATABASE_URI)
    produto_atual = session.query(Produto).get(id)
    if produto_atual is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    produto_atual.id = id
    produto_atual.nome = produto.nome
    produto_atual.valor = produto.valor
    session.commit()
    session.close()
    return produto_atual

@router.delete("/produtos/{id}")
async def delete_produto(id: int):
    """
    Exclui um produto.

    Args:
        id: O ID do produto a ser excluído.

    Returns:
        Um objeto vazio.
    """
    session = Session(Config.SQLALCHEMY_DATABASE_URI)
    produto = session.query(Produto).get(id)
    if produto is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    session.delete(produto)
    session.commit()
    session.close()
    return {}