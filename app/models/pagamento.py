from app import db

class Pagamento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pedido_id = db.Column(db.Integer, db.ForeignKey('pedido.id'), nullable=False)
    metodo_pagamento = db.Column(db.String(50), nullable=False)
    dados_pagamento = db.Column(db.Text, nullable=False)
    status_pagamento = db.Column(db.String(20), nullable=False)

    def __init__(self, pedido_id, metodo_pagamento, dados_pagamento):
        self.pedido_id = pedido_id
        self.metodo_pagamento = metodo_pagamento
        self.dados_pagamento = dados_pagamento
        self.status_pagamento = 'Confirmado'
