from django.http import HttpResponse 
from django.shortcuts import render
from FeedApp.models import Post

def home(request):

    context = {}

    template = 'home.html'

    return render(request, template, context)

def login(request):

    context = {'texto': 'Este es el login'}

    template = 'login.html'

    return render(request, template, context)

def posts(request):

    posts = Post.objects.all()
    

    context = {'posts':posts}

    template = 'post.html'

    return render(request, template, context)


