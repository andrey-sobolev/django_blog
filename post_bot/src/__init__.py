from .data_reader import DataReader
from .sender import Sender
from .post_bot import PostBot


def create_app(config):
    data_reader_ = DataReader(config)
    app = PostBot(config, data_reader_)
    return app
