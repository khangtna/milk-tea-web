# Generated by Django 4.1.6 on 2023-02-18 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_mon_trangthaimon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mon',
            name='moTa',
            field=models.CharField(max_length=500),
        ),
    ]
