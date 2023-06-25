from app import db
from app.models.pedido import Pedido

def cadastra_pedido(data):
    itens = data['itens']
    pedido = Pedido(valor_total=0.0)
    for item in itens:
        produto_id = item['produto_id']
        quantidade = item['quantidade']
        # Lógica para buscar o produto pelo ID e calcular o valor total do pedido
        # Adicionar o item ao pedido

    db.session.add(pedido)
    db.session.commit()
    return pedido


def atualiza_pedido(pedido_id, data):
    pedido = Pedido.query.get(pedido_id)

    if not pedido:
        return None

    db.session.commit()

    return pedido


def exclui_pedido(pedido_id):
    pedido = Pedido.query.get(pedido_id)

    if not pedido:
        return False

    db.session.delete(pedido)
    db.session.commit()

    return True

def obtem_pedido(pedido_id):
    pedido = Pedido.query.get(pedido_id)
    if pedido:
        return pedido
    else:
        return None

def lista_pedidos():
    pedidos = Pedido.query.all()
    return pedidos
