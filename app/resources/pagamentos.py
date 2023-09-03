from fastapi import APIRouter, Depends
from app.dependencies import get_session
from app.crud.pagamentos import PagamentosRepository
from app.schemas.pagamentos import PagamentoRequest, PagamentoResponse, PagamentoListResponse

router = APIRouter(prefix="/pagamentos")

@router.post("/")
async def create_pagamento(pagamento_request: PagamentoRequest, session: Session = Depends(get_session)):
    """
    Cadastra um novo pagamento.

    Args:
        pagamento_request: A solicitação de pagamento.
        session: O `Session` do SQLAlchemy.

    Returns:
        O pagamento criado.
    """
    pagamento = Pagamento(
        valor_pago=pagamento_request.valor_pago,
        status=pagamento_request.status,
    )
    repository = PagamentosRepository(session)
    return repository.create_pagamento(pagamento)


@router.get("/")
async def list_pagamentos(session: Session = Depends(get_session)):
    """
    Listagem de pagamentos.

    Args:
        session: O `Session` do SQLAlchemy.

    Returns:
        Uma lista de pagamentos.
    """
    repository = PagamentosRepository(session)
    return repository.get_pagamentos()


@router.get("/{id}")
async def get_pagamento_by_id(id: int, session: Session = Depends(get_session)):
    """
    Busca um pagamento por ID.

    Args:
        id: O ID do pagamento.
        session: O `Session` do SQLAlchemy.

    Returns:
        O pagamento encontrado.
    """
    repository = PagamentosRepository(session)
    return repository.get_pagamento_by_id(id)


@router.put("/{id}")
async def update_pagamento(id: int, pagamento_request: PagamentoRequest, session: Session = Depends(get_session)):
    """
    Atualizar um pagamento.

    Args:
        id: O ID do pagamento.
        pagamento_request: A solicitação de pagamento.
        session: O `Session` do SQLAlchemy.

    Returns:
        O pagamento atualizado.
    """
    repository = PagamentosRepository(session)
    return repository.update_pagamento(id, pagamento_request)


@router.delete("/{id}")
async def delete_pagamento(id: int, session: Session = Depends(get_session)):
    """
    Exclui um pagamento.

    Args:
        id: O ID do pagamento.
        session: O `Session` do SQLAlchemy.

    Returns:
        Um objeto vazio.
    """
    repository = PagamentosRepository(session)
    return repository.delete_pagamento(id)