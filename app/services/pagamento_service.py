from app import db
from app.models.pagamento import Pagamento


def processar_pagamento(pedido_id, metodo_pagamento, dados_pagamento):
    pagamento = Pagamento(pedido_id=pedido_id, metodo_pagamento=metodo_pagamento, dados_pagamento=dados_pagamento)

    # Lógica para processar o pagamento
    # Aqui você pode adicionar a lógica específica para o seu processo de pagamento,
    # como integração com API de pagamento, verificação de dados, entre outros.
    # Nesse exemplo, faremos apenas uma simulação de processamento de pagamento com sucesso.

    if metodo_pagamento == 'cartao_credito':
        if dados_pagamento.get('numero_cartao') and dados_pagamento.get('validade') and dados_pagamento.get('cvv'):
            pagamento.status = 'Confirmado'
        else:
            pagamento.status = 'Falha na verificação'
    elif metodo_pagamento == 'boleto':
        if dados_pagamento.get('nome_pagador') and dados_pagamento.get('cpf_pagador'):
            pagamento.status = 'Confirmado'
        else:
            pagamento.status = 'Falha na geração do boleto'
    else:
        pagamento.status = 'Método de pagamento inválido'

    db.session.add(pagamento)
    db.session.commit()

    return pagamento
