import unittest
from flask import current_app
from app import create_app, db
from app.models.pedido import Pedido

class PedidoTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_cadastra_pedido(self):
        pedido_data = {
            'itens': [
                {'produto_id': 1, 'quantidade': 2},
                {'produto_id': 2, 'quantidade': 1}
            ]
        }

        response = self.client.post('/pedido/', json=pedido_data)
        self.assertEqual(response.status_code, 201)

        pedido = Pedido.query.first()
        self.assertIsNotNone(pedido)
        self.assertEqual(len(pedido.itens), 2)