from flask import Blueprint, jsonify, request
from app.services.item_pedido_service import cadastra_item_pedido, atualiza_item_pedido, exclui_item_pedido

item_pedido_bp = Blueprint("item_pedido", __name__, url_prefix="/item_pedido")

@item_pedido_bp.route("/", methods=["POST"])
def cadastra_item():
    data = request.get_json()
    item_pedido = cadastra_item_pedido(data)
    return jsonify(item_pedido.to_dict()), 201

@item_pedido_bp.route("/<int:item_pedido_id>", methods=["PUT"])
def atualiza_item(item_pedido_id):
    data = request.get_json()
    item_pedido = atualiza_item_pedido(item_pedido_id, data)
    return jsonify(item_pedido.to_dict())

@item_pedido_bp.route("/<int:item_pedido_id>", methods=["DELETE"])
def exclui_item(item_pedido_id):
    message = exclui_item_pedido(item_pedido_id)
    return jsonify({"message": message}), 204
