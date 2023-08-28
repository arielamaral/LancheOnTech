from pydantic import BaseModel

class Produto(BaseModel):
    """
    Schema para o modelo produto.
    """

    id: int
    nome: str
    valor: float
    descricao: float

