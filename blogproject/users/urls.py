from django.urls import path
from django.contrib.auth import views as auth_views
from users.forms import AuthForm

from . import views


SUCCESS_URL = '/success?msg='

app_name = 'users'  # 命名空间
urlpatterns = [
    path('register', views.register, name='register'),
    path('success', views.success, name='success'),

    path('login/', auth_views.LoginView.as_view(
        form_class=AuthForm,
        extra_context={'title': '登录'},
        template_name='form.html'
    ), name='login'),

    path('logout/', auth_views.LogoutView.as_view(
        next_page=SUCCESS_URL + '成功注销',
    ), name='logout'),

    path('password_change/', auth_views.PasswordChangeView.as_view(
        template_name='form.html',
        success_url=SUCCESS_URL + '恭喜你，密码修改成功！',
    ), name='password_change'),

    path('password_reset/', auth_views.PasswordResetView.as_view(
        email_template_name='users/password_reset_email.html',
        template_name='form.html',
        success_url=SUCCESS_URL + '重置密码的邮件已发送！',
    ), name='password_reset'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='form.html',
        success_url=SUCCESS_URL + '密码已重置！',
    ), name='password_reset_confirm'),
]
