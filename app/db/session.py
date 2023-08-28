import sqlalchemy as sa

class Session(sa.orm.Session):
    """
    Classe para gerenciar a sessão com o banco de dados.
    """

    def __init__(self, url):
        super(Session, self).__init__(sa.create_engine(url))