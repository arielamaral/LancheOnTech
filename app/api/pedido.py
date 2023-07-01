from flask import Blueprint, jsonify, request

from app.services.pedido_service import (
    cadastra_pedido,
    obtem_pedido,
    lista_pedidos,
    atualiza_pedido,
    exclui_pedido
)

pedido_bp = Blueprint("pedido_bp", __name__, url_prefix="/pedido")

@pedido_bp.route("/", methods=["GET"])
def get_pedidos():
    pedidos = lista_pedidos()
    return jsonify([pedido.to_dict() for pedido in pedidos])

@pedido_bp.route("/<int:id>", methods=["GET"])
def get_pedido(id):
    pedido = obtem_pedido(id)
    if pedido:
        return jsonify(pedido.to_dict())
    else:
        return jsonify({"message": "Pedido não encontrado"}), 404

@pedido_bp.route("/", methods=["POST"])
def post_pedido():
    data = request.get_json()
    pedido = cadastra_pedido(data)
    return jsonify(pedido.to_dict()), 201

@pedido_bp.route("/<int:id>", methods=["PUT"])
def put_pedido(id):
    data = request.get_json()
    pedido = atualiza_pedido(id, data)
    if pedido:
        return jsonify(pedido.to_dict())
    else:
        return jsonify({"message": "Pedido não encontrado"}), 404

@pedido_bp.route("/<int:id>", methods=["DELETE"])
def delete_pedido(id):
    sucesso = exclui_pedido(id)
    if sucesso:
        return jsonify({"message": "Pedido removido com sucesso"})
    else:
        return jsonify({"message": "Pedido não encontrado"}), 404
