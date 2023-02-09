from django.db import models
from FeedApp.models import User

# Create your models here.
class Chat(models.Model):
    id_chat = models.AutoField(primary_key=True)
    user_1 = models.ForeignKey(User,)
    user_2 = models.ForeignKey(User,)

class Message(models.Model):
    id_msg = models.AutoField(primary_key=True)
    date = models.DateTimeField(auto_now=True, editable=False)
    sender = models.ForeignKey(User, )
    chat = models.ForeignKey(Chat, )
    seen = models.BooleanField(default=False)
    message = models.TextField()