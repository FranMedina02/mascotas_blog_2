# Generated by Django 4.1.5 on 2023-03-11 21:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0001_initial'),
        ('ChatApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='user_1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_1', to='UserApp.user'),
        ),
        migrations.AlterField(
            model_name='chat',
            name='user_2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_2', to='UserApp.user'),
        ),
        migrations.AlterField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserApp.user'),
        ),
    ]
