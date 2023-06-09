# Generated by Django 3.2.5 on 2023-03-15 00:05

import common.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='users',
            options={'verbose_name': 'user', 'verbose_name_plural': 'user'},
        ),
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.CharField(default='', max_length=50, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='users',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='users',
            name='idcard',
            field=models.CharField(default='', max_length=50, verbose_name='idcard'),
        ),
        migrations.AlterField(
            model_name='users',
            name='mobile',
            field=models.CharField(default='', max_length=50, verbose_name='mobile'),
        ),
        migrations.AlterField(
            model_name='users',
            name='name',
            field=models.CharField(default='', max_length=50, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='users',
            name='password',
            field=models.CharField(default='', max_length=128, verbose_name='password'),
        ),
        migrations.AlterField(
            model_name='users',
            name='photo',
            field=common.models.MyImageField(default='', max_length=255, verbose_name='photo'),
        ),
        migrations.AlterField(
            model_name='users',
            name='sex',
            field=models.CharField(choices=[('男', '男'), ('女', '女')], default='', max_length=512, verbose_name='sex'),
        ),
        migrations.AlterField(
            model_name='users',
            name='username',
            field=models.CharField(default='', max_length=50, verbose_name='username'),
        ),
    ]
