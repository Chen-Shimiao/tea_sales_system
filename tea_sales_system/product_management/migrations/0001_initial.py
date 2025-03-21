# Generated by Django 3.2.25 on 2024-10-30 01:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('product_id', models.CharField(blank=True, max_length=128)),
                ('description', models.CharField(max_length=500)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('cover', models.ImageField(null=True, upload_to='cover/')),
                ('status', models.CharField(choices=[('0', '上架'), ('1', '下架')], default='0', max_length=1)),
                ('cost_price', models.DecimalField(decimal_places=3, max_digits=18)),
                ('sales_price', models.DecimalField(decimal_places=3, max_digits=18)),
                ('stock', models.DecimalField(decimal_places=3, max_digits=18)),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category_product', to='product_management.category')),
            ],
        ),
    ]
