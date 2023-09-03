import logging

def get_logger(name: str) -> logging.Logger:
    """
    Gera um logger para a aplicação.

    Args:
        name: O nome do logger.

    Returns:
        O logger.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))
    logger.addHandler(stream_handler)

    return logger

logger = get_logger(__name__)