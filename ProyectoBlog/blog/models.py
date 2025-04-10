from django.db import models

# Create your models here.

# Modelo Categoría
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre


# Modelo Publicaciones
class Publicacion(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.TextField()
    Categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.titulo
    
