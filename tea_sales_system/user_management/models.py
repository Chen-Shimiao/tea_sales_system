from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import RegexValidator
from django.db import models

phone_regex = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',  # 允许国际电话号码格式
    message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
)

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser,PermissionsMixin):
    GENDER_CHOICES = (
        ('M', 'male'),
        ('F', 'female'),
    )
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=128, unique=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    phone = models.CharField(validators=[phone_regex], max_length=15, unique=True)
    birthday = models.DateTimeField()
    c_time = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    last_login = models.DateTimeField(blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'phone']

    # 必须定义 has_module_perms 方法
    def has_module_perms(self, app_label):
        return True  # 简单实现，返回True表示用户有该模块的访问权限

    def has_perm(self, perm, obj=None):
        return True  # 简单实现，返回True表示用户有所有权限

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='addresses')
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    postal_code = models.CharField(max_length=20)
    province = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    address_line = models.CharField(max_length=255)
    is_default = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.full_name}, {self.address_line}, {self.city}, {self.province}, {self.postal_code}"

    def save(self, *args, **kwargs):
        # 确保只有一个默认地址
        if self.is_default:
            Address.objects.filter(user=self.user, is_default=True).update(is_default=False)
        super().save(*args, **kwargs)
