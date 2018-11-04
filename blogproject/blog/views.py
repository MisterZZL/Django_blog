from django.shortcuts import render, get_object_or_404
from blog.models import Article
import markdown


def index(request):
    article_list = Article.objects.all()
    context = {'article_list': article_list}
    return render(request, 'index.html', context=context)


def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    md_content = markdown.markdown(article.content,
                                   extensions=[
                                       'markdown.extensions.extra',  # 基础应用
                                       'markdown.extensions.codehilite',  # 代码高亮
                                       'markdown.extensions.toc'  # 目录结构
                                   ])
    return render(request, 'detail.html', {'article': article,'md_content':md_content})
