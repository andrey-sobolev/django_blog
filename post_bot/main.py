import logging
import logging.config

from src import create_app
from config import Config


def run():
    logging.config.fileConfig('logging.conf')
    logger = logging.getLogger()
    app = create_app(Config)
    logger.info('run application')
    app.run()
    logger.info('finish application')


if __name__ == '__main__':
    run()
