# Generated by Django 4.1.6 on 2023-02-18 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mon',
            name='tenMon',
            field=models.CharField(max_length=50),
        ),
    ]
