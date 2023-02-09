from django.db import models

# Create your models here.
class User(models.Model):
    id_user = models.AutoField(primary_key=True)
    mail = models.EmailField(unique=True)
    username = models.CharField(max_length=40, unique=True)
    password = models.CharField(max_length=16)
    description = models.CharField(max_length=255)

class Post(models.Model):

    id_img = models.ImageField(primary_key=True,upload_to='post_imgs', null=True)

    title = models.CharField(max_length=25)
    subtitle = models.CharField(max_length=35)
    description = models.TextField(max_length=255)
    id_user = models.ForeignKey(User, models.CASCADE)

    