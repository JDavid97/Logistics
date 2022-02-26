from pyexpat import model
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from erp.models import Usuario
from .serializer import UserSerializer

# Create your views here.

class UsuarioView(View):
    def get(self, request, *args, **kwargs):
        if 'cedula_empleado' in kwargs:
            cedula_empleado: int = kwargs['cedula_empleado']
        else:
            cedula_empleado = 345345

        context ={}
        context["usuario"] = Usuario.objects.get(cedula=cedula_empleado)
        return render(request, "../templates/usuario/perfil.html", context)

