# Generated by Django 3.1.6 on 2021-02-18 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_auto_20210217_1058'),
        ('cons', '0011_auto_20210218_0955'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Author',
            new_name='ConsAuthor',
        ),
    ]
