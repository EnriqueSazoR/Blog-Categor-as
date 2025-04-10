from django.shortcuts import render
from blog.models import Publicacion

# Create your views here.

# Listar las publicaciones
def post_list(request):
    listaPublicacion = Publicacion.objects.all().order_by('-fecha_creacion')
    contexto = {'listPublicaciones':listaPublicacion}
    return render(request, 'blog/post_list.html', contexto)


# Obtener publicacion por ID
def  get_publicacion(request, id):
    publicacion = Publicacion.objects.get(id=id)
    return render(request, 'blog/get_publicacion.html', {'publicacion':publicacion})


    