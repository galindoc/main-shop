import logging


class Logger:
    def info(message):
        logging.basicConfig(format='[%(asctime)s] [%(levelname)s] - %(message)s', level=logging.INFO)
        logging.info(message)

    def error(message):
        logging.basicConfig(format='[%(asctime)s] [%(levelname)s] - %(message)s', level=logging.ERROR)
        logging.error(message)

    def warning(message):
        logging.basicConfig(format='[%(asctime)s] [%(levelname)s] - %(message)s', level=logging.WARNING)
        logging.warning(message)
