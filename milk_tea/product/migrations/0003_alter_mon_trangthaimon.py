# Generated by Django 4.1.6 on 2023-02-18 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_mon_tenmon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mon',
            name='trangThaiMon',
            field=models.BooleanField(default=True),
        ),
    ]
