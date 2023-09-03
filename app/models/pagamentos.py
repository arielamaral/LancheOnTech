from sqlalchemy import Column, Integer, String, DECIMAL, Date, Enum

class Pagamento(Base):
    """
    Modelo de pagamento.
    """

    id = Column(Integer, primary_key=True, autoincrement=True)
    pedido_id = Column(Integer, nullable=False)
    valor_pago = Column(DECIMAL(10, 2), nullable=False)
    status = Column(Enum("PAGO", "PENDENTE"), nullable=False)
    criado_em = Column(Date, default=func.now())
    atualizado_em = Column(Date, onupdate=func.now())

    def __repr__(self):
        return f"<Pagamento {self.id}>"