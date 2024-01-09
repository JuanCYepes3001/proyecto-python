import json
import os
from commons.utils import *

def guardarAulas_json():
    try:
      with open(os.path.join("data","Aulas.json"), 'w') as archivo_json:
        json.dump(lista_aulas, archivo_json, indent=2)
        print("La lista de Aulas ha sido guardada")
    except FileNotFoundError:
        print("El archivo no existe. Puede que aún no haya Aulas guardados.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON . El formato podría ser incorrecto.")
    except Exception as e:
        print("Error desconocido:")

def cargarAulas_json():
    try:
        with open(os.path.join("data","Aulas.json"), 'r') as archivo_json:        
            lista_aulas = json.load(archivo_json)
            print("La lista de Aulas ha sido cargada")
            return lista_aulas
    except FileNotFoundError:
        print("El archivo 'Aulas.json' no existe. Devolviendo una lista vacía.")
        return []
    except Exception as e:
     print(f"Error al cargar el archivo: {e}")
    return []
lista_aulas = cargarAulas_json()
    

def crearAulas():
    print("Seleccione el aula que desea revisar.")
    AulaNombre = input("Ingrese el nombre del Aula (Grupo): ")
    Ruta = input("Ingrese la Ruta del Aula: ")
    Modulo = input("Ingrese el modulo del Aula: ")
    ZonaEntrenamiento = input("Ingrese Zona de Entrenamiento del Aula: ")
    Trainer = input("Ingrese el trainer asignado al Aula: ")
    camper = {
        'Nombre':AulaNombre,
        'Ruta': Ruta,
        'Modulo': Modulo,
        'Zona de Entrenamiento': ZonaEntrenamiento,
        'Trainer': Trainer,
    }

    lista_aulas.append(camper)
    print("Se creó el aula con éxito")
    guardarAulas_json()

def modificarAulas():
    pass
    

def buscarAulas():
    def buscar_por_aula(json_path, palabra_ingresada):
        try:
            with open(json_path, 'r') as archivo_json:
                data = json.load(archivo_json)
                aulas_coincidentes = [entry for entry in data if entry.get('Aula') == palabra_ingresada]

                if aulas_coincidentes:
                    print(f"El aula '{palabra_ingresada}' existe. Datos de los estudiantes:")
                    for entry in aulas_coincidentes:
                        print(f"Nombre: {entry['Nombre']}, Ruta: {entry['Ruta']}, Modulo: {entry['Modulo']}")
                else:
                    print(f"No hay coincidencias para el aula '{palabra_ingresada}'.")

        except FileNotFoundError:
            print(f"El archivo '{json_path}' no fue encontrado.")
        except Exception as e:
            print(f"Error al cargar el archivo JSON: {type(e).__name__}: {e}")


    json_path = os.path.join("proyecto-python","data","Aulas.json")
 

    palabra_ingresada = input("Ingrese una palabra para buscar por Aula: ")


    buscar_por_aula(json_path, palabra_ingresada)