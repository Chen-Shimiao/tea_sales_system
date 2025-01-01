from django.db import models


# 商品分类
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="分类名称")
    description = models.TextField(blank=True, null=True, verbose_name="分类描述")
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subcategories', verbose_name="父级分类")

    class Meta:
        verbose_name = "商品分类"
        verbose_name_plural = "商品分类"

    def __str__(self):
        return self.name

# 商品产地
class Origin(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="产地名称")
    country = models.CharField(max_length=100, verbose_name="国家")
    description = models.TextField(blank=True, null=True, verbose_name="描述")

    class Meta:
        verbose_name = "茶叶产地"
        verbose_name_plural = "茶叶产地"
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} ({self.country})"

# 商品
class Product(models.Model):
    STATUS_CHOICES = (
        ('0', '上架'),
        ('1', '下架'),
    )
    id = models.BigAutoField(primary_key=True)
    product_id = models.CharField(blank=True, max_length=128)
    description = models.CharField(max_length=500)
    category  = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True,
                                         related_name='category_product')
    origin = models.ForeignKey(Origin, on_delete=models.CASCADE, blank=True, null=True,)
    name = models.CharField(max_length=100, blank=True, null=True)
    cover = models.ImageField(upload_to='cover/', null=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='0')
    cost_price = models.DecimalField(max_digits=18, decimal_places=3)
    sales_price = models.DecimalField(max_digits=18, decimal_places=3)
    stock = models.DecimalField(max_digits=18, decimal_places=3, default=0.000)
    create_time = models.DateTimeField(auto_now_add=True, null=True)
    promotion = models.ManyToManyField(
        'Promotion', null=True, blank=True,verbose_name="促销活动"
    )

    def __str__(self):
        return self.name

    def reduce_stock(self, quantity):
        """减少库存"""
        if quantity > self.stock:
            raise ValueError("库存不足")
        self.stock -= quantity
        self.save()

    def increase_stock(self, quantity):
        """增加库存"""
        self.stock += quantity
        self.save()

#促销活动
class Promotion(models.Model):
    PROMOTION_TYPE_CHOICES = [
        ('discount', '打折'),
        ('full_reduction', '满减'),
        ('buy_gift', '买赠'),
    ]

    name = models.CharField(max_length=100, verbose_name="促销活动名称")
    promotion_type = models.CharField(max_length=20, choices=PROMOTION_TYPE_CHOICES, verbose_name="促销类型")
    discount = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, verbose_name="折扣(如0.8代表8折)")
    full_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="满减条件金额")
    reduction_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="满减金额")
    buy_quantity = models.IntegerField(null=True, blank=True, verbose_name="买赠条件数量")
    gift_quantity = models.IntegerField(null=True, blank=True, verbose_name="赠送数量")
    start_time = models.DateTimeField(verbose_name="活动开始时间")
    end_time = models.DateTimeField(verbose_name="活动结束时间")
    is_active = models.BooleanField(default=True, verbose_name="是否启用")
    priority = models.IntegerField(default=100, verbose_name="优先级")  # 数值越小优先级越高
    allow_stack = models.BooleanField(default=False, verbose_name="是否允许叠加")
    applicable_products = models.ManyToManyField('Product', blank=True, related_name='promotions')
    def __str__(self):
        return self.name

