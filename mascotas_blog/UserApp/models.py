from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    description = models.CharField(max_length=255)

    def __str__(self):
        return f'id: {self.id_user} - username: {self.username}'