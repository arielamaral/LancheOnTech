from fastapi import APIRouter, HTTPException
from app.models.clientes import Cliente

router = APIRouter()

@router.post("/clientes")
async def create_cliente(cliente: Cliente):
    # TODO: Implementar a criação de clientes
    raise HTTPException(status_code=404, detail="Not implemented")

@router.get("/clientes")
async def get_clientes():
    # TODO: Implementar a listagem de clientes
    raise HTTPException(status_code=404, detail="Not implemented")

@router.get("/clientes/{id}")
async def get_cliente_by_id(id: int):
    # TODO: Implementar a busca de clientes por ID
    raise HTTPException(status_code=404, detail="Not implemented")

@router.put("/clientes/{id}")
async def update_cliente(id: int, cliente: Cliente):
    # TODO: Implementar a atualização de clientes
    raise HTTPException(status_code=404, detail="Not implemented")

@router.delete("/clientes/{id}")
async def delete_cliente(id: int):
    # TODO: Implementar a exclusão de clientes
    raise HTTPException(status_code=404, detail="Not implemented")