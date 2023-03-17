from django.db import models

# Create your models here.

class User(models.Model):
    id_user = models.AutoField(primary_key=True)
    mail = models.EmailField(unique=True)
    username = models.CharField(max_length=40, unique=True)
    password = models.CharField(max_length=16)
    description = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.id_user}_{self.username}'