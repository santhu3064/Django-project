# Generated by Django 3.0.8 on 2020-07-27 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='topic_name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='webpage',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]