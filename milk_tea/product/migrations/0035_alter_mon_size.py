# Generated by Django 4.1.6 on 2023-02-26 06:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0034_alter_mon_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mon',
            name='size',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='product.ctgia'),
        ),
    ]