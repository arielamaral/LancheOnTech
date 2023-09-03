from fastapi import APIRouter, HTTPException
from app.models import Pagamento
from app.crud import pagamentos

router = APIRouter()

@router.post("/pagamentos")
async def create_pagamento(pagamento: Pagamento):
    """
    Cria um novo pagamento.

    Args:
        pagamento: O pagamento a ser criado.

    Returns:
        O pagamento criado.
    """
    pedido = await pagamentos.get_pedido_by_id(pagamento.pedido_id)
    if pedido is None:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    pagamento.valor_pago = pagamento.valor_total
    pagamento.status = "PAGO"
    pagamento_criado = pagamentos.create_pagamento(pagamento)
    return pagamento_criado


@router.get("/pagamentos")
async def get_pagamentos():
    """
    Listagem de pagamentos.

    Returns:
        Uma lista com todos os pagamentos.
    """
    return pagamentos.get_pagamentos()


@router.get("/pagamentos/{id}")
async def get_pagamento_by_id(id: int):
    """
    Busca um pagamento por ID.

    Args:
        id: O ID do pagamento a ser buscado.

    Returns:
        O pagamento encontrado.
    """
    return pagamentos.get_pagamento_by_id(id)


@router.put("/pagamentos/{id}")
async def update_pagamento(id: int, pagamento: Pagamento):
    """
    Atualizar um pagamento.

    Args:
        id: O ID do pagamento a ser atualizado.
        pagamento: O pagamento com as alterações.

    Returns:
        O pagamento atualizado.
    """
    pagamento_atualizado = pagamentos.update_pagamento(id, pagamento)
    return pagamento_atualizado


@router.delete("/pagamentos/{id}")
async def delete_pagamento(id: int):
    """
    Exclui um pagamento.

    Args:
        id: O ID do pagamento a ser excluído.

    Returns:
        Um objeto vazio.
    """
    pagamentos.delete_pagamento(id)
    return {}