from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
class Marca (models.Model):
    nombre = models.TextField(max_length=100)
    activo = models.BooleanField()

    def str(self):
        return self.nombre

opciones_consultas = [

    [0, "consulta"],
    [1,"reclamo"],
    [2,"sugerencia"],
    [3,"felicitaciones"]
]


class contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField()
    avisos = models.BooleanField()

    def str(self):
        return self.nombre

class Producto (models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()
    codigo = models.IntegerField()
    marca = models.CharField(max_length=30)
    fecha_vencimiento = models.DateField()


    def __str__(self):
        return self.nombre