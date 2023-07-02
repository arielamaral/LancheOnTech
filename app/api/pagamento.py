from flask import Blueprint, jsonify, request
from app.services.pagamento_service import processar_pagamento
from app.models.pedido import Pedido
from app import db

pagamento_bp = Blueprint("pagamento", __name__, url_prefix="/pagamento")

@pagamento_bp.route("/", methods=["POST"])
def realizar_pagamento():
    data = request.json
    pedido_id = data.get("pedido_id")
    metodo_pagamento = data.get("metodo_pagamento")
    dados_pagamento = data.get("dados_pagamento")

    pedido = Pedido.query.get(pedido_id)
    if not pedido:
        return jsonify({"message": "Pedido inválido ou não disponível para pagamento"}), 400

    pagamento = processar_pagamento(pedido_id, metodo_pagamento, dados_pagamento)

    if pagamento.status_pagamento == "Confirmado":
        pedido.confirmar_pagamento()
        db.session.commit()
        return jsonify({"message": "Pagamento realizado com sucesso"})
    else:
        return jsonify({"message": "Falha ao processar o pagamento"}), 400
