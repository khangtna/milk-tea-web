# Generated by Django 4.1.6 on 2023-02-18 14:04

import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Danhmuc',
            fields=[
                ('maDM', models.AutoField(primary_key=True, serialize=False)),
                ('tenDM', models.CharField(max_length=15)),
                ('ngayCN', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mon',
            fields=[
                ('maMon', models.AutoField(primary_key=True, serialize=False)),
                ('tenMon', models.CharField(max_length=15)),
                ('trangThaiMon', models.IntegerField(default=1)),
                ('hinhAnh', models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='/static/homepage/img'), upload_to='')),
                ('moTa', models.CharField(max_length=50)),
                ('ngayCN', models.DateTimeField(auto_now_add=True)),
                ('maDM', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.danhmuc')),
            ],
        ),
    ]