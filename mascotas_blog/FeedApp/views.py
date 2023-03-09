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

def posts(request, id_post=None):

    posts = Post.objects.all()
    template = 'FeedApp/post.html'
    context = {'posts':posts}

    return render(request, template, context)


def single_post(request, id_post):
    
    post = Post.objects.get(id_post=id_post)
    template = 'FeedApp/single_post.html'
    context = {'post':post}

    return render(request, template, context)