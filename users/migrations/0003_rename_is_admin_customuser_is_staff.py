# Generated by Django 3.2.9 on 2022-01-27 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20220127_1319'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='is_admin',
            new_name='is_staff',
        ),
    ]
