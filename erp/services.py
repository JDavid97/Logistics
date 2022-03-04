from erp.models import Usuario

#Niveles de los cargos para ver si un usuario puede entrar al perfil de su jefe
cargos = {
            "Gerente Comercial": 1,
            "Gerente Regional": 2,
            "Subgerente Regional": 3,
            "Ejecutivo Comercial": 4,            
            "Asistente de Gerencia": 5,
        }

def is_show_jefe(usuario, jefe):
    return cargos[usuario.cargo] <= cargos[jefe.cargo]


def is_permission(requestUser, usuario):
    return cargos[requestUser.cargo] <= cargos[usuario.cargo]


def get_total_sales(subor_id):
        total_sales = 0        

        #obtine recursiva de un empleado y sus subalternos
        def sum(subordinates):
            nonlocal total_sales             

            total = subordinates.count()-1
            i = 0
            while i <= total:
                eid = subordinates[i].numeroempleado
                sales = 0 if not subordinates[i].ventas_anteriores else int(subordinates[i].ventas_anteriores) 
                hijos = Usuario.objects.filter(jefe = eid)
                total_sales+= sales
                sum(hijos)
                i+=1

        #Obtenemos el subordinado
        subor = Usuario.objects.filter(numeroempleado = subor_id)
        sum(subor)

        return total_sales