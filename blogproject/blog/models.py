from django.db import models



# Create your models here.

# 用户 文章 分类 标签 评论
# 模型字段
# 用户: id 昵称 电子邮箱 密码
# 分类：id 名称
# 标签：id 名称
# 文章：id author 创建时间 修改时间 阅读次数 标题 文章内容 摘要 分类
# 评论：id user 文章 内容 创建时间
from users.models import User


class CreateTimeModel(models.Model):
    created_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)  # 创建时间

    class Meta:  # 抽象类，不生实体成表
        abstract = True


class Category(models.Model):  # 文章分类
    name = models.CharField(verbose_name='名称', max_length=32, unique=True)

    class Meta:
        verbose_name = '类别'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tag(models.Model):  # 文章标签
    name = models.CharField(verbose_name='标签', max_length=32, unique=True)

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Article(CreateTimeModel):  # 文章
    author = models.ForeignKey(User, verbose_name='作者', on_delete=models.CASCADE)  # 外键删除时的选项,级联删除
    title = models.CharField(verbose_name='标题', max_length=32)  # 标题
    content = models.TextField(verbose_name='内容')  # 文章内容
    excerpt = models.CharField(verbose_name='摘要', max_length=128)  # 摘要
    views = models.PositiveIntegerField(verbose_name='浏览次数', default=0)  # 阅读量
    modified_time = models.DateTimeField(verbose_name='修改时间', auto_now=True)  # 修改时间
    category = models.ForeignKey(Category, verbose_name='类别', on_delete=models.CASCADE)  # 文章的分类
    tags = models.ManyToManyField(Tag, verbose_name='标签')  # 一篇文章可以有多个标签，一个标签可以对应多篇文章，多对多

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Comment(CreateTimeModel):  # 评论
    user = models.ForeignKey(User, verbose_name='用户', on_delete=models.CASCADE)  # 评论的人
    article = models.ForeignKey(Article, verbose_name='文章', on_delete=models.CASCADE)  # 评论的哪篇文章
    content = models.TextField(verbose_name='评论内容', max_length=1024)  # 评论内容

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content
