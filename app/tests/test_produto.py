import unittest
from flask import current_app
from app import create_app, db
from app.models.produto import Produto

class ProdutoTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_cadastra_produto(self):
        produto_data = {
            'nome': 'Sobremesa',
            'descricao': 'Pudim',
            'preco': 10.0
        }

        response = self.client.post('/produto/', json=produto_data)
        self.assertEqual(response.status_code, 201)

        produto = Produto.query.filter_by(nome='Sobremesa').first()
        self.assertIsNotNone(produto)
        self.assertEqual(produto.descricao, 'Pudim')
        self.assertEqual(produto.preco, 10.0)
