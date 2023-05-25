import logging


def setup_logger():
    logger = logging.getLogger(__name__)
    for handler in logger.handlers:
        logger.removeHandler(handler)
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler('log/file.log')
    file_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(levelname)s - %(asctime)s -%(module)s- %(name)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger