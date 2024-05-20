# Generated by Django 5.0.6 on 2024-05-20 09:52

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='categories',
            field=models.CharField(choices=[('python', 'python'), ('django', 'django'), ('javascript', 'javascript')], default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
