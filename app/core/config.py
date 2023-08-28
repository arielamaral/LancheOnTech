import os

class Config:
    """
    Classe para gerenciar as configurações do projeto.
    """

    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class LoggingConfig:
    """
    Classe para configurar o log do projeto.
    """

    LOGGING_LEVEL = os.getenv("LOGGING_LEVEL", "INFO")
    LOGGING_FORMAT = "%(asctime)s %(levelname)-8s %(message)s"
    LOGGING_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

