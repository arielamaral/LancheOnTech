from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Cliente(Base):
    """
    Modelo para a entidade cliente.
    """

    __tablename__ = 'clientes'

    nome = Column(String(255), nullable=False)
    cpf = Column(String(11), nullable=False)
    email = Column(String(255), nullable=False)