from django.db import migrations
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model

def create_superuser(apps, schema_editor):
    User = get_user_model()
    User.objects.create(
        username='admin',
        email='497898@qq.com',
        phone='15230378721',
        gender='M',
        password=make_password('adminpassword'),
        birthday='2024-10-31 00:00:00.000000',
        is_superuser=1,
        is_staff=1,
        is_active=1,
    )

class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0006_auto_20241105_2115'),
    ]

    operations = [
        migrations.RunPython(create_superuser),
    ]
