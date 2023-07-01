from flask import Blueprint, jsonify

from app.services.pagamento_service import processar_pagamento
from app.models.pedido import Pedido

pagamento_bp = Blueprint("pagamento", __name__, url_prefix="/pagamento")


@pagamento_bp.route("/", methods=["POST"])
def realizar_pagamento():
    pedido_id = request.json.get("pedido_id")
    metodo_pagamento = request.json.get("metodo_pagamento")
    dados_pagamento = request.json.get("dados_pagamento")

    pedido = Pedido.query.get(pedido_id)
    if not pedido or not pedido.pode_pagar():
        return jsonify({"message": "Pedido inválido ou não disponível para pagamento"}), 400

    if not pedido.tem_item_pedido():
        return jsonify({"message": "Pedido não contém itens para pagamento"}), 400

    status_pagamento = processar_pagamento(pedido_id, metodo_pagamento, dados_pagamento)

    if status_pagamento == "sucesso":
        pedido.confirmar_pagamento()
        db.session.commit()
        return jsonify({"message": "Pagamento realizado com sucesso"})
    else:
        return jsonify({"message": "Falha ao processar o pagamento"}), 400
