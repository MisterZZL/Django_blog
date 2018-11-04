from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index),
    path('detail/<pk>', views.detail, name='detail'),
]
