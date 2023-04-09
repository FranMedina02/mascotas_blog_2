from django.db import models
from django.contrib.auth.models import AbstractUser
from time import time
from uuid import uuid4
import os


def path_and_rename(instance, filename : str):
    upload_to = 'avatar'
    ext = filename.split('.')[-1]
    if instance.pk:
        name = (str(instance.pk) + '_' + str(int(time())))
        filename = f'{name}.{ext}'
    else:
        filename = f'{uuid4().hex}.{ext}'
    return os.path.join(upload_to, filename)

class CustomUser(AbstractUser):
    description = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to= path_and_rename,
                                max_length=255, null=True, blank=True)

    def __str__(self):
        return f'{self.pk}_{self.username}'

