import os

class Config:
    """
    Configuração da aplicação.
    """

    ENV = os.getenv("ENV", "dev")

    if ENV == "prod":
        DEBUG = False
        SECRET_KEY = os.getenv("SECRET_KEY")
        ACCESS_TOKEN_EXPIRY_MINUTES = 60 * 24
    else:
        DEBUG = True
        SECRET_KEY = "some-secret-key"
        ACCESS_TOKEN_EXPIRY_MINUTES = 60 * 5

    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config = Config()