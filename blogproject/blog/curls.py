from django.urls import path

from . import cviews

app_name = 'category'  # 命名空间
urlpatterns = [
    path('add', cviews.add, name='add'),

]
#