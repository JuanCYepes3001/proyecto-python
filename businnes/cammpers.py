import json
import os
from commons.menus import mod_camper
def guardar_json():
    try:
      with open(os.path.join("proyecto-python","data","Ingresos.json"), 'w') as archivo_json:
        json.dump(lista_campers, archivo_json, indent=2)
        print("La lista de campers ha sido guardada")
    except FileNotFoundError:
        print("El archivo no existe. Puede que aún no haya campers guardados.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON . El formato podría ser incorrecto.")
    except Exception as e:
        print("Error desconocido:")
def listar_campers():
    print("Listado de campers: ")
    for camper in lista_campers:
        print(camper)

def load_campers_json():
    try:
        with open(os.path.join("proyecto-python","data","Ingresos.json"), 'r') as archivo_json:        
            lista_campers = json.load(archivo_json)
            print("La lista de campers ha sido cargada")
            return lista_campers
    except FileNotFoundError:
        print("El archivo 'Ingresos.json' no existe. Devolviendo una lista vacía.")
        return []
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")
        return []
lista_campers = load_campers_json()

def crear_camper():
    Nombre = input("Ingrese el nombre del camper: ")
    Apellido = input("Ingrese el apellido del camper: ")
    Identificacion = int(input("Ingrese la Identificacion del camper: "))
    Direccion = input("Ingrese la direccion del camper: ")
    Telefono = input("Ingrese el número de teléfono del camper: ")
    Acudiente = input("Ingrese nombre del acudiente del camper: ")
    NotaP = int(0)
    NotaT = int(0)
    camper = {
        'Nombre':Nombre,
        'Apellido': Apellido,
        'Identificacion': Identificacion,
        'Direccion': Direccion,
        'Telefono': Telefono,
        'Acudiente': Acudiente,
        'NotaP': NotaP,
        'NotaT': NotaT
    }

    lista_campers.append(camper)
    print("Se creó el camper con éxito")
    guardar_json()

def modificar_campers():
    if not lista_campers:
        print("No hay campers registrados.")
        return

    nombre_camper = input("Ingrese la identificacion del camper que desea modificar: ")

    for campers in lista_campers:
        if campers['Identificacion'] == nombre_camper:
            print(f"Datos actuales del campers con identificacion {nombre_camper}:")
            print(campers)
            op = mod_camper()

            if op == 1:
                nuevo_valor = input("Direccion: ")
                if nuevo_valor:
                    campers['Direccion'] = nuevo_valor
            elif op == 2:
                nuevo_valor = input("Telefono: ")
                if nuevo_valor:
                    campers['Telefono'] = nuevo_valor
            elif op == 3:
                nuevo_valor = input("Acudiente: ")
                if nuevo_valor:
                    campers['Acudiente'] = nuevo_valor
            elif op == 4:
                nuevo_valor = int(input("Nota practica: "))
                if nuevo_valor:
                    campers['NotaP'] = nuevo_valor
            elif op == 5:
                nuevo_valor = int(input("Nota teorica: "))
                if nuevo_valor:
                    campers['NotaT'] = nuevo_valor
            else:
                print("Opción no válida. No se realizaron modificaciones.")
                return

            print("Camper modificado con éxito.")
      
            guardar_json()
            return

    print(f"No se encontró un campers con el nombre {nombre_camper}.")


