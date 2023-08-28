from fastapi import APIRouter, HTTPException
from .schemas import Produto

router = APIRouter()

@router.post("/produtos")
async def create_produto(produto: Produto):
    # TODO: Implementar a criação de produtos
    raise HTTPException(status_code=404, detail="Not implemented")

@router.get("/produtos")
async def get_produtos():
    # TODO: Implementar a listagem de produtos
    raise HTTPException(status_code=404, detail="Not implemented")

@router.get("/produtos/{id}")
async def get_produto_by_id(id: int):
    # TODO: Implementar a busca de produtos por ID
    raise HTTPException(status_code=404, detail="Not implemented")

@router.put("/produtos/{id}")
async def update_produto(id: int, produto: Produto):
    # TODO: Implementar a atualização de produtos
    raise HTTPException(status_code=404, detail="Not implemented")