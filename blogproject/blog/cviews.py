from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib import messages

from .models import Category, Article
from .forms import CategoryForm, ArticleModelForm

def list(request):
    # ?page=1&q=django
    q = request.GET.get('q', '')
    page = request.GET.get('page')
    article_list = Article.objects.filter(
        Q(title__contains=q) | Q(content__contains=q))
    paginator = Paginator(article_list, settings.PER_PAGE)
    article_list = paginator.get_page(page)
    context = {'article_list': article_list}
    return render(request, 'article/list.html', context)


def add(request):  # get post
    if request.method == 'POST':
        form = ArticleModelForm(request.POST)
        if form.is_valid():
            # 保存数据
            form.save()
            messages.add_message(request, messages.SUCCESS, '添加成功！')
            return redirect('article:list')
    else:
        form = ArticleModelForm()
    return render(request, 'article/add.html', {'form': form})


def edit(request, pk):  # get post
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = ArticleModelForm(request.POST, instance=article)
        if form.is_valid():
            # 保存数据
            form.save()
            messages.add_message(request, messages.SUCCESS, '编辑成功！')
            return redirect('article:list')
    else:
        form = ArticleModelForm(instance=article)
    return render(request, 'article/add.html', {'form': form})


def delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    messages.add_message(request, messages.SUCCESS, '删除成功！')
    return redirect('article:list')
