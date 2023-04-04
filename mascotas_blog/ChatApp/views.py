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
    context = {}

    
    return render(request, 'ChatApp/single_chat.html', context)


@login_required(login_url='/login/')
def all_chats(request):

    user = request.user


    chats = Chat.objects.filter(Q(user_1 = user) | Q(user_2 = user))
    msgs = Message.objects.filter(chat__in = chats).order_by('chat_id','date')


    return render(request, 'ChatApp/all_chats.html', {'chats': chats, 'mensajes':msgs})
