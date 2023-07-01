from app import db

class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(200), nullable=False)
    preco = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<Produto {self.nome}>"

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

