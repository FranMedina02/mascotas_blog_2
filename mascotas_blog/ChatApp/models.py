from django.db import models
from UserApp.models import CustomUser

# Create your models here.
class Chat(models.Model):
    id_chat = models.AutoField(primary_key=True)
    user_1 = models.ForeignKey(CustomUser, on_delete= models.CASCADE, related_name='user_1')
    user_2 = models.ForeignKey(CustomUser, on_delete= models.CASCADE, related_name='user_2')
    last_msg = models.ForeignKey('Message',on_delete= models.DO_NOTHING, related_name='last_msg', null=True)


class Message(models.Model):
    id_msg = models.AutoField(primary_key=True)
    date = models.DateTimeField(auto_now=True, editable=False)
    sender = models.ForeignKey(CustomUser, on_delete= models.CASCADE)
    chat = models.ForeignKey(Chat, on_delete= models.CASCADE)
    seen = models.BooleanField(default=False)
    message = models.TextField()