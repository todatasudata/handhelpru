# Generated by Django 3.1.6 on 2021-02-03 13:17

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0059_apply_collection_ordering'),
    ]

    operations = [
        migrations.CreateModel(
            name='GuidelinePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('content', wagtail.core.fields.RichTextField(verbose_name='Содержание')),
            ],
            options={
                'verbose_name': 'Памятка',
                'verbose_name_plural': 'Памятки',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='GuidelinesIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
            ],
            options={
                'verbose_name': 'Страница всех памяток',
            },
            bases=('wagtailcore.page',),
        ),
    ]
