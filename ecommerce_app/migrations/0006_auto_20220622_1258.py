# Generated by Django 3.2.6 on 2022-06-22 07:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_app', '0005_auto_20220622_1246'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='address1',
            new_name='address',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='address2',
        ),
    ]
