from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=255, unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']

