import logging

def configure_logging():
    """
    Funcao para configurar o log do projeto.
    """
    logging.basicConfig(
        level=logging.getLevelName(Config.LOGGING_LEVEL),
        format=Config.LOGGING_FORMAT,
        datefmt=Config.LOGGING_DATE_FORMAT,
    )

if __name__ == "__main__":
    configure_logging()
