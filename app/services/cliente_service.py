from app import db
from app.models.cliente import Cliente

def cadastra_cliente(data):
    cpf = data['cpf']
    nome = data['nome']
    email = data['email']

    cliente = Cliente(cpf=cpf, nome=nome, email=email)

    db.session.add(cliente)
    db.session.commit()

    return cliente


def atualiza_cliente(cliente_id, data):
    cliente = Cliente.query.get(cliente_id)

    if not cliente:
        return None

    cliente.cpf = data.get('cpf', cliente.cpf)
    cliente.nome = data.get('nome', cliente.nome)
    cliente.email = data.get('email', cliente.email)

    db.session.commit()

    return cliente


def exclui_cliente(cliente_id):
    cliente = Cliente.query.get(cliente_id)

    if not cliente:
        return False

    db.session.delete(cliente)
    db.session.commit()

    return True
