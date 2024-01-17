from fastapi import APIRouter, HTTPException
from app.models.clientes import Cliente

router = APIRouter()

@router.post("/clientes")
async def create_cliente(cliente: Cliente):
    """
    Cria um novo cliente.
    """
    # TODO: Implementar a criação de clientes
    raise HTTPException(status_code=400, detail="Not implemented")

@router.get("/clientes")
async def get_clientes():
    """
    Retorna uma lista de todos os clientes.
    """
    # TODO: Implementar a listagem de clientes
    raise HTTPException(status_code=400, detail="Not implemented")

@router.get("/clientes/{id}")
async def get_cliente_by_id(id: int):
    """
    Retorna um cliente pelo ID.
    """
    # TODO: Implementar a busca de clientes por ID
    raise HTTPException(status_code=404, detail="Not implemented")

@router.put("/clientes/{id}")
async def update_cliente(id: int, cliente: Cliente):
    """
    Atualiza um cliente pelo ID.
    """
    # TODO: Implementar a atualização de clientes
    raise HTTPException(status_code=400, detail="Not implemented")

@router.delete("/clientes/{id}")
async def delete_cliente(id: int):
    """
    Exclui um cliente pelo ID.
    """
    # TODO: Implementar a exclusão de clientes
    raise HTTPException(status_code=404, detail="Not implemented")