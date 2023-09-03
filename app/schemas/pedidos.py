from pydantic import BaseModel

class Pedido(BaseModel):
    """
    Schema para o modelo pedido.
    """

    id: int
    data: str
    valor_total: float
    cliente_id: int
    produtos: list

