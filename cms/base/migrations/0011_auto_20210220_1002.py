# Generated by Django 3.1.6 on 2021-02-20 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_auto_20210220_1000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='website_url',
            field=models.URLField(blank=True, null=True, verbose_name='Страница на стороннем сайте'),
        ),
    ]
