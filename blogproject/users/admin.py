from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from users.models import User


@admin.register(User)
class UsersUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff','nickname')#展示字段
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups','nickname')#界面右侧的过滤器
    search_fields = ('username', 'first_name', 'last_name', 'email','nickname')#搜索过滤（通过那些字段来搜索）

