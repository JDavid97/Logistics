from pyexpat import model
from tokenize import Double
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from erp.models import Usuario
from .serializer import UserSerializer
from erp.services import is_show_jefe, is_permission

# Create your views here.

class UsuarioView(View):    
    def get(self, request, *args, **kwargs):
        if 'cedula_empleado' in kwargs:
            cedula_empleado: int = kwargs['cedula_empleado']
            usuario = Usuario.objects.get(numeroempleado=cedula_empleado)

        else:
            usuario = request.user

        context ={}

        context["usuario"] = usuario
        if context["usuario"].jefe:
            context["jefe"] = Usuario.objects.get(numeroempleado=usuario.jefe)
            context["mostrarjefe"] = is_show_jefe(request.user, context["jefe"])
        context["subalternos"] = Usuario.objects.filter(jefe=usuario.numeroempleado)
        
        ventas_subalternos = 0
    
        for c in context["subalternos"]:
            if c.ventas_anteriores:
                ventas_subalternos += int(c.ventas_anteriores)            

        print(ventas_subalternos)
        context["ventas_subalternos"] = ventas_subalternos

        return render(request, "../templates/usuario/perfil.html", context)

