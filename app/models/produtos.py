from db.base import Base

class Produto(Base):
    """
    Modelo para a entidade produto.
    """

    nome = sa.Column(sa.String(255), nullable=False)
    valor = sa.Column(sa.Float, nullable=False)
    descricao = sa.Column(sa.String(255), nullable=False)
