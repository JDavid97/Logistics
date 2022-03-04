from pyexpat import model
from tokenize import Double
from django.shortcuts import render
from django.views import View
from erp.models import Usuario
from erp.services import is_show_jefe, is_permission
from erp.services import get_total_sales

# Create your views here.

#Se mandan datos del usuario logueado como sus datos, su jefe y sus subalternos
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
        # context["subalternos"] = Usuario.objects.filter(jefe=usuario.numeroempleado)
        subalternos = Usuario.objects.filter(jefe=usuario.numeroempleado)


        
        ventas_subalternos = 0   
        for c in subalternos:

                total_subalterno = int(get_total_sales(c.numeroempleado))
                c.total_ventas = total_subalterno
                ventas_subalternos += total_subalterno

        context["subalternos"] = subalternos
        context["ventas_subalternos"] = ventas_subalternos

        return render(request, "../templates/usuario/perfil.html", context)


