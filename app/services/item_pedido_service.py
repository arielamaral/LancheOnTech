from app import db
from app.models.itempedido import ItemPedido

def cadastra_item_pedido(data):
    pedido_id = data['pedido_id']
    produto_id = data['produto_id']
    quantidade = data['quantidade']

    item_pedido = ItemPedido(pedido_id=pedido_id, produto_id=produto_id, quantidade=quantidade)

    db.session.add(item_pedido)
    db.session.commit()
    return item_pedido

def atualiza_item_pedido(item_pedido, data):
    produto_id = data['produto_id']
    quantidade = data['quantidade']

    item_pedido.produto_id = produto_id
    item_pedido.quantidade = quantidade

    db.session.commit()
    return item_pedido

def exclui_item_pedido(item_pedido):
    db.session.delete(item_pedido)
    db.session.commit()
