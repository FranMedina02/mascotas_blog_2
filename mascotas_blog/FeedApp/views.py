# Create your views here.
from django.shortcuts import render, redirect
from FeedApp.models import Post
from FeedApp.forms import PostFormulario
from UserApp.models import CustomUser
from django.contrib.auth.decorators import login_required


def posts(request):
    
    posts = Post.objects.all().order_by('-id_post')
    template = 'FeedApp/post.html'
    context = {'posts':posts}

    return render(request, template, context)


def single_post(request, id_post):
    
    post = Post.objects.get(id_post=id_post)
    template = 'FeedApp/single_post.html'
    context = {'post':post}

    return render(request, template, context)

@login_required(login_url='/login/')
def postFormulario(request):

    if request.method == 'POST':
        
        form = PostFormulario(request.POST, request.FILES)
        print(form)
        if form.is_valid():

            info = form.cleaned_data
            print(info)
            post = Post(title = info['title'],
                        subtitle = info['subtitle'],
                        description = info['desc'],
                        id_user = request.user,
                        id_img = info['id_img'])
            post.save()

            return redirect('Home')
    
    else:
        form = PostFormulario()

    return render(request, 'FeedApp/postFormulario.html', {'form':form})

def search(request):
    
    username = request.GET['username']
    users = CustomUser.objects.filter(username__icontains=username)

    return render(request, 'FeedApp/search_results.html', {'results':users})
