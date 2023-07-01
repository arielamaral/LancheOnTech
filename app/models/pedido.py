from app import db

class Pedido(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    valor_total = db.Column(db.Float, nullable=False)

    itens = db.relationship('Item_Pedido', backref='pedido', lazy=True)

    def __repr__(self):
        return f"<Pedido {self.id}>"

    def to_dict(self):
        data = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        data['itens'] = [item.to_dict() for item in self.itens]
        return data

