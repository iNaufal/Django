# Generated by Django 5.0.6 on 2024-05-27 14:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_publications_reader_tag_alter_article_fill_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='publications',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.publications'),
        ),
    ]
