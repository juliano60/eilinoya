# Generated by Django 5.0.1 on 2024-02-11 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wine',
            name='preparation',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='wine',
            name='slogan',
            field=models.CharField(default='', max_length=200),
        ),
    ]