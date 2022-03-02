from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.contrib.auth.hashers import make_password
from datetime import datetime

# Create your models here.
class MyUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None):

        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, password):

        user = self.create_user(
            email,
            password=password,
            date_of_birth=date_of_birth,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class Usuario(AbstractBaseUser):    
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
    contraseña = models.CharField(max_length=50, verbose_name='Contraseña', null=True)
    imagen = models.CharField(max_length=50, verbose_name='Imagen', null=True)
    celular = models.CharField(max_length=50, verbose_name='Celular', null=True)
    jefe = models.CharField(max_length=50, null=True)

    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth']

    def before_import_row(self,row, **kwargs):
        self.password = row['password']
        row['password'] = make_password(self.password)

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin 

    def __str__(self):
        return self.cedula

    def get_queryset(self):
        pk=self.kwargs['pk']
        if Usuario.objects.filter(id=pk).exists():
            return Usuario.objects.filter(id=pk)

    class Meta:
            verbose_name = 'Usuario'
            verbose_name_plural = 'Usuario' 
            db_table = 'usuario'
            ordering = ['id']
