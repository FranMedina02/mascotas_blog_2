# Create your views here.
from django.shortcuts import render
from FeedApp.models import Post
from FeedApp.forms import PostFormulario

def home(request):

    context = {}

    template = 'mascotas_blog/home.html'

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

def postFormulario(request):

    if request.method == 'POST':

        form = PostFormulario(request.POST)

        if form.is_valid():

            info = form.cleaned_data
            post = Post(title = info['title'],
                        subtitle = info['subtitle'],
                        description = info['desc'],
                        id_img = info['img'])
            post.save()

        return render(request, 'FeedApp/post.html')
    
    else:
        form = PostFormulario()

    return render(request, 'postFormulario.html', {'form':form})

def search(request, data):
    pass
