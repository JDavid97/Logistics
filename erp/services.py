from erp.models import Usuario
cargos = {
            "Gerente Regional": 1,
            "Subgerente Regional": 2,
            "Ejecutivo Comercial": 3,
            "Gerente Comercial": 4,
            "Asistente de Gerencia": 5,
        }

def is_show_jefe(usuario, jefe):
    return cargos[usuario.cargo] <= cargos[jefe.cargo]


def is_permission(requestUser, usuario):
    return cargos[requestUser.cargo] <= cargos[usuario.cargo]