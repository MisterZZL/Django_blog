from django.contrib import admin

# Register your models here.

from .models import Category, Tag, Article, Comment


class ArticleAdimn(admin.ModelAdmin):
    list_display = ['title', 'author', 'excerpt', 'views', 'category', 'created_time']
    search_fields = ['title', 'content','category__name']  # 增加搜索功能


admin.site.register(Article, ArticleAdimn)
admin.site.register([Category, Tag, Comment])
