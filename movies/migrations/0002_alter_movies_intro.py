# Generated by Django 3.2.5 on 2023-03-15 02:43

import common.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='intro',
            field=common.models.UMeditorField(default='', max_length=4096, verbose_name='intro'),
        ),
    ]
