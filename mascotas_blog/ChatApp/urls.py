from django.urls import path
import ChatApp.views as views

urlpatterns = [
    path('Chats', views.all_chats, name='All Chats'),
    path('Chats/<conversation>', views.conversation, name='Single Chat'),
    
]