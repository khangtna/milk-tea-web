# Generated by Django 4.1.6 on 2023-03-05 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_khuyenmai_alter_donhang_trangthaidh'),
    ]

    operations = [
        migrations.AlterField(
            model_name='khuyenmai',
            name='ngayHetHan',
            field=models.DateField(),
        ),
    ]
