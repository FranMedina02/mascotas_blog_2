# Generated by Django 4.1.5 on 2023-04-09 15:18

import UserApp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0002_customuser_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to=UserApp.models.path_and_rename),
        ),
    ]
