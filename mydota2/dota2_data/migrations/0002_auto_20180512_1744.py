# Generated by Django 2.0.2 on 2018-05-12 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dota2_data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='heros',
            name='img',
            field=models.ImageField(upload_to='dota2_data/img'),
        ),
        migrations.AlterField(
            model_name='items',
            name='logo',
            field=models.ImageField(upload_to='dota2_data/img'),
        ),
        migrations.AlterField(
            model_name='skills',
            name='logo',
            field=models.ImageField(upload_to='dota2_data/img'),
        ),
    ]