from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from app.api.cliente import cliente_bp
    from app.api.produto import produto_bp
    from app.api.pedido import pedido_bp
    from app.api.item_pedido import item_pedido_bp
    from app.api.pagamento import pagamento_bp

    app.register_blueprint(cliente_bp, url_prefix='/cliente')
    app.register_blueprint(produto_bp, url_prefix='/produto')
    app.register_blueprint(pedido_bp, url_prefix='/pedido')
    app.register_blueprint(item_pedido_bp, url_prefix='/item_pedido')
    app.register_blueprint(pagamento_bp, url_prefix='/pagamento')

    return app
