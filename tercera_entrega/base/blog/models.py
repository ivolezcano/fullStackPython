from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

class Entrada(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

class Comentario(models.Model):
    entrada = models.ForeignKey(Entrada, on_delete=models.CASCADE)
    texto = models.TextField()
    fecha_comentario = models.DateTimeField(auto_now_add=True)