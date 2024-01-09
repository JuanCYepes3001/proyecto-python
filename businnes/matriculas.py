import json
import os
from commons.utils import *
from commons.menus import mod_matricula

def guardarMatricula_json():
    try:
      with open(os.path.join("proyecto-python", "data", "CampersData.json"), 'w') as archivo_json:
        json.dump(lista_matriculas, archivo_json, indent=2)
        print("La lista de matriculas ha sido guardada")
    except FileNotFoundError:
        print("El archivo no existe. Puede que aún no haya matriculas guardados.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON . El formato podría ser incorrecto.")
    except Exception as e:
        print("Error desconocido:")
def cargarmatriculas_json():
    try:
        with open(os.path.join("proyecto-python", "data", "CampersData.json"), 'r') as archivo_json:        
            lista_matriculas = json.load(archivo_json)
            print("La lista de matriculas ha sido cargada")
            return lista_matriculas
    except FileNotFoundError:
        print("El archivo 'matriculas.json' no existe. Devolviendo una lista vacía.")
        return []
    except Exception as e:
     print(f"Error al cargar el archivo: {e}")
    return []
lista_matriculas = cargarmatriculas_json()
def crearmatricula():
    print("Ingrese los datos del nuevo Camper")
    Nombre= input("Ingrese el nombre del camper: ")
    Apellido= input("Ingres el apellido del camper")
    Identificacion = input("Ingrese el numero de identificacion del camper")
    Direccion= input("Ingrese la direccion del Camper")
    Telefono= input("Ingrese el telefono del camper")
    Acudiente= input("Ingrese el nombre del acudiente del camper")
    Ruta= input("Ingrese la ruta del camper")
    Horario= input("Ingrese el horario del camper")
    Profesor = input("Ingrese el profesor asignado")
    Salon= input("Ingrese el salon")
    Modulo= input("Ingrese el modulo")
    Fecha_Inicio= input("Ingrese la fecha de inicio")
    Fecha_Fin= input("Ingrese la fecha estimada para finalizar la formacion")
   
    camper = {
        'Nombre': Nombre,
        'Apellido': Apellido,
        'Identificacion': Identificacion,
        'Direccion': Direccion,
        'Telefono': Telefono,
        'Acudiente': Acudiente,
        'Ruta': Ruta,
        'Horario': Horario,
        'Profesor': Profesor,
        'Salon': Salon,
        'Modulo': Modulo,
        'Fecha Inicio': Fecha_Inicio,
        'Fecha Fin': Fecha_Fin 
    }

    lista_matriculas.append(camper)
    print("Se creó la matricula con éxito")
    guardarMatricula_json()

def modificarMatricula():
    if not lista_matriculas:
        print("No hay Matriculass registrados.")
        return

    id_Matriculas = input("Ingrese el numero de identificacion de la matricula que desea modificar: ")

    for Matriculas in lista_matriculas:
        if Matriculas['Identificacion'] == id_Matriculas:
            print(f"Datos actuales del Matriculas {id_Matriculas}:")
            print(Matriculas)
            op = mod_matricula()
            if op== 1:
                nuevo_valor = input("Nueva direccion: ")
                if nuevo_valor:
                    Matriculas['Direccion'] = nuevo_valor
            elif op== 2:
                nuevo_valor = input("Nuevo Telefono: ")
                if nuevo_valor:
                    Matriculas['Telefono'] = nuevo_valor
            elif op== 3:
                nuevo_valor = input("Nuevo Acudiente: ")
                if nuevo_valor:
                    Matriculas['Acudiente'] = nuevo_valor
            elif op== 4:
                nuevo_valor = input("Nuevo Ruta: ")
                if nuevo_valor:
                    Matriculas['Ruta'] = nuevo_valor
            elif op== 5:
                nuevo_valor = input("Nuevo Horario: ")
                if nuevo_valor:
                    Matriculas['Horario'] = nuevo_valor
            elif op== 6:
                nuevo_valor = input("Nuevo Profesor: ")
                if nuevo_valor:
                    Matriculas['Profesor'] = nuevo_valor
            elif op== 7:
                nuevo_valor = input("Nuevo Salon: ")
                if nuevo_valor:
                    Matriculas['Salon'] = nuevo_valor
            elif op== 8:
                nuevo_valor = input("Nuevo Modulo: ")
                if nuevo_valor:
                    Matriculas['Modulo'] = nuevo_valor
            else:
                print("Opción no válida. No se realizaron modificaciones.")
                return

            print("Matriculas modificado con éxito.")
      
            guardarMatricula_json()
            return

    print(f"No se encontró un Matriculas con la identificacion {id_Matriculas}.")


    

def buscarMatricula():
    def buscar_por_id(json_path, palabra_ingresada):
        try:
            with open(json_path, 'r') as archivo_json:
                data = json.load(archivo_json)
                identificacion_coincidente = [entry for entry in data if entry.get('Identificacion') == palabra_ingresada]

                if identificacion_coincidente:
                    print(f"El camper con identificacion '{palabra_ingresada}' existe. Datos de los estudiantes:")
                    for entry in identificacion_coincidente:
                        print(f"Nombre: {entry['Nombre']}, Apellido: {entry['Apellido']}")
                        print(f"Direccion: {entry['Direccion']}")
                        print(f"Telefono: {entry['Telefono']}")
                        print(f"Acudiente: {entry['Acudiente']}")
                        print(f"Ruta: {entry['Ruta']}")
                        print(f"Horario: {entry['Horario']}")
                        print(f"Profesor: {entry['Profesor']}")
                        print(f"Salon: {entry['Salon']}")
                        print(f"Modulo: {entry['Modulo']}")
                else:
                    print(f"No hay coincidencias para el numero de identifiacion '{palabra_ingresada}'.")

        except FileNotFoundError:
            print(f"El archivo '{json_path}' no fue encontrado.")
        except Exception as e:
            print(f"Error al cargar el archivo JSON: {type(e).__name__}: {e}")


    json_path = os.path.join("proyecto-python", "data", "CampersData.json")
 

    palabra_ingresada = input("Ingrese el numero de identificacion del camper: ")


    buscar_por_id(json_path, palabra_ingresada)