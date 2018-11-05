from django.shortcuts import render
from django.http import HttpResponse

from blog.forms import CategoryModelForm


def add(request):
    if request.method == 'GET':
        form = CategoryModelForm()
        return render(request, 'category/add.html', {'form': form})
    else:
        form = CategoryModelForm(request.POST)
        if form.is_valid():  # 验证通过，数据合法
            form.save()  # 保存数据
            return HttpResponse('success')
        else:  # 验证不通过
            return render(request, 'category/add.html', {'form': form})
