# Generated by Django 4.1.6 on 2023-03-07 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_thanhtoan_donhang_matt'),
    ]

    operations = [
        migrations.AddField(
            model_name='donhang',
            name='diachi',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='donhang',
            name='hoten',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='donhang',
            name='quanhuyen',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='donhang',
            name='sdt',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='donhang',
            name='tinhtp',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='donhang',
            name='xaphuong',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
