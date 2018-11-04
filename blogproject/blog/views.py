from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from blog.models import Article


def index(request):
    article_list = Article.objects.all()
    context = {'article_list':article_list}
    return render(request,'index.html',context=context)

def detail(request,pk):

    return render(request,'detail.html')
