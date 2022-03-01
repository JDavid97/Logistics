from erp.models import Usuario

def cambiarpw():
    usuarios = Usuario.objects.all()
    for user in usuarios:
        user.set_password(user.password)
        user.save()