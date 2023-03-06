# Generated by Django 4.1.6 on 2023-02-21 13:53

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
            name='GioHang',
            fields=[
                ('maGH', models.AutoField(primary_key=True, serialize=False)),
                ('maKH', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.khachhang')),
            ],
        ),
        migrations.CreateModel(
            name='CTGioHang',
            fields=[
                ('maCTGH', models.AutoField(primary_key=True, serialize=False)),
                ('maGH', models.CharField(max_length=15)),
                ('soLuong', models.IntegerField(default=1)),
                ('maMon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.mon')),
            ],
        ),
    ]