from flask import Blueprint, jsonify, request

from app.services.produto_service import (
    cadastra_produto,
    obtem_produto,
    lista_produtos,
    atualiza_produto,
    exclui_produto
)

produto_bp = Blueprint("produto_bp", __name__, url_prefix="/produto")

@produto_bp.route("/", methods=["GET"])
def get_produtos():
    produtos = lista_produtos()
    return jsonify(produtos)

@produto_bp.route("/<int:id>", methods=["GET"])
def get_produto(id):
    produto = obtem_produto(id)
    if produto:
        return jsonify(produto)
    else:
        return jsonify({"message": "Produto não encontrado"}), 404

@produto_bp.route("/", methods=["POST"])
def post_produto():
    data = request.get_json()
    produto = cadastra_produto(data)
    return jsonify(produto), 201

@produto_bp.route("/<int:id>", methods=["PUT"])
def put_produto(id):
    data = request.get_json()
    produto = atualiza_produto(id, data)
    if produto:
        return jsonify(produto)
    else:
        return jsonify({"message": "Produto não encontrado"}), 404

@produto_bp.route("/<int:id>", methods=["DELETE"])
def delete_produto(id):
    sucesso = exclui_produto(id)
    if sucesso:
        return jsonify({"message": "Produto removido com sucesso"})
    else:
        return jsonify({"message": "Produto não encontrado"}), 404
