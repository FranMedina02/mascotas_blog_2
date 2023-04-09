from django.shortcuts import render, redirect
from ChatApp.models import Chat, Message
from UserApp.models import CustomUser
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import Http404

# Create your views here.
@login_required(login_url='/login/')
def conversation(request, conversation:int):
    
    conversation = int(conversation)
    user :CustomUser = request.user
    chats = Chat.objects.filter(Q(user_1 = user) | Q(user_2 = user))
    chat = Chat.objects.get(id_chat = conversation)
    
    if not chat in chats:
        raise Http404('La conversacion no le pertenece al usuario')

    if request.method == 'POST':
        if request.POST['message']:
            Message.objects.create(sender = user, chat = chat,
                                   message = request.POST['message'])

    
    msgs = Message.objects.filter(chat = chat).filter(chat=conversation).order_by('chat_id','date')

    print(type(conversation),type(chat.id_chat))

    return render(request, 'ChatApp/single_chat.html', {'chats': chats, 'mensajes': msgs, 'conv': conversation})


@login_required(login_url='/login/')
def all_chats(request):

    user = request.user

    chats = Chat.objects.filter(Q(user_1 = user) | Q(user_2 = user))

    return render(request, 'ChatApp/all_chats.html', {'chats': chats})
