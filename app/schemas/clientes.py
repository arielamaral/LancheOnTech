from pydantic import BaseModel

class Cliente(BaseModel):
    """
    Schema para o modelo cliente.
    """

    id: int
    nome: str
    cpf: str
    email: str