
from commons.utils import validar_opcion
def menu_principal():
    print("----------- Menú Principal-----------")
    print("1. Campers")
    print("2. Trainers")
    print("3. Matriculas")
    print("4. Aulas")
    print("5. Reportes")
    print("6. Salir")       
    op=validar_opcion("Opcion: ",1,6)
    return op

def menu_campers():
    print("----------- Menú Campers-----------")
    print("1. Crear campers")
    print("2. listar campers")
    print("3. Modificar campers")
    print("4. Salir")
    op=validar_opcion("Opcion: ",1,4)
    return op
    
    
def menu_trainers():
    print("----------- Menú Trainers-----------")
    print("1. Crear trainer")
    print("2. Buscar trainer")
    print("3. Modificar trainer")
    print("4. Salir")
    op=validar_opcion("Opcion: ",1,4)
    return op

def menu_matriculas():
    print("----------- Menú Matriculas-----------")
    print("1. Crear Matriculas")
    print("2. Buscar Matriculas")
    print("3. Modificar Matriuclas")
    print("4. Salir")
    op=validar_opcion("Opcion: ",1,4)
    return op

def menu_aulas():
    print("----------- Menú Aulas-----------")
    print("1. Crear Aulas")
    print("2. Buscar Aulas")
    print("3. Modificar Aulas")
    print("4. Salir")
    op=validar_opcion("Opcion: ",1,4)
    return op

def menu_reportes():
    print("----------- Menú Reportes-----------")
    print("1. Listar campers estado inscrito")
    print("2. Listar campers aprobaron examen")
    print("3. Listar trainers trabajando en campus")
    print("4. Listar campers con bajo rendimiento")
    print("5. Listar campers y entrenador por ruta")
    print("6. Listar campers aprobados y reprobados por ruta")
    print("7. Salir")
    op=validar_opcion("Opcion: ",1,7)
    return op

def menu_rutas():
    print("----------- Menú Rutas-----------")
    print("1. Ruta NodeJS")
    print("2. Ruta Java")
    print("3. Ruta NetCore")
    print("4. Salir")
    op=validar_opcion("Opcion: ",1,4)
    return op

def mod_matricula():
    print("-----------Modificar matriculas-----------")
    print("1. Direccion")
    print("2. Telefono")
    print("3. Acudiente")
    print("4. Ruta")
    print("5. Horario")
    print("6. Profesor")
    print("7. Salon")
    print("8. Modulo")
    print("9. Salir")
    op=validar_opcion("Opcion: ",1,9)
    return op

def mod_camper():
    print("-----------Modificar camper-----------")
    print("1. Direccion")
    print("2. Telefono")
    print("3. Acudiente")
    print("4. Nota practica")
    print("5. Nota teorica")
    print("6. Salir")
    op=validar_opcion("Opcion: ",1,6)
    return op