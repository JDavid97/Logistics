from erp.models import Usuario

def is_show_jefe(usuario, jefe):
    cargos = {
            "Gerente Regional": 1,
            "Subgerente Regional": 2,
            "Ejecutivo Comercial": 3,
            "Gerente Comercial": 4,
            "Asistente de Gerencia": 5,
        }
    return cargos[usuario.cargo] <= cargos[jefe.cargo]