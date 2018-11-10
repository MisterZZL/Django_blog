from django.urls import path

from . import cviews

app_name = 'article'  # 命名空间
urlpatterns = [
    # path中第一个参数add后不加左斜线，get请求时url也不要加,否则会404
    # 如果加上，get请求时url如果没加，不会报错，但有一次301跳转
    path('add/', cviews.add, name='add'),
    path('list/', cviews.list, name='list'),
    path('edit/<pk>', cviews.edit, name='edit'),
    path('delete/<pk>', cviews.delete, name='delete'),

]
