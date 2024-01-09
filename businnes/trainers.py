import json
import os
from commons.utils import *

def guardarTrainers_json():
    try:
      with open(os.path.join("proyecto-python", "data", "trainers.json"), 'w') as archivo_json:
        json.dump(lista_Trainers, archivo_json, indent=2)
        print("La lista de Trainers ha sido guardada")
    except FileNotFoundError:
        print("El archivo no existe. Puede que aún no haya Trainers guardados.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON . El formato podría ser incorrecto.")
    except Exception as e:
        print("Error desconocido:")
def cargarTrainers_json():
    try:
        with open(os.path.join("proyecto-python", "data", "trainers.json"), 'r') as archivo_json:        
            lista_Trainers = json.load(archivo_json)
            print("La lista de Trainers ha sido cargada")
            return lista_Trainers
    except FileNotFoundError:
        print("El archivo 'Trainers.json' no existe. Devolviendo una lista vacía.")
        return []
    except Exception as e:
     print(f"Error al cargar el archivo: {e}")
    return []
lista_Trainers = cargarTrainers_json()
def crearTrainer():
    print("Ingrese los datos del nuevo Trainer")
    Nombre= input("Ingrese el nombre del Trainer: ")
    Apellido= input("Ingres el apellido del Trainer")
    Ruta= input("Ingrese la ruta del Trainer")
    Horario= input("Ingrese el horario del Trainer")
    
   
    Trainer = {
        'Nombre': Nombre,
        'Apellido': Apellido,
        'Ruta': Ruta,
        'Horario': Horario,
    }

    lista_Trainers.append(Trainer)
    print("Se creó el trainer con éxito")
    guardarTrainers_json()

def modificarTrainer():
    if not lista_Trainers:
        print("No hay trainers registrados.")
        return

    nombre_trainer = input("Ingrese el nombre del trainer que desea modificar: ")

    for trainer in lista_Trainers:
        if trainer['Nombre'] == nombre_trainer:
            print(f"Datos actuales del trainer {nombre_trainer}:")
            print(trainer)
            dato_a_modificar = input("¿Qué dato desea modificar? (horario/ruta): ").lower()

            if dato_a_modificar == "horario":
                nuevo_valor = input("Nuevo horario del trainer: ")
                if nuevo_valor:
                    trainer['Horario'] = nuevo_valor
            elif dato_a_modificar == "ruta":
                nuevo_valor = input("Nueva ruta del trainer : ")
                if nuevo_valor:
                    trainer['Ruta'] = nuevo_valor
            else:
                print("Opción no válida. No se realizaron modificaciones.")
                return

            print("Trainer modificado con éxito.")
      
            guardarTrainers_json()
            return

    print(f"No se encontró un trainer con el nombre {nombre_trainer}.")





def buscarTrainer():
    def buscar_por_id(json_path, palabra_ingresada):
        try:
            with open(json_path, 'r') as archivo_json:
                data = json.load(archivo_json)
                identificacion_coincidente = [entry for entry in data if entry.get('Nombre') == palabra_ingresada]

                if identificacion_coincidente:
                    print(f"El Trainer con nombre '{palabra_ingresada}' existe. Datos del trainer:")
                    for entry in identificacion_coincidente:
                        print(f"Nombre: {entry['Nombre']}, Apellido: {entry['Apellido']}")
                        print(f"Ruta: {entry['Ruta']}")
                        print(f"Horario: {entry['Horario']}")
                else:
                    print(f"No hay coincidencias para el numero de identifiacion '{palabra_ingresada}'.")

        except FileNotFoundError:
            print(f"El archivo '{json_path}' no fue encontrado.")
        except Exception as e:
            print(f"Error al cargar el archivo JSON: {type(e).__name__}: {e}")


    json_path = os.path.join("proyecto-python", "data", "trainers.json")
 

    palabra_ingresada = input("Ingrese el numero de identificacion del Trainer: ")


    buscar_por_id(json_path, palabra_ingresada)