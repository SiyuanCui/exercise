# Generated by Django 3.2.5 on 2023-03-18 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_alter_movies_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movies',
            name='colum',
        ),
        migrations.AddField(
            model_name='movies',
            name='column',
            field=models.IntegerField(db_column='column', default=1),
        ),
    ]
