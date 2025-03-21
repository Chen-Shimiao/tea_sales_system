# Generated by Django 3.2.25 on 2024-11-16 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_management', '0006_auto_20241116_2212'),
    ]

    operations = [
        migrations.AddField(
            model_name='promotion',
            name='applicable_products',
            field=models.ManyToManyField(blank=True, related_name='promotions', to='product_management.Product'),
        ),
        migrations.RemoveField(
            model_name='product',
            name='promotion',
        ),
        migrations.AddField(
            model_name='product',
            name='promotion',
            field=models.ManyToManyField(blank=True, null=True, to='product_management.Promotion', verbose_name='促销活动'),
        ),
    ]
