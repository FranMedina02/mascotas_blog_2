# Generated by Django 4.1.5 on 2023-03-05 15:47

import FeedApp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FeedApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id_img',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to=FeedApp.models.path_and_rename),
        ),
    ]
