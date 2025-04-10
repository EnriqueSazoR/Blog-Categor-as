from blog.views import post_list, get_publicacion
from django.urls import path

urlpatterns = [
    path('', post_list, name='lista-publicaciones'),
    path('publicacion/<int:id>', get_publicacion, name="publicacion")
]