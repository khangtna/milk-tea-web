# Generated by Django 4.1.6 on 2023-03-11 04:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
        ('product', '0046_remove_ctgia_madm'),
    ]

    operations = [
        migrations.CreateModel(
            name='CTDanhGia',
            fields=[
                ('idDanhGia', models.AutoField(primary_key=True, serialize=False)),
                ('rating', models.FloatField(default=0)),
                ('ngayDanhGia', models.DateTimeField(auto_now_add=True)),
                ('nhanXet', models.TextField(max_length=1000)),
                ('hinhAnh', models.ImageField(blank=True, default=None, upload_to='img')),
                ('maKH', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.khachhang')),
                ('maMon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.mon')),
            ],
        ),
    ]
