# Generated by Django 4.1.6 on 2023-02-26 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0038_mon_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mon',
            name='size',
        ),
        migrations.AddField(
            model_name='mon',
            name='size',
            field=models.ManyToManyField(to='product.ctgia'),
        ),
    ]
