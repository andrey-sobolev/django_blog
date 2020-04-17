import json


class DataReader:
    def __init__(self, config):
        self.user_registration_data_file = config.USER_REGISTRATION_DATA_FILE
        self.user_posts_data_folder = config.USER_POSTS_DATA_FILE
        
    def get_users(self, count_of_users):
        with open(self.user_registration_data_file) as file:
            json_data = json.load(file)
            for user_data in json_data:
                if not count_of_users > 0:
                    break
                yield user_data.get('email'), user_data.get('username'), user_data.get('password')
                count_of_users -= 1
    
    def get_posts(self, count_of_posts):
        # if count_of_posts large then posts in file we will get old posts again
        while count_of_posts > 0:
            with open(self.user_posts_data_folder) as file:
                json_data = json.load(file)
                for user_data in json_data:
                    if not count_of_posts > 0:
                        break
                    yield user_data.get('title'), user_data.get('text')
                    count_of_posts -= 1
