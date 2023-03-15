from django.shortcuts import render

# Create your views here.
def login(request):

    context = {'texto': 'Este es el login'}

    template = 'UserApp/login.html'

    return render(request, template, context)
