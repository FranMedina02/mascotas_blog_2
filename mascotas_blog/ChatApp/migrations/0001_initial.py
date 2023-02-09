# Generated by Django 4.1.5 on 2023-02-09 23:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('FeedApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id_chat', models.AutoField(primary_key=True, serialize=False)),
                ('user_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_1', to='FeedApp.user')),
                ('user_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_2', to='FeedApp.user')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id_msg', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now=True)),
                ('seen', models.BooleanField(default=False)),
                ('message', models.TextField()),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ChatApp.chat')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FeedApp.user')),
            ],
        ),
    ]
