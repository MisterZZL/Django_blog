from django import forms

from blog.models import Category


class CategoryModelForm(forms.ModelForm):
    class Meta:
        model = Category  # 指定模型
        # fields = ['name','desc']#指定要验证的字段
        exclude = []
