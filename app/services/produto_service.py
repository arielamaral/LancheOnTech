from app import db
from app.models.produto import Produto

def cadastra_produto(data):
    nome = data['nome']
    preco = data['preco']
    quantidade = data['quantidade']

    produto = Produto(nome=nome, preco=preco, quantidade=quantidade)

    db.session.add(produto)
    db.session.commit()

    return produto

def obtem_produto(produto_id):
    produto = Produto.query.get(produto_id)
    return produto

def lista_produtos():
    produtos = Produto.query.all()
    return produtos

def atualiza_produto(produto_id, data):
    produto = Produto.query.get(produto_id)

    if not produto:
        return None

    produto.nome = data.get('nome', produto.nome)
    produto.preco = data.get('preco', produto.preco)
    produto.quantidade = data.get('quantidade', produto.quantidade)

    db.session.commit()

    return produto

def exclui_produto(produto_id):
    produto = Produto.query.get(produto_id)

    if not produto:
        return False

    db.session.delete(produto)
    db.session.commit()

    return True
