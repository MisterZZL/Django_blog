from django.contrib import messages
from django.shortcuts import render, redirect

from users.forms import RegisterForm


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, '恭喜你注册成功')
            return redirect('blog:index')
    else:
        form = RegisterForm()
    return render(request, 'form.html', {'form': form, 'title': '注册'})


def success(request):
    msg = request.GET.get('msg', '恭喜你，操作成功！')
    messages.add_message(request, messages.SUCCESS, msg)
    return redirect('blog:index')
