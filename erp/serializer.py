from erp.models import Usuario
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model= Usuario
        fields = ('id', 'nombres', 'apellido_uno', 'apellido_dos', 'cedula','genero','cargo','zona')