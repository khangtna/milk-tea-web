# Generated by Django 4.1.6 on 2023-02-22 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_ctdonhang_donhang_remove_giohang_makh_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donhang',
            name='trangThaiMon',
        ),
        migrations.AddField(
            model_name='donhang',
            name='trangThaiDH',
            field=models.CharField(choices=[(0, 'Chưa xác nhận'), (1, 'Đã xác nhận'), (2, 'Đang vận chuyển'), (3, 'Hoàn thành')], default=0, max_length=50),
        ),
    ]
