from django.shortcuts import render

# Create your views here.
def login(request):

    context = {'texto': 'Este es el login'}

    template = 'UserApp/login.html'

    return render(request, template, context)

def logout(request):
    pass
def user_settings(request):
    pass
def profile(request):
    pass
