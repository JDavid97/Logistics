from pyexpat import model
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from erp.models import Usuario
from .serializer import UserSerializer
from erp.services import is_show_jefe

# Create your views here.

class UsuarioView(View):
    def get(self, request, *args, **kwargs):
        if 'cedula_empleado' in kwargs:
            cedula_empleado: int = kwargs['cedula_empleado']
        else:
            cedula_empleado = request.user.cedula

        context ={}

        context["usuario"] = Usuario.objects.get(cedula=cedula_empleado)
        if context["usuario"].jefe:
            context["jefe"] = Usuario.objects.get(cedula=context["usuario"].jefe)
            context["mostrarjefe"] = is_show_jefe(request.user, context["jefe"])
        context["subalternos"] = Usuario.objects.filter(jefe=cedula_empleado)
            

        return render(request, "../templates/usuario/perfil.html", context)

