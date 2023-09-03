from typing import Optional

from pydantic import BaseModel


class ProdutoRequest(BaseModel):
    """
    Solicitação de criação ou atualização de produto.

    Atributos:
        nome: O nome do produto.
        valor: O valor do produto.
        descricao: A descrição do produto.
    """

    nome: str
    valor: float
    descricao: Optional[str] = None


class ProdutoResponse(BaseModel):
    """
    Dados de um produto.

    Atributos:
        id: O ID do produto.
        nome: O nome do produto.
        valor: O valor do produto.
        descricao: A descrição do produto.
    """

    id: int
    nome: str
    valor: float
    descricao: Optional[str] = None