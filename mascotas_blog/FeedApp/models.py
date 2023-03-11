from django.db import models
from time import time
from uuid import uuid4
import os

# Create your models here.
class User(models.Model):
    id_user = models.AutoField(primary_key=True)
    mail = models.EmailField(unique=True)
    username = models.CharField(max_length=40, unique=True)
    password = models.CharField(max_length=16)
    description = models.CharField(max_length=255)

def path_and_rename(instance, filename : str):
    upload_to = 'post_imgs'
    ext = filename.split('.')[-1]
    if instance.id_user:
        name = (str(instance.id_user) + '_' + str(int(time())))
        filename = f'{name}.{ext}'
    else:
        filename = f'{uuid4().hex}.{ext}'
    return os.path.join(upload_to, filename)

class Post(models.Model):
    id_post = models.AutoField(primary_key=True)
    title = models.CharField(max_length=25)
    subtitle = models.CharField(max_length=35)
    description = models.TextField(max_length=255)
    id_user = models.ForeignKey(User, models.CASCADE)
    id_img = models.ImageField(upload_to=path_and_rename,
                                max_length=255, null=True, blank=True)

    def __str__(self) -> str:
        return str((self.id_post, self.id_img))

    