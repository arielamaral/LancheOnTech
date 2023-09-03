from fastapi import APIRouter, HTTPException
from .schemas import Pedido

router = APIRouter()

@router.post("/pedidos")
async def create_pedido(pedido: Pedido):
    # TODO: Implementar a criação de pedidos
    raise HTTPException(status_code=404, detail="Not implemented")

@router.get("/pedidos")
async def get_pedidos():
    # TODO: Implementar a listagem de pedidos
    raise HTTPException(status_code=404, detail="Not implemented")

@router.get("/pedidos/{id}")
async def get_pedido_by_id(id: int):
    # TODO: Implementar a busca de pedidos por ID
    raise HTTPException(status_code=404, detail="Not implemented")

@router.put("/pedidos/{id}")
async def update_pedido(id: int, pedido: Pedido):
    # TODO: Implementar a atualização de pedidos
    raise HTTPException(status_code=404, detail="Not implemented")

@router.delete("/pedidos/{id}")
async def delete_pedido(id: int):
    # TODO: Implementar a exclusão de pedidos
    raise HTTPException(status_code=404, detail="Not implemented")
