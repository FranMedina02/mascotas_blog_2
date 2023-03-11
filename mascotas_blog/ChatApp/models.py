from django.db import models
from UserApp.models import User

# Create your models here.
class Chat(models.Model):
    id_chat = models.AutoField(primary_key=True)
    user_1 = models.ForeignKey(User, on_delete= models.CASCADE, related_name='user_1')
    user_2 = models.ForeignKey(User, on_delete= models.CASCADE, related_name='user_2')

class Message(models.Model):
    id_msg = models.AutoField(primary_key=True)
    date = models.DateTimeField(auto_now=True, editable=False)
    sender = models.ForeignKey(User, on_delete= models.CASCADE)
    chat = models.ForeignKey(Chat, on_delete= models.CASCADE)
    seen = models.BooleanField(default=False)
    message = models.TextField()