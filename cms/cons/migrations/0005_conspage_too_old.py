# Generated by Django 3.1.6 on 2021-02-08 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cons', '0004_remove_conspage_too_old'),
    ]

    operations = [
        migrations.AddField(
            model_name='conspage',
            name='too_old',
            field=models.BooleanField(default=False, verbose_name='Устарела'),
        ),
    ]
