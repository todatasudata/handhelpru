# Generated by Django 3.1.6 on 2021-02-05 13:10

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20210205_1306'),
    ]

    operations = [
        migrations.AddField(
            model_name='newspage',
            name='content',
            field=wagtail.core.fields.StreamField([('date', wagtail.core.blocks.DateBlock()), ('text', wagtail.core.blocks.RichTextBlock())], null=True),
        ),
    ]
