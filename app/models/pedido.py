from app import db

class Pedido(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    valor_total = db.Column(db.Float, nullable=False)

    itens = db.relationship('Item_Pedido', backref='pedido', lazy=True)

    def __repr__(self):
        return f"<Pedido {self.id}>"
