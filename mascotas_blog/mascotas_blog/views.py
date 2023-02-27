from django.http import HttpResponse 
from django.shortcuts import render

def home(request):

    context = {}

    template = 'home.html'

    return render(request, template, context)

def login(request):

    context = {}

    template = 'login.html'

    return render(request, template, context)
