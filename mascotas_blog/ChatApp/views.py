from django.shortcuts import render, redirect
from ChatApp.models import Chat, Message
from UserApp.models import CustomUser
from django.contrib.auth.decorators import login_required



# Create your views here.
def conversation(request, conversation:int):
    context = {}
    return render(request, 'ChatApp/single_chat.html', context)
def all_chats(request):
    context = {}
    return render(request, 'ChatApp/all_chats.html', context)
