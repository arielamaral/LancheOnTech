from sqlalchemy.orm import Session
from app.models import Pagamento

class PagamentosRepository:
    """
    Repository para o modelo de pagamento.
    """

    def __init__(self, session: Session):
        self.session = session

    async def create_pagamento(self, pagamento: Pagamento):
        """
        Cria um novo pagamento.

        Args:
            pagamento: O pagamento a ser criado.

        Returns:
            O pagamento criado.
        """
        self.session.add(pagamento)
        await self.session.commit()
        return pagamento

    async def get_pagamentos(self):
        """
        Listagem de pagamentos.

        Returns:
            Uma lista com todos os pagamentos.
        """
        return self.session.query(Pagamento).all()

    async def get_pagamento_by_id(self, id: int):
        """
        Busca um pagamento por ID.

        Args:
            id: O ID do pagamento a ser buscado.

        Returns:
            O pagamento encontrado.
        """
        return self.session.query(Pagamento).get(id)

    async def update_pagamento(self, id: int, pagamento: Pagamento):
        """
        Atualizar um pagamento.

        Args:
            id: O ID do pagamento a ser atualizado.
            pagamento: O pagamento com as alterações.

        Returns:
            O pagamento atualizado.
        """
        pagamento_existente = self.session.query(Pagamento).get(id)
        if pagamento_existente is None:
            raise HTTPException(status_code=404, detail="Pagamento não encontrado")
        pagamento_existente.valor_pago = pagamento.valor_pago
        pagamento_existente.status = pagamento.status
        await self.session.commit()
        return pagamento_existente

    async def delete_pagamento(self, id: int):
        """
        Exclui um pagamento.

        Args:
            id: O ID do pagamento a ser excluído.

        Returns:
            Um objeto vazio.
        """
        pagamento_existente = self.session.query(Pagamento).get(id)
        if pagamento_existente is None:
            raise HTTPException(status_code=404, detail="Pagamento não encontrado")
        self.session.delete(pagamento_existente)
        await self.session.commit()
        return {}