from django.shortcuts import render
from django.http import HttpResponse

from blog.forms import ArticleModelForm


def add(request):
    if request.method == 'GET':
        form = ArticleModelForm()
        return render(request, 'article/add.html', {'form': form})
    else:
        form = ArticleModelForm(request.POST)
        if form.is_valid():  # 验证通过，数据合法
            form.save()  # 保存数据
            return HttpResponse('success')
        else:  # 验证不通过
            return render(request, 'article/add.html', {'form': form})
