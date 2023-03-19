from django.shortcuts import render, redirect
from UserApp.forms import UserFormulario
from django.contrib.auth import authenticate, login as dj_login, logout as dj_logout
from FeedApp.models import Post

# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect('Home')

    if request.method == 'POST':
        
        form = UserFormulario(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            print('valid')
            user = authenticate(request, username=info['username'], password=info['password'])

            if user is not None:
                print('authenticated')
                dj_login(request,user)
                return redirect('Home')
            else:
                print('not authenticated')
                form.add_error(field=None,error='Invalid authentication')
                return render(request, 'UserApp/login.html', {'form':form})
    else:
        form = UserFormulario()
    return render(request, 'UserApp/login.html', {'form':form})

        

    
def logout(request):
    dj_logout(request)
    return redirect('Home')

def user_settings(request):
    pass

def profile(request):
    if request.user.is_authenticated:
        curr_user = request.user
        context = {}

        user_posts = Post.objects.filter(id_user=curr_user)
        n_posts = len(user_posts)

        return render(request, 'UserApp/login.html', {'posts':user_posts,'n_post':n_posts})
    
    return redirect('Log in')
    


