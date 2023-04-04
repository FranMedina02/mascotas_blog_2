from django.shortcuts import render, redirect
from ChatApp.models import Chat, Message
from UserApp.models import CustomUser
from django.contrib.auth.decorators import login_required
from django.db.models import Q


# Create your views here.
@login_required(login_url='/login/')
def conversation(request, conversation:int):
    context = {}

    
    return render(request, 'ChatApp/single_chat.html', context)


@login_required(login_url='/login/')
def all_chats(request):
    user = request.user
    context = {}

    genericUser = CustomUser.objects.get(id = 9)

    chat1 = Chat(user_1 = user, user_2 = genericUser)
    chat1.save()
    chat2 = Chat(user_1 = genericUser, user_2 = user)
    chat2.save()


    chats = Chat.objects.filter(Q(user_1 = user) | Q(user_2 = user))
    print(chats)

    return render(request, 'ChatApp/all_chats.html', context)
