from django.conf import settings
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

from blog.forms import ArticleModelForm
from blog.models import Article


def list(request):
    q = request.GET.get('q', '')  # 有q值就获取q关键字，没有就默认给一个空字符串
    page = request.GET.get('page')
    # article_list = Article.objects.all()  # 查出所有文章
    article_list = Article.objects.filter(#Q | 实现“模糊、或”的查询
        Q(title__contains=q) | Q(content__contains=q))#title包含q或content包含q
    paginator = Paginator(object_list=article_list, per_page=settings.PER_PAGE)  # 分页的对象列表，每页分多少元素
    article_list = paginator.get_page(page)
    context = {'article_list': article_list}
    return render(request, 'article/list.html', context=context)


def add(request):
    if request.method == 'POST':
        form = ArticleModelForm(request.POST)
        if form.is_valid():  # 验证通过，数据合法
            form.save()  # 保存数据
            messages.add_message(request, messages.SUCCESS, '添加成功')  # 闪现消息
            return redirect('article:list')  # 跳转list页面
    else:
        form = ArticleModelForm()
    return render(request, 'article/add.html', {'form': form})


def edit(request,pk):
    article = get_object_or_404(Article,pk = pk)
    if request.method == 'POST':
        form = ArticleModelForm(request.POST,instance=article)
        if form.is_valid():  # 验证通过，数据合法
            form.save()  # 保存数据
            messages.add_message(request, messages.SUCCESS, '编辑成功')  # 闪现消息
            return redirect('article:list')  # 跳转list页面
    else:
        form = ArticleModelForm(instance=article)
    return render(request, 'article/add.html', {'form': form})


def delete(request,pk):
    article = get_object_or_404(Article,pk = pk)#找到文章
    article.delete()
    messages.add_message(request, messages.SUCCESS, '删除成功')  # 闪现消息
    return redirect('article:list')  # 跳转list页面

