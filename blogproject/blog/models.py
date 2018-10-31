from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# 用户 文章 分类 标签 评论
# 模型字段
# 用户: id 昵称 电子邮箱 密码
# 分类：id 名称
# 标签：id 名称
# 文章：id author 创建时间 修改时间 阅读次数 标题 文章内容 摘要 分类
# 评论：id user 文章 内容 创建时间


class Category(models.Model):  # 文章分类
    name = models.CharField(max_length=32, unique=True)


class Tag(models.Model):  # 文章标签
    name = models.CharField(max_length=32, unique=True)


class Article(models.Model):  # 文章
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # 外键删除时的选项,级联删除
    title = models.CharField(max_length=32)  # 标题
    content = models.TextField()  # 文章内容
    excerpt = models.CharField(max_length=128)  # 摘要
    views = models.PositiveIntegerField(default=0)  # 阅读量
    created_time = models.DateTimeField(auto_now_add=True)  # 创建时间
    modified_time = models.DateTimeField(auto_now=True)  # 修改时间
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # 文章的分类
    tags = models.ManyToManyField(Tag)  # 一篇文章可以有多个标签，一个标签可以对应多篇文章，多对多


class Comment(models.Model):  # 评论
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 评论的人
    article = models.ForeignKey(Article, on_delete=models.CASCADE)  # 评论的哪篇文章
    content = models.TextField(max_length=1024)  # 评论内容
    created_time = models.DateTimeField(auto_now_add=True)  # 评论的时间
