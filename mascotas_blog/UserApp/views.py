from django.shortcuts import render, redirect
from UserApp.forms import UserLoginForm, UserEditForm, UserRegisterForm, UserDeleteForm
from django.contrib.auth import authenticate, login as dj_login, logout as dj_logout
from FeedApp.models import Post
from UserApp.models import CustomUser
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.hashers import check_password

def login(request):
    if request.user.is_authenticated:
        return redirect(next)

    if request.method == 'POST':
        
        form = UserLoginForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            print('valid')
            user = authenticate(request, username=info['username'], password=info['password'])

            if user is not None:
                dj_login(request,user)
                return redirect(request.GET.get('next', '/'))
            else:
                form.add_error(field=None,error='Error en la autenticacion')
                return render(request, 'UserApp/login.html', {'form':form})
    else:
        form = UserLoginForm()
    return render(request, 'UserApp/login.html', {'form':form})

def register(request):
    if request.method == 'POST':
        
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            try:
                CustomUser.objects.get(username=username)
            except CustomUser.DoesNotExist:
                #form.save(request)
                return redirect('Home') 
            else:
                form.add_error(field='username',error='Usuario ya existente')
                return render(request, 'UserApp/register.html', {'form':form})
    else:
        form = UserRegisterForm()

    return render(request, 'UserApp/register.html', {'form':form})

def logout(request):
    dj_logout(request)
    return redirect('Home')

@login_required(login_url='/login/')
def user_settings(request):

    user:CustomUser = request.user

    if request.method == 'POST':
        
        form = UserEditForm(request.POST)

        if form.is_valid():

            info = form.cleaned_data
            print('valid')

            user.username = info['username'] or user.username
            user.email = info['email'] or user.email
            user.first_name = info['first_name'] or user.first_name
            user.last_name = info['last_name'] or user.last_name
            user.description = info['biografia'] or user.description
            user.save()

            return redirect(reverse("Profile"))

    else:
        form = UserEditForm(request.POST)
    
    return render(request, 'UserApp/settings.html', {'edit_form':form})



@login_required(login_url='/login/')
def profile(request, user = None):
    if user is None:
        user:CustomUser = request.user
    else:
        user:CustomUser = CustomUser.objects.get(id=user)

    user_posts = Post.objects.filter(id_user=user)
    n_posts = len(user_posts)



    return render(request, 'UserApp/profile.html',
                  context = {'posts':user_posts,'n_posts':n_posts, 'profile':user})

@login_required(login_url='/login/')
def delete(request):

    user:CustomUser = request.user

    if request.method == 'POST':

        form = UserDeleteForm(request.POST)

        if form.is_valid():
            info = form.cleaned_data
            
            if not check_password(info['password'], user.password):
                form.add_error(field='password', error='Contraseña incorrecta')
            else:
                user.delete()
                return redirect('Home')
        
        return render(request, 'UserApp/delete.html', {'delete_form':form})


    else:
        form = UserDeleteForm()
    
    return render(request, 'UserApp/delete.html', {'delete_form':form})
    


