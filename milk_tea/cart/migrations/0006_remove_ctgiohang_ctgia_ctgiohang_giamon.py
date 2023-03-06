# Generated by Django 4.1.6 on 2023-02-25 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_ctgiohang_giohang_remove_donhang_makh_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ctgiohang',
            name='ctGia',
        ),
        migrations.AddField(
            model_name='ctgiohang',
            name='giaMon',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=9),
        ),
    ]