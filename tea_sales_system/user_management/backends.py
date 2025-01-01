from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend


class CustomAuthBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        UserModel = get_user_model()  # 获取自定义用户模型
        try:
            user = UserModel.objects.get(username=username)  # 根据用户名查找用户
        except UserModel.DoesNotExist:
            return None  # 用户不存在

        if user.check_password(password):  # 检查密码是否匹配
            return user  # 认证成功，返回用户对象

        return None  # 密码不匹配

    def get_user(self, user_id):
        UserModel = get_user_model()
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None