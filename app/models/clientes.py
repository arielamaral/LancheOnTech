from db.base import Base

class Cliente(Base):
    """
    Modelo para a entidade cliente.
    """

    nome = sa.Column(sa.String(255), nullable=False)
    cpf = sa.Column(sa.String(11), nullable=False)
    email = sa.Column(sa.String(255), nullable=False)