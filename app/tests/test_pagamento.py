import unittest
from app import create_app, db
from app.models.pagamento import Pagamento

class PagamentoTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()


        self.pagamento = Pagamento(valor=100.0, status="Pendente")

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_cria_pagamento(self):
        db.session.add(self.pagamento)
        db.session.commit()


        pagamento_salvo = Pagamento.query.first()
        self.assertIsNotNone(pagamento_salvo)
        self.assertEqual(pagamento_salvo.valor, 100.0)
        self.assertEqual(pagamento_salvo.status, "Pendente")

    def test_atualiza_status_pagamento(self):
        db.session.add(self.pagamento)
        db.session.commit()


        self.pagamento.status = "Confirmado"
        db.session.commit()


        pagamento_atualizado = Pagamento.query.first()
        self.assertEqual(pagamento_atualizado.status, "Confirmado")

    def test_deleta_pagamento(self):
        db.session.add(self.pagamento)
        db.session.commit()


        db.session.delete(self.pagamento)
        db.session.commit()


        pagamento_deletado = Pagamento.query.first()
        self.assertIsNone(pagamento_deletado)

if __name__ == '__main__':
    unittest.main()
