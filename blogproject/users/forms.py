import uuid

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse

from users.models import User


class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User  # model指定为我们自己定义的User类
        fields = ('nickname', 'email')  # 要显示的字段

    def save(self, *args, **kwargs):  # 重写save方法，保存username
        if not self.instance.username:
            self.instance.username = uuid.uuid1()
        super(RegisterForm, self).save(*args, **kwargs)

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True  # email改为必填字段

    # def clean_email(self):#第一种判断邮箱已存在就抛出异常的方法，第二种是直接在用户模型中将email属性改为不能重复
    #     if User.objects.filter(email=self.cleaned_data['email']).exists():
    #         raise ValidationError('对应邮箱的用户已存在')


class AuthForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(AuthForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = '用户名或邮箱'
        url = reverse('users:password_reset')
        self.fields['password'].help_text = f'<a href="{url}">忘记密码?</a>'
