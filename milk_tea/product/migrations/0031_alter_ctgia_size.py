# Generated by Django 4.1.6 on 2023-02-25 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0030_remove_ctgia_mamon_ctgia_madm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ctgia',
            name='size',
            field=models.CharField(choices=[('M', 'M'), ('L', 'L')], max_length=2),
        ),
    ]
