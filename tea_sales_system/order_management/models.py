from django.db import models

from product_management.models import Product
from user_management.models import User, Address


class Order(models.Model):
    ORDER_STATUS_CHOICES  = (
        ('pending_payment', '待付款'),
        ('pending_shipment', '待发货'),
        ('pending_receipt', '待收货'),
        ('pending_review', '待评价'),
        ('completed', '已完成'),
        ('cancelled', '已取消'),
    )
    AFTER_SALE_STATUS_CHOICES = [
        ('none', '无售后'),  # 默认无售后申请
        ('requested', '申请售后'),  # 用户申请售后
        ('processing', '售后处理中'),  # 售后处理中
        ('approved', '售后通过'),  # 售后申请通过
        ('rejected', '售后被拒绝'),  # 售后申请被拒绝
        ('completed', '售后完成'),  # 售后完成
    ]
    PAYMENT_STATUS = (
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('failed', 'Failed'),
    )

    PAYMENT_METHODS = (
        ('alipay', 'Alipay'),
        ('wechat', 'WeChat Pay'),
        ('paypal', 'PayPal'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default='pending_payment')
    after_sale_status = models.CharField( max_length=20, choices=AFTER_SALE_STATUS_CHOICES, default='none')
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS, default='pending')
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS, null=True, blank=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # 优惠金额
    final_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # 实际支付金额

    def get_status_display(self):
        return dict(self.ORDER_STATUS_CHOICES).get(self.status, '未知状态')

    def __str__(self):
        return f"Order {self.id} - {self.user.username}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product.name} (x{self.quantity})"


class Evaluation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_evaluation')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_evaluation')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_evaluation')
    score = models.FloatField()  # 假设评分为 1 到 5 的浮点数
    comments = models.CharField(max_length=200, blank=True, null=True)
    evaluate_time = models.DateTimeField(auto_now_add=True, null=True)

    # class Meta:
    #     unique_together = ('user', 'product')  # 确保每个用户对同一个商品只有一个评分
