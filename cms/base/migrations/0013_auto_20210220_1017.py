# Generated by Django 3.1.6 on 2021-02-20 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_auto_20210220_1004'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='page_url',
            new_name='handhelp_url',
        ),
        migrations.RenameField(
            model_name='author',
            old_name='website_url',
            new_name='outer_url',
        ),
    ]
