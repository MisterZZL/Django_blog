from django import forms

from blog.models import Category, Article


class ArticleModelForm(forms.ModelForm):
    class Meta:
        model = Article  # 指定模型
        # fields = ['name','desc']#指定要验证的字段
        exclude = []
