from unicodedata import name
from django.urls import path
from erp.views import UsuarioView

app_name = 'erp'

urlpatterns = [
    path('<cedula_empleado>', UsuarioView.as_view(), name="obtener_usuario"),
    path('', UsuarioView.as_view(), name="home"),
    #path('usuario/lista/<int:pk>/', UsuarioView.as_view(), name="obtener_usuario"),
]
