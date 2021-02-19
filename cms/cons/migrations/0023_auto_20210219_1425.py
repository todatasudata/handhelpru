# Generated by Django 3.1.6 on 2021-02-19 14:25

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.contrib.taggit
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0060_auto_20210219_0933'),
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('cons', '0022_auto_20210219_0933'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
            ],
            options={
                'verbose_name': 'Частые вопросы Главная',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AlterModelOptions(
            name='faqpage',
            options={'verbose_name': 'Частый вопрос'},
        ),
        migrations.AddField(
            model_name='faqpage',
            name='number',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='faqpage',
            name='tags',
            field=modelcluster.contrib.taggit.ClusterTaggableManager(blank=True, help_text='A comma-separated list of tags.', through='cons.ConsPageTag', to='taggit.Tag', verbose_name='Теги'),
        ),
        migrations.CreateModel(
            name='FAQPageTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_object', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='tagged_items', to='cons.faqpage')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cons_faqpagetag_items', to='taggit.tag')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]