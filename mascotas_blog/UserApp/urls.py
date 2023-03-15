from django.urls import path
import UserApp.views as views


urlpatterns = [
    path('login/', views.login, name='Log in'),
]
