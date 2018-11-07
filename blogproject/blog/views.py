from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from blog.models import Article


def index(request):
    # ?page=1
    page = request.GET.get('page')
    article_list = Article.objects.all()
    paginator = Paginator(article_list, settings.PER_PAGE)
    article_list = paginator.get_page(page)
    context = {'article_list': article_list, }
    return render(request, 'blog/index.html', context)


def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'blog/detail.html', locals())
