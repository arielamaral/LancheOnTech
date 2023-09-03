from db.base import Base

class Pedido(Base):
    """
    Modelo para a entidade pedido.
    """

    data = sa.Column(sa.DateTime, nullable=False)
    valor_total = sa.Column(sa.Float, nullable=False)
    cliente_id = sa.Column(sa.Integer, sa.ForeignKey("clientes.id"), nullable=False)
    produtos = sa.relationship("Produto", secondary="pedidos_produtos")