from sqlalchemy import Column, Integer, String, DECIMAL, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Produto(Base):
    """
    Modelo de produto.
    """

    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(255), nullable=False)
    descricao = Column(String(255), nullable=False)
    preco = Column(DECIMAL(10, 2), nullable=False)
    criado_em = Column(Date, default=func.now())
    atualizado_em = Column(Date, onupdate=func.now())

    def __repr__(self):
        return f"<Produto {self.id}>"


class ProdutosRepository:
    """
    Repository de produtos.
    """

    def __init__(self, session: Session):
        self.session = session

    def create_produto(self, produto_request: ProdutoRequest) -> Produto:
        """
        Cria um novo produto.

        Args:
            produto_request: A solicitação de produto.

        Returns:
            O produto criado.
        """
        produto = Produto(
            nome=produto_request.nome,
            descricao=produto_request.descricao,
            preco=produto_request.preco,
        )
        self.session.add(produto)
        self.session.commit()
        return produto

    def get_produtos(self) -> list[Produto]:
        """
        Listagem de produtos.

        Returns:
            Uma lista com todos os produtos.
        """
        return self.session.query(Produto).all()

    def get_produto_by_id(self, id: int) -> Produto:
        """
        Busca um produto por ID.

        Args:
            id: O ID do produto a ser buscado.

        Returns:
            O produto encontrado.
        """
        return self.session.query(Produto).filter_by(id=id).first()

    def update_produto(self, id: int, produto: Produto) -> Produto:
        """
        Atualizar um produto.

        Args:
            id: O ID do produto a ser atualizado.
            produto: O produto a ser atualizado.

        Returns:
            O produto atualizado.
        """
        produto_existente = self.get_produto_by_id(id)
        if produto_existente is None:
            raise HTTPException(status_code=404, detail="Produto não encontrado")
        produto_existente.nome = produto.nome
        produto_existente.descricao = produto.descricao
        produto_existente.preco = produto.preco
        self.session.commit()
        return produto_existente

    def delete_produto(self, id: int) -> None:
        """
        Exclui um produto.

        Args:
            id: O ID do produto a ser excluído.

        Returns:
            None.
        """
        produto_existente = self.get_produto_by_id(id)
        if produto_existente is None:
            raise HTTPException(status_code=404, detail="Produto não encontrado")
        self.session.delete(produto_existente)
        self.session.commit()