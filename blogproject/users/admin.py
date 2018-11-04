from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from users.models import User


class UsersUserAdmin(UserAdmin):
    def __init__(self, *args, **kwargs):
        super(UsersUserAdmin, self).__init__(*args, **kwargs)
        self.list_display = self.list_display + ('nickname',)  # 展示字段
        self.list_filter = self.list_filter + ('nickname',)  # 界面右侧的过滤器
        self.search_fields = self.search_fields + ('nickname',)  # 搜索过滤（通过那些字段来搜索）
        self.fieldsets[1][1]['fields'] = ('first_name', 'last_name', 'email', 'nickname')


admin.site.register(User, UsersUserAdmin)
