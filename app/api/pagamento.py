from flask import Blueprint, jsonify, request
from app.services.pagamento_service import processar_pagamento
from app.models.pedido import Pedido

pagamento_bp = Blueprint("pagamento", __name__, url_prefix="/pagamento")

@pagamento_bp.route("/", methods=["POST"])
def realizar_pagamento():
    pedido_id = request.json.get("pedido_id")
    metodo_pagamento = request.json.get("metodo_pagamento")
    dados_pagamento = request.json.get("dados_pagamento")

    pedido = Pedido.query.get(pedido_id)
    if not pedido:
        return jsonify({"message": "Pedido inválido ou não disponível para pagamento"}), 400

    pagamento = processar_pagamento(pedido_id, metodo_pagamento, dados_pagamento)

    if pagamento.status_pagamento == "Confirmado":
        return jsonify({"message": "Pagamento realizado com sucesso"}), 200
    else:
        return jsonify({"message": "Falha ao processar o pagamento"}), 400
