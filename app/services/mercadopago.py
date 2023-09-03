from typing import Any, Dict

from mercadopago import MercadoPago


class MercadoPagoService:
    """
    Serviço de pagamentos do Mercado Pago.
    """

    def __init__(self, client_id: str, client_secret: str):
        self.client_id = client_id
        self.client_secret = client_secret

    def realizar_pagamento(
        self,
        valor_pago: Decimal,
        status: str,
        pedido_id: int,
    ) -> Dict[str, Any]:
        """
        Realiza um pagamento pelo Mercado Pago.

        Args:
            valor_pago: O valor pago do pedido.
            status: O status do pagamento.
            pedido_id: O ID do pedido associado ao pagamento.

        Returns:
            As informações do pagamento.
        """
        mercadopago = MercadoPago(
            client_id=self.client_id, client_secret=self.client_secret
        )
        payment = mercadopago.create_payment(
            amount=valor_pago, status=status, order_id=pedido_id
        )
        return payment