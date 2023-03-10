# Generated by Django 4.1.6 on 2023-02-25 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0028_alter_ctgia_size'),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DonHang',
            fields=[
                ('maDH', models.AutoField(primary_key=True, serialize=False)),
                ('tongTien', models.DecimalField(decimal_places=3, default=0, max_digits=9)),
                ('ngayLap', models.DateTimeField(auto_now_add=True)),
                ('trangThaiDH', models.CharField(choices=[('0', 'Chưa xác nhận'), ('1', 'Đã xác nhận'), ('2', 'Đang vận chuyển'), ('3', 'Hoàn thành')], default=0, max_length=50)),
                ('maKH', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.khachhang')),
            ],
        ),
        migrations.CreateModel(
            name='CTDonHang',
            fields=[
                ('maCTDH', models.AutoField(primary_key=True, serialize=False)),
                ('giaMon', models.DecimalField(decimal_places=3, default=0, max_digits=9)),
                ('soLuong', models.IntegerField(default=1)),
                ('maDH', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.donhang')),
                ('maMon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.mon')),
            ],
        ),
    ]
