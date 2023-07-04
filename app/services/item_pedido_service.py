from app import db
from app.models.item_pedido import Item_Pedido
from app.models.pedido import Pedido
from app.models.produto import Produto
from flask import jsonify


def cadastra_item_pedido(data):
    pedido_id = data['pedido_id']
    itens_data = data['itens']

    for item_data in itens_data:
        produto_id = item_data['produto_id']
        quantidade = item_data['quantidade']

        item_pedido = Item_Pedido(pedido_id=pedido_id, produto_id=produto_id, quantidade=quantidade)
        db.session.add(item_pedido)

    db.session.commit()

    pedido = Pedido.query.get(pedido_id)
    return pedido


def atualiza_item_pedido(item_pedido, data):
    produto_id = data['produto_id']
    quantidade = data['quantidade']

    item_pedido.produto_id = produto_id
    item_pedido.quantidade = quantidade

    db.session.commit()
    return item_pedido


def exclui_item_pedido(item_pedido_id):
    item_pedido = Item_Pedido.query.get(item_pedido_id)

    if item_pedido:
        produto = Produto.query.get(item_pedido.produto_id)

        if not produto:
            return 'Produto não encontrado'

        valor_total_item = produto.preco * item_pedido.quantidade

        pedido = Pedido.query.get(item_pedido.pedido_id)
        if pedido:
            pedido.valor_total -= valor_total_item
            if pedido.valor_total < 0:
                pedido.valor_total = 0

        db.session.delete(item_pedido)
        db.session.commit()

        return 'Item do Pedido, removido com sucesso!'
    else:
        return 'ItemPedido não encontrado'
