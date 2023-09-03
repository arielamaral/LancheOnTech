from typing import Optional
from pydantic import BaseModel

class PagamentoRequest(BaseModel):
    """
    Esquema de solicitação de pagamento.
    """

    valor_pago: Decimal
    status: str

class PagamentoResponse(BaseModel):
    """
    Esquema de resposta de pagamento.
    """

    id: int
    pedido_id: int
    valor_pago: Decimal
    status: str
    criado_em: datetime
    atualizado_em: datetime


class PagamentoListResponse(BaseModel):
    """
    Esquema de resposta de listagem de pagamentos.
    """

    pagamentos: list[PagamentoResponse]