from flask import Blueprint, jsonify, request

from app.services.cliente_service import (
    cadastra_cliente,
    obtem_cliente,
    lista_clientes,
    atualiza_cliente,
    exclui_cliente
)

cliente_bp = Blueprint("cliente_bp", __name__, url_prefix="/cliente")

@cliente_bp.route("/", methods=["GET"])
def get_clientes():
    clientes = lista_clientes()
    return jsonify(clientes)

@cliente_bp.route("/<int:id>", methods=["GET"])
def get_cliente(id):
    cliente = obtem_cliente(id)
    if cliente:
        return jsonify(cliente)
    else:
        return jsonify({"message": "Cliente não encontrado"}), 404

@cliente_bp.route("/", methods=["POST"])
def post_cliente():
    data = request.get_json()
    cliente = cadastra_cliente(data)
    return jsonify(cliente.to_dict()), 201

@cliente_bp.route("/<int:id>", methods=["PUT"])
def put_cliente(id):
    data = request.get_json()
    cliente = atualiza_cliente(id, data)
    if cliente:
        return jsonify(cliente)
    else:
        return jsonify({"message": "Cliente não encontrado"}), 404

@cliente_bp.route("/<int:id>", methods=["DELETE"])
def delete_cliente(id):
    sucesso = exclui_cliente(id)
    if sucesso:
        return jsonify({"message": "Cliente removido com sucesso"})
    else:
        return jsonify({"message": "Cliente não encontrado"}), 404
