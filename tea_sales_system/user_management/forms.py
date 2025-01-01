from django import forms
from .models import User, Address


class UserForm(forms.ModelForm):
    username = forms.CharField(
        label='用户名',  # 标签
        widget=forms.TextInput(attrs={
            'class': 'form-control custom-input',  # 应用 form-control 类
            'placeholder': '请输入用户名',  # 设置提示文字
            'style': 'width:40%'
        })
    )
    password = forms.CharField(
        label='密码',  # 标签
        widget=forms.TextInput(attrs={
            'class': 'form-control custom-input',  # 应用 form-control 类
            'placeholder': '请输入默认密码',  # 设置提示文字
            'style': 'width:40%'
        })
    )
    gender = forms.ChoiceField(
        label='性别',  # 标签
        choices=[('M', '男'), ('F', '女')],
        widget=forms.Select(attrs={
            'class': 'form-control custom-input',  # 应用 form-control 类
            'placeholder': '请选择性别',  # 设置提示文字
            'style': 'width:40%'
        })
    )
    email = forms.EmailField(
        label="邮箱",
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': '请输入邮箱',
            'style': 'width:40%'
        })
    )
    phone = forms.CharField(
        label='手机号码',
        max_length=11,
        widget=forms.TextInput(attrs={
            'type': 'tel',
            'class': 'form-control',
            'placeholder': '请输入手机号码',
            'pattern': '[0-9]{11}',  # 假设手机号为11位数
            'style': 'width:40%'
        })
    )

    birthday = forms.DateField(
        label='生日',  # 标签
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control',
            'placeholder': '请选择生日',
            'style': 'width:40%'
        }, format='%Y-%m-%d')
    )
    is_active = forms.BooleanField(
        label="Active",
        required=False,# 设置为非必填，未勾选则为 False
        initial=True,
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input'}))

    is_staff = forms.BooleanField(
        label="是否为管理员",
        required=False,# 设置为非必填，未勾选则为 False
        initial=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input'}))

    class Meta:
        model = User
        fields = ['username', 'password', 'gender', 'email', 'phone', 'birthday','is_active','is_staff']


    def save(self, commit=True):
        # 从表单数据创建 User 实例
        user = super().save(commit=False)  # 不立即保存到数据库

        # 你可以在这里执行额外的逻辑，例如添加默认值、验证等

        # 现在保存到数据库
        if commit:
            user.save()

        return user


class AddressForm(forms.ModelForm):
    full_name = forms.CharField(
        label='姓名',  # 标签
        widget=forms.TextInput(attrs={
            'class': 'form-control custom-input',  # 应用 form-control 类
            'placeholder': '请输入姓名',  # 设置提示文字
            'style': 'width:40%'
        })
    )
    phone_number = forms.CharField(
        label='手机号码',
        max_length=11,
        widget=forms.TextInput(attrs={
            'type': 'tel',
            'class': 'form-control',
            'placeholder': '请输入手机号码',
            'pattern': '[0-9]{11}',  # 假设手机号为11位数
            'style': 'width:40%'
        })
    )
    postal_code = forms.CharField(
        label='邮政编码',
        max_length=6,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '请输入邮政编码',
            'pattern': '[0-9]{6}',
            'style': 'width:40%'
        })
    )
    address_line = forms.CharField(
        label='详细地址',  # 标签
        widget=forms.TextInput(attrs={
            'class': 'form-control custom-input',  # 应用 form-control 类
            'placeholder': '请输入详细地址',  # 设置提示文字
            'style': 'width:40%'
        })
    )
    is_default = forms.BooleanField(
        label="是否为默认地址",
        required=False,# 设置为非必填，未勾选则为 False
        initial=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input'}))

    class Meta:
        model = Address
        fields = ['full_name', 'phone_number', 'postal_code', 'province', 'city', 'district', 'address_line',
                  'is_default']
