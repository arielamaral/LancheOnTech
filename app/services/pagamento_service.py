import json
from app import db
from app.models.pagamento import Pagamento

def processar_pagamento(pedido_id, metodo_pagamento, dados_pagamento):

    dados_pagamento_str = json.dumps(dados_pagamento)

    pagamento = Pagamento(pedido_id=pedido_id, metodo_pagamento=metodo_pagamento, dados_pagamento=dados_pagamento_str, status_pagamento='Confirmado')

    db.session.add(pagamento)
    db.session.commit()

    return pagamento
