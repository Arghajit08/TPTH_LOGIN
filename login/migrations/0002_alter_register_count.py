# Generated by Django 4.1 on 2022-09-01 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]
