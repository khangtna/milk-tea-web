# Generated by Django 4.1.6 on 2023-02-18 14:54

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_alter_mon_hinhanh'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mon',
            name='hinhAnh',
            field=models.ImageField(default=None, storage=django.core.files.storage.FileSystemStorage(location='/static/homepage/img'), upload_to='img'),
        ),
    ]
