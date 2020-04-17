from configparser import ConfigParser
config_parser = ConfigParser()
config_parser.read('config.ini')


class Config:
    NUMBER_OF_USERS = config_parser.getint('post_bot', 'number_of_users')
    MAX_POSTS_PER_USER = config_parser.getint('post_bot', 'max_posts_per_user')
    MAX_LIKES_PER_USER = config_parser.getint('post_bot', 'max_likes_per_user')
    
    USER_REGISTRATION_DATA_FILE = config_parser.get('data', 'user_registration_data_file')
    USER_POSTS_DATA_FILE = config_parser.get('data', 'user_posts_data_file')

    DOMAIN = config_parser.get('www', 'domain')