from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

# Create your models here.

class Usuario(models.Model):    
    nombres = models.CharField(max_length=50, verbose_name='Nombres', null=True)
    apellido_uno = models.CharField(max_length=50, verbose_name='Primer Apellido', null=True)
    apellido_dos = models.CharField(max_length=50, verbose_name='Segundo Apellido', null=True)
    cedula= models.CharField(max_length=50, verbose_name='Cedula', null=True)
    fecha_nacimiento = models.DateField(max_length=150, verbose_name='Fecha de nacimiento', null=True)
    genero = models.CharField(max_length=50, verbose_name='Genero', null=True)
    fecha_Ingreso = models.DateField(max_length=150, verbose_name='Fecha de ingreso', null=True)
    numeroempleado = models.CharField(max_length=50, verbose_name='Numero empleado', null=True)
    cargo = models.CharField(max_length=50, verbose_name='Cargo', null=True)
    zona = models.CharField(max_length=50, verbose_name='Zona', null=True)
    municipio = models.CharField(max_length=50, verbose_name='Municipio', null=True)
    departamento = models.CharField(max_length=50, verbose_name='Departamento', null=True)
    ventas_anteriores = models.CharField(max_length=50, verbose_name='Ventas', null=True)
    email = models.EmailField(max_length=50, verbose_name='Email', null=True)
    contraseña = models.CharField(max_length=50, verbose_name='Contraseña', null=True)
    imagen = models.CharField(max_length=50, verbose_name='Imagen', null=True)
    celular = models.CharField(max_length=50, verbose_name='Celular', null=True)
    jefe = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.cedula

    def subalternos(self):
        subalternos = Usuario.objects.filter(jefe=self.cedula)
        return subalternos

    def get_queryset(self):
        pk=self.kwargs['pk']
        if Usuario.objects.filter(id=pk).exists():
            return Usuario.objects.filter(id=pk)

    class Meta:
            verbose_name = 'Usuario'
            verbose_name_plural = 'Usuario' 
            db_table = 'usuario'
            ordering = ['id']