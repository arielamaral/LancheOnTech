import unittest
from flask import current_app
from app import create_app, db
from app.models.cliente import Cliente

class ClienteTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_cadastra_cliente(self):
        cliente_data = {
            'nome': 'Ariel Amaral',
            'cpf': '12345678900',
            'email': 'ariel@localhost'
        }

        response = self.client.post('/cliente/', json=cliente_data)
        self.assertEqual(response.status_code, 201)

        cliente = Cliente.query.filter_by(cpf='12345678900').first()
        self.assertIsNotNone(cliente)
        self.assertEqual(cliente.nome, 'Ariel Amaral')
        self.assertEqual(cliente.email, 'ariel@localhost')
