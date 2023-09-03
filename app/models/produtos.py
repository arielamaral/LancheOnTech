from db.base import Base

class Produto(Base):
    """
    Modelo para a entidade produto.

    Atributos:
        id: O ID do produto no banco de dados.
        nome: O nome do produto.
        valor: O valor do produto.
        descricao: A descrição do produto.
    """

    __tablename__ = "produtos"

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    nome = sa.Column(sa.String(255), nullable=False)
    valor = sa.Column(sa.Decimal(10, 2), nullable=False)
    descricao = sa.Column(sa.String(255), nullable=False)