from django.http import HttpResponse, HttpRequest


def hello(request):
    return HttpResponse('hello,word')
