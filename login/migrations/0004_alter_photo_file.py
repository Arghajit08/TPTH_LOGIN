# Generated by Django 4.1 on 2022-09-01 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='file',
            field=models.FileField(upload_to='file'),
        ),
    ]
