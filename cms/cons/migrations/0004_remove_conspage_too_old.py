# Generated by Django 3.1.6 on 2021-02-08 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cons', '0003_auto_20210208_1127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conspage',
            name='too_old',
        ),
    ]