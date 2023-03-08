# Create your views here.
from django.shortcuts import render
from FeedApp.models import Post

def home(request):

    context = {}

    template = 'FeedApp/home.html'

    return render(request, template, context)

def login(request):

    context = {'texto': 'Este es el login'}

    template = 'FeedApp/login.html'

    return render(request, template, context)

def posts(request):

    posts = Post.objects.all()
    

    context = {'posts':posts}

    template = 'FeedApp/post.html'

    return render(request, template, context)