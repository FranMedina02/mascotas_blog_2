from django.http import HttpResponse 
from django.template import loader

def home(request):
    plantilla = loader.get_template('index.html')
    document = plantilla.render()

    return HttpResponse(document)