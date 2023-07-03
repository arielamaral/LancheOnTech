from app import db
from app.models.item_pedido import Item_Pedido
from app.models.pedido import Pedido


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

def exclui_item_pedido(item_pedido):
    item_pedido = Item_Pedido.query.get(item_pedido)

    if not item_pedido:
        return False

    db.session.delete(item_pedido)
    db.session.commit()

    return True