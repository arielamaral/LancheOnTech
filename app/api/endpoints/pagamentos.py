from fastapi import APIRouter, HTTPException
from app.models import Pagamento
from app.crud import pagamentos

router = APIRouter()

@router.post("/pagamentos")
async def create_pagamento(pagamento: Pagamento):
    pedido = await pagamentos.get_pedido_by_id(pagamento.pedido_id)
    if pedido is None:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    pagamento.valor_pago = pagamento.valor_total
    pagamento.status = "PAGO"
    pagamento_criado = await pagamentos.create_pagamento(pagamento)
    return pagamento_criado

@router.get("/pagamentos")
async def get_pagamentos():
    pagamentos_list = await pagamentos.get_all_pagamentos()
    return pagamentos_list

@router.put("/pagamentos/{id}")
async def update_pagamento(id: int, pagamento: Pagamento):
    existing_pagamento = await pagamentos.get_pagamento_by_id(id)
    if existing_pagamento is None:
        raise HTTPException(status_code=404, detail="Pagamento não encontrado")
    updated_pagamento = await pagamentos.update_pagamento(id, pagamento)
    return updated_pagamento

@router.delete("/pagamentos/{id}")
async def delete_pagamento(id: int):
    existing_pagamento = await pagamentos.get_pagamento_by_id(id)
    if existing_pagamento is None:
        raise HTTPException(status_code=404, detail="Pagamento não encontrado")
    await pagamentos.delete_pagamento(id)
    return Response(status_code=204)