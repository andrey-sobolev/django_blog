import datetime

from django.db import models
from django.contrib.auth import get_user_model


class Post(models.Model):
    title = models.CharField(max_length=250)
    detail = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    date = models.DateTimeField(auto_now_add=True)
    
    
class Like(models.Model):
    date = models.DateTimeField(default=datetime.datetime.now)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    unique_together = ['user', 'post']
