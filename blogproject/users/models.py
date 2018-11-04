from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    nickname = models.CharField(max_length=32, verbose_name='昵称', unique=True)

    class Meta(AbstractUser.Meta):
        pass
