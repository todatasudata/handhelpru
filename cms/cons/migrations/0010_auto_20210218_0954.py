# Generated by Django 3.1.6 on 2021-02-18 09:54

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_auto_20210217_1058'),
        ('cons', '0009_authorsorderable'),
    ]

    operations = [
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='base.author')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='authors', to='cons.conspage')),
            ],
        ),
        migrations.DeleteModel(
            name='AuthorsOrderable',
        ),
    ]
