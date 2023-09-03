from fastapi import FastAPI
from app.api.endpoints.dependencies import get_session
from app.api.endpoints.pedidos import pedidos_router
from app.api.endpoints.produtos import produtos_router
from app.api.endpoints.clientes import clientes_router
from app.api.endpoints.pagamentos import pagamentos_router


app = FastAPI()


app.include_router(pedidos_router, prefix="/pedidos")
app.include_router(produtos_router, prefix="/produtos")
app.include_router(clientes_router, prefix="/clientes")
app.include_router(pagamentos_router, prefix="/pagamentos")


@app.on_event("startup")
async def startup_event():
    """
    Evento de inicialização da API.
    """
    await init_db()


async def init_db():
    """
    Inicializa o banco de dados.
    """
    session = await get_session()
    await session.execute("CREATE TABLE IF NOT EXISTS pedidos (id INT AUTO_INCREMENT PRIMARY KEY, data DATE, valor_total DECIMAL(10, 2), cliente_id INT, produtos JSON)")
    await session.execute("CREATE TABLE IF NOT EXISTS clientes (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255), email VARCHAR(255), telefone VARCHAR(255))")
    await session.execute("CREATE TABLE IF NOT EXISTS produtos (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255), valor DECIMAL(10, 2))")
    await session.execute("CREATE TABLE IF NOT EXISTS pagamentos (id INT AUTO_INCREMENT PRIMARY KEY, pedido_id INT, valor_pago DECIMAL(10, 2), status VARCHAR(255))")
    await session.commit()