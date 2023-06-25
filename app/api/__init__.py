from flask import Flask
from flask_cors import CORS

from app.api.cliente import cliente_bp
from app.api.produto import produto_bp
from app.api.pedido import pedido_bp

def create_app():
    app = Flask(__name__)
    CORS(app)

    app.register_blueprint(cliente_bp)
    app.register_blueprint(produto_bp)
    app.register_blueprint(pedido_bp)

    return app
