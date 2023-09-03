from fastapi import APIRouter, Depends, HTTPException
from app.api.dependencies import get_session
from app.crud.produtos import ProdutosRepository
from app.schemas.produtos import ProdutoRequest, ProdutoResponse, ProdutoListResponse


router = APIRouter()


@router.post("/", response_model=ProdutoResponse)
async def criar_produto(
    produto_request: ProdutoRequest,
    session: Session = Depends(get_session),
):
    """
    Cria um novo produto.

    Args:
        produto_request: A solicitação de produto.
        session: A sessão do banco de dados.

    Returns:
        O produto criado.
    """

    produto = ProdutosRepository(session).create_produto(produto_request)
    return produto


@router.get("/", response_model=ProdutoListResponse)
async def listar_produtos(
    session: Session = Depends(get_session),
):
    """
    Listagem de produtos.

    Args:
        session: A sessão do banco de dados.

    Returns:
        Uma lista com todos os produtos.
    """

    produtos = ProdutosRepository(session).get_produtos()
    return ProdutoListResponse(produtos=produtos)


@router.get("/{id}", response_model=ProdutoResponse)
async def buscar_produto_por_id(
    id: int, session: Session = Depends(get_session),
):
    """
    Busca um produto por ID.

    Args:
        id: O ID do produto a ser buscado.
        session: A sessão do banco de dados.

    Returns:
        O produto encontrado.
    """

    produto = ProdutosRepository(session).get_produto_by_id(id)
    if produto is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto


@router.put("/{id}", response_model=ProdutoResponse)
async def atualizar_produto(
    id: int,
    produto_request: ProdutoRequest,
    session: Session = Depends(get_session),
):
    """
    Atualizar um produto.

    Args:
        id: O ID do produto a ser atualizado.
        produto_request: A solicitação de atualização do produto.
        session: A sessão do banco de dados.

    Returns:
        O produto atualizado.
    """

    produto_existente = ProdutosRepository(session).get_produto_by_id(id)
    if produto_existente is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    produto_existente.nome = produto_request.nome
    produto_existente.descricao = produto_request.descricao
    produto_existente.preco = produto_request.preco
    return ProdutosRepository(session).update_produto(id, produto_existente)


@router.delete("/{id}")
async def excluir_produto(
    id: int, session: Session = Depends(get_session),
):
    """
    Exclui um produto.

    Args:
        id: O ID do produto a ser excluído.
        session: A sessão do banco de dados.

    Returns:
        Um objeto vazio.
    """

    produto_existente = ProdutosRepository(session).get_produto_by_id(id)
    if produto_existente is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    ProdutosRepository(session).delete_produto(id)
    return {}
