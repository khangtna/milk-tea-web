# Generated by Django 4.1.6 on 2023-03-10 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_donhang_diachi_donhang_hoten_donhang_quanhuyen_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donhang',
            name='trangThaiDH',
            field=models.CharField(choices=[('0', 'Hủy'), ('1', 'Chưa xác nhận'), ('2', 'Đã xác nhận'), ('3', 'Đang chuẩn bị'), ('4', 'Đang vận chuyển'), ('5', 'Hoàn thành')], default=1, max_length=50),
        ),
    ]
