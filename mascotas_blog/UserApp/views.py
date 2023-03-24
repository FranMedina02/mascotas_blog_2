from django.shortcuts import render, redirect
from UserApp.forms import UserFormulario
from django.contrib.auth import authenticate, login as dj_login, logout as dj_logout
from FeedApp.models import Post
from django.contrib.auth.decorators import login_required


def login(request):
    if request.user.is_authenticated:
        return redirect(next)

    if request.method == 'POST':
        
        form = UserFormulario(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            print('valid')
            user = authenticate(request, username=info['username'], password=info['password'])

            if user is not None:
                print('authenticated')
                dj_login(request,user)
                return redirect(request.GET.get('next', '/'))
            else:
                print('not authenticated')
                form.add_error(field=None,error='Error en la autenticcion')
                return render(request, 'UserApp/login.html', {'form':form})
    else:
        form = UserFormulario()
    return render(request, 'UserApp/login.html', {'form':form})

        

def logout(request):
    dj_logout(request)
    return redirect('Home')

@login_required(login_url='/login/')
def user_settings(request):
    return redirect('Home')

@login_required(login_url='/login/')
def profile(request, user = None):
    if user is None:
        user = request.user

    user_posts = Post.objects.filter(id_user=user)
    n_posts = len(user_posts)

    print(n_posts)

    return render(request, 'UserApp/profile.html',
                  context = {'posts':user_posts,'n_posts':n_posts})
    

    


