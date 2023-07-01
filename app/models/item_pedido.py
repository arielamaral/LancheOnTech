from app import db

class Item_Pedido(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pedido_id = db.Column(db.Integer, db.ForeignKey('pedido.id'), nullable=False)
    produto_id = db.Column(db.Integer, db.ForeignKey('produto.id'), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)

#    def __repr__(self):
#        return f"<Item_Pedido {self.id}>"

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}