import sqlalchemy as sa

class Base(sa.Model):
    """
    Classe base para todos os modelos do banco de dados.
    """

    __abstract__ = True

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)

def to_dict(self):
    """
    Converte o modelo em um dicionário.

    Returns:
        Um dicionário com os atributos do modelo.
    """
    data = {}
    for column in self.__table__.columns:
        data[column.name] = getattr(self, column.name)
    return data