from django.shortcuts import render, redirect
from ChatApp.models import Chat, Message
from UserApp.models import CustomUser
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.hashers import make_password
import random
# Create your views here.
@login_required(login_url='/login/')
def conversation(request, conversation:int):
    user = request.user


    chats = Chat.objects.filter(Q(user_1 = user) | Q(user_2 = user))
    msgs = Message.objects.filter(chat__in = chats).filter(chat=conversation).order_by('chat_id','date')
    
    for msg in msgs:
        print('sended') if msg.sender == user else print('recived')

    return render(request, 'ChatApp/single_chat.html', {'chats': chats, 'mensajes': msgs})


@login_required(login_url='/login/')
def all_chats(request):

    user = request.user

    chats = Chat.objects.filter(Q(user_1 = user) | Q(user_2 = user))

    return render(request, 'ChatApp/all_chats.html', {'chats': chats})
