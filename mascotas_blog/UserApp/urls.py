from django.urls import path
import UserApp.views as views


urlpatterns = [
    path('login/', views.login, name='Log in'),
    path('logout/', views.logout, name='Log Out'),
    path('profile/', views.profile, name='Profile'),
    path('profile/<user>', views.profile, name='Owner'),
    path('settings/', views.user_settings, name='User Settings'),
]
