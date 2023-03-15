from django.contrib import admin
from django.urls import path
import FeedApp.views as views


urlpatterns = [
    path('', views.home, name='Home'),
    path('posts/', views.posts, name='Posts'),
    path('posts/<id_post>', views.single_post, name='Single Post'),
]