# Generated by Django 4.1.6 on 2023-02-26 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0043_rename_sizemon_mon_sizes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mon',
            old_name='sizes',
            new_name='sizeMon',
        ),
    ]