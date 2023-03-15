from django.urls import path
import FeedApp.views as views


urlpatterns = [
    path('', views.posts, name='Home'),
    #path('posts/', views.posts, name='Posts'),
    path('posts/<id_post>', views.single_post, name='Single Post'),
    path('crearPost', views.postFormulario, name='Crear Post'),
    path('search/<data>', views.search, name='Search'),
    path('search', views.search, name='Search'),
]