from flask import Flask
from flask_cors import CORS
from app.api.cliente import cliente_bp
from app.api.produto import produto_bp
from app.api.pedido import pedido_bp
from app.api.item_pedido import item_pedido_bp
from app import db


def create_app():
    app = Flask(__name__)
    CORS(app)

    app.config.from_object("config.Config")

    db.init_app(app)

    app.register_blueprint(cliente_bp)
    app.register_blueprint(produto_bp)
    app.register_blueprint(pedido_bp)
    app.register_blueprint(item_pedido_bp)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
