import logging
import random

from src.sender import Sender

logger = logging.getLogger()


class PostBot:
    def __init__(self, config, data_reader):
        self.number_of_users = config.NUMBER_OF_USERS
        self.max_posts_per_user = config.MAX_POSTS_PER_USER
        self.max_likes_per_user = config.MAX_LIKES_PER_USER
        self.domain = config.DOMAIN
        
        self.data_reader = data_reader
        self.user_sender_list = []
        
    def run(self):
        self._get_user_senders()
        for user_sender_ in self.user_sender_list:
            self._create_posts(user_sender_)
        for user_sender_ in self.user_sender_list:
            self._create_likes(user_sender_)
        
    def _get_user_senders(self):
        for user_email, user_name, user_password in self.data_reader.get_users(self.number_of_users):
            self.user_sender_list.append(
                Sender(self.domain, user_email, user_name, user_password)
            )
        
    def _create_posts(self, user_sender):
        successful_auth = user_sender.send_auth()
        if not successful_auth:
            successful_auth = user_sender.send_register() and user_sender.send_auth()
            if successful_auth:
                logger.debug(f'{user_sender.user_email} new user created')

        if not successful_auth:
            logger.error(f'{user_sender.user_email} error auth with user')
            return
            
        for post_title, post_text in self.data_reader.get_posts(self.max_posts_per_user):
            logger.debug(f'{user_sender.user_email} new post created')
            user_sender.send_post(post_title, post_text)
    
    def _create_likes(self, user_sender):
        successful_auth = user_sender.send_auth()
        if not successful_auth:
            logger.error(f'{user_sender.user_email} error auth with user')
            return
        complete, post_list = user_sender.get_post_list()
        if complete:
            post_id_list = [post["id"] for post in post_list]
            for _ in range(self.max_likes_per_user):
                if not post_id_list:
                    logger.warning(f'{user_sender.user_email} no post for create more likes')
                    return
                post_like_id = random.choice(post_id_list)
                if user_sender.send_like(post_like_id):
                    logger.debug(f'{user_sender.user_email} new like for post {post_like_id} created')
                post_id_list.remove(post_like_id)
        else:
            logger.error(f'{user_sender.user_email} could not get post list')
