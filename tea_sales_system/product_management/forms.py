from django import forms
from .models import Product, Category, Promotion, Origin


class ProductForm(forms.ModelForm):
    product_id = forms.CharField(
        label='商品编号',  # 标签
        widget=forms.TextInput(attrs={
            'class': 'form-control custom-input',  # 应用 form-control 类
            'placeholder': '请输入商品编号',  # 设置提示文字
            'style': 'width:40%'
        })
    )
    name = forms.CharField(
        label='商品名',  # 标签
        widget=forms.TextInput(attrs={
            'class': 'form-control custom-input',  # 应用 form-control 类
            'placeholder': '请输入商品名',  # 设置提示文字
            'style': 'width:40%'
        })
    )
    description = forms.CharField(
        label='商品描述',  # 标签
        widget=forms.Textarea(attrs={
            'class': 'form-control custom-input',  # 应用 form-control 类
            'placeholder': '请输入商品描述',  # 设置提示文字
            'style': 'width:40%; height:50px'
                     ''
        })
    )
    category = forms.ModelChoiceField(
        label='商品分类',
        queryset=Category.objects.filter(),  # 仅显示顶级分类
        widget=forms.Select(attrs={'class': 'form-select'})  # 使用 Bootstrap 的样式
    )
    origin = forms.ModelChoiceField(
        label='产地',
        queryset=Origin.objects.filter(),  # 仅显示顶级分类
        widget=forms.Select(attrs={'class': 'form-select'})  # 使用 Bootstrap 的样式
    )
    status = forms.ChoiceField(
        label='状态',  # 标签
        choices=[('0', '上架'), ('1', '下架')],
        widget=forms.Select(attrs={'class': 'form-select'}),
    )
    cover = forms.FileField(
        label='图片',
    )

    cost_price=forms.DecimalField(
        label='商品进价'
    )
    sales_price = forms.DecimalField(
        label='商品售价'
    )
    promotion = forms.ModelMultipleChoiceField(
        queryset=Promotion.objects.filter(is_active=True),  # 只显示有效的促销活动
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="选择促销活动"
    )

    class Meta:
        model = Product
        fields = ['product_id','name', 'description', 'category','origin','cover','status','cost_price','sales_price','promotion']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']

class CustomClearableFileInput(forms.ClearableFileInput):
    template_name = 'widgets/custom_clearable_file_input.html'  # 指定自定义模板

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('attrs', {}).update({'class': 'form-control'})
        super().__init__(*args, **kwargs)