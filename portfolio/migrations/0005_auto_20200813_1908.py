# Generated by Django 3.0.8 on 2020-08-13 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_auto_20200813_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='event',
            name='url',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='resources',
            name='description',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='resources',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='resources',
            name='url',
            field=models.TextField(max_length=1000),
        ),
    ]
