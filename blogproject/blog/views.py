from django.conf import settings
from django.shortcuts import render, get_object_or_404
from blog.models import Article
from django.core.paginator import Paginator


def index(request):
    # 分页的url--->?page=1
    page = request.GET.get('page')
    article_list = Article.objects.all()  # 查出所有文章
    paginator = Paginator(object_list=article_list, per_page=settings.PER_PAGE)  # 分页的对象列表，每页分多少元素
    article_list = paginator.get_page(page)
    context = {'article_list': article_list}
    return render(request, 'blog/index.html', context=context)


def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'blog/detail.html', {'category': article})
