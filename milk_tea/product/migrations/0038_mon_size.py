# Generated by Django 4.1.6 on 2023-02-26 06:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0037_remove_mon_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='mon',
            name='size',
            field=models.ForeignKey(default=9, on_delete=django.db.models.deletion.CASCADE, to='product.ctgia'),
        ),
    ]