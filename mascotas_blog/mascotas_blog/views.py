from django.shortcuts import render


def aboutUs(request):
    return render(request, 'mascotas_blog/about_us.html', {})