# Generated by Django 4.1.6 on 2023-03-04 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0006_remove_ctgiohang_ctgia_ctgiohang_giamon'),
    ]

    operations = [
        migrations.AddField(
            model_name='ctgiohang',
            name='size',
            field=models.CharField(blank=True, max_length=2),
        ),
    ]
