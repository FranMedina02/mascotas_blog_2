from django.db import models
from UserApp.models import CustomUser
from time import time
from uuid import uuid4
import os

# Create your models here.


def path_and_rename(instance, filename : str):
    upload_to = 'post_imgs'
    ext = filename.split('.')[-1]
    if instance.pk:
        name = (str(instance.pk) + '_' + str(int(time())))
        filename = f'{name}.{ext}'
    else:
        filename = f'{uuid4().hex}.{ext}'
    return os.path.join(upload_to, filename)

class Post(models.Model):
    id_post = models.AutoField(primary_key=True)
    title = models.CharField(max_length=25)
    subtitle = models.CharField(max_length=35)
    description = models.TextField(max_length=255)
    id_user = models.ForeignKey(CustomUser, on_delete= models.CASCADE)
    id_img = models.ImageField(upload_to=path_and_rename,
                                max_length=255, null=True, blank=True)

    def __str__(self) -> str:
        return f'id: {self.id_post} - title: {self.title} - img: {self.id_img}'

    