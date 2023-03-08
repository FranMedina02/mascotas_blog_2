from django.contrib import admin
from django.urls import path
import FeedApp.views as views


urlpatterns = [
    path('', views.home, name='Home'),
    path('login/', views.login, name='Log in'),
    path('posts/', views.posts, name='Posts'),
]