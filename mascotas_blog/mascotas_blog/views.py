from django.http import HttpResponse 
from django.template import loader

def home(request):

    data = {}

    plantilla = loader.get_template('home.html')
    document = plantilla.render(data)

    return HttpResponse(document)

def login(request):

    data = {}

    plantilla = loader.get_template('login.html')
    document = plantilla.render(data)

    return HttpResponse(document)
