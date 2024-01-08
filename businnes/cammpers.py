import json
import os

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
    Nota = int(0)
    camper = {
        'Nombre':Nombre,
        'Apellido': Apellido,
        'Identificacion': Identificacion,
        'Direccion': Direccion,
        'Telefono': Telefono,
        'Acudiente': Acudiente,
        'Nota': Nota
    }

    lista_campers.append(camper)
    print("Se creó el camper con éxito")
    guardar_json()




