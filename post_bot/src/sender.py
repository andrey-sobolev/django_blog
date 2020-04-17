import logging

import urllib.parse
import requests


logger = logging.getLogger()


class Sender:
    REGISTER_URL = 'api/members/'
    AUTHORIZE_URL = 'api/token/'
    POST_URL = '/api/post/'
    LIKE_URL = 'api/post/{post}/like/'
    
    def __init__(self, domain, user_email, user_name, user_password):
        self.domain = domain
        self.user_email = user_email
        self.user_name = user_name
        self.user_password = user_password
        
        self.token = ''
    
    def get_request_head(self):
        return {'Authorization': 'Bearer ' + self.token}
        
    def send_auth(self):
        complete = False
        url = urllib.parse.urljoin(self.domain, self.AUTHORIZE_URL)
        body = {
            'password': self.user_password,
            'email': self.user_email,
        }
        response = requests.post(url, json=body)
        if response.status_code == 200:
            complete = True
            result = response.json()
            self.token = result['access']
        return complete
    
    def send_register(self):
        complete = False
        url = urllib.parse.urljoin(self.domain, self.REGISTER_URL)
        body = {
            'password': self.user_password,
            'username': self.user_name,
            'email': self.user_email,
        }
        response = requests.post(url, json=body)
        if response.status_code == 201:
            complete = True
        return complete
        
    def send_post(self, post_title, post_text):
        complete = False
        url = urllib.parse.urljoin(self.domain, self.POST_URL)
        body = {
            'title': post_title,
            'detail': post_text,
        }
        response = requests.post(url, json=body, headers=self.get_request_head())
        if response.status_code == 201:
            complete = True
        return complete
    
    def get_post_list(self):
        complete = False
        result = None
        url = urllib.parse.urljoin(self.domain, self.POST_URL)
        response = requests.get(url, headers=self.get_request_head())
        if response.status_code == 200:
            result = response.json()
            complete = True
        return complete, result
    
    def send_like(self, post_id):
        complete = False
        url = urllib.parse.urljoin(self.domain, self.LIKE_URL.format(post=post_id))
        response = requests.post(url, headers=self.get_request_head())
        if response.status_code == 201:
            complete = True
        return complete
