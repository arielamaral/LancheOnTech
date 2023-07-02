from app import db
from app.models.pedido import Pedido
from app.models.item_pedido import Item_Pedido
from app.models.produto import Produto

def cadastra_pedido(data):
    itens = data['itens']
    pedido = Pedido(valor_total=0.0)

    for item in itens:
        produto_id = item['produto_id']
        quantidade = item['quantidade']

        produto = Produto.query.get(produto_id)
        if not produto:
            raise Exception(f'Produto com id {produto_id} não encontrado')

        valor_item = produto.preco * quantidade

        item_pedido = Item_Pedido(produto_id=produto_id, quantidade=quantidade)
        pedido.itens.append(item_pedido)

        pedido.valor_total += valor_item

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
