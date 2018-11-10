from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    nickname = models.CharField(max_length=32, verbose_name='昵称', unique=True)
    email = models.EmailField(verbose_name='邮箱', unique=True)  # 邮箱不能重复

    class Meta(AbstractUser.Meta):
        pass
