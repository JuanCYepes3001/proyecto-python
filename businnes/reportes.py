import json
import os
def inscritos():
    print("Los campers inscritos son:")  
    def nom_ap(file):
        try:
            with open(file, 'r') as archivo_json:
                data = json.load(archivo_json)
                
                if all(entry.get('Nombre') is not None and entry.get('Apellido') is not None for entry in data):
                    # Obtén una lista de tuplas (nombre, apellido)
                    names_and_surnames = [(entry['Nombre'], entry['Apellido']) for entry in data]
                    return names_and_surnames
                else:
                    print("El archivo JSON no tiene la estructura esperada (nombre y apellido).")
                    return []
        except FileNotFoundError:
            print(f"El archivo  no fue encontrado.")
            return []
        except Exception as e:
            print(f"Error al cargar el archivo JSON: {type(e).__name__}: {e}")
            return []
    
    json_path = os.path.join("proyecto-python","data","Ingresos.json")

    nombres_apellidos = nom_ap(json_path)

    for Nombre, Apellido in nombres_apellidos:
            print(f"{Nombre} {Apellido}")


def aprobados():
    print("Los campers aprobados son:")
    def ap(file_path):
        try:
            with open(file_path, 'r') as archivo_json:
                data = json.load(archivo_json)

                if all(entry.get('Nombre') is not None and entry.get('Apellido') is not None and
                       entry.get('NotaT') is not None and entry.get('NotaP') is not None for entry in data):
                    # Obtén una lista de tuplas (Nombre, Apellido, NotaT, NotaP)
                    info_campers = [(entry['Nombre'], entry['Apellido'], entry['NotaT'], entry['NotaP']) for entry in data]
                    return info_campers
                else:
                    print("El archivo JSON no tiene la estructura esperada (Nombre, Apellido, NotaT, NotaP).")
                    return []
        except FileNotFoundError:
            print("El archivo no fue encontrado.")
            return []
        except Exception as e:
            print(f"Error al cargar el archivo JSON: {type(e).__name__}: {e}")
            return []

    json_path = os.path.join("proyecto-python", "data", "Ingresos.json")

    info_campers = ap(json_path)

    for Nombre, Apellido, NotaT, NotaP in info_campers:
        promedio = (NotaT + NotaP) / 2
        if promedio > 60:
            print(f"{Nombre} {Apellido} - Promedio: {promedio}")

def lista_trainers():
    print("Los traines en campus son:")
    def nom_ap_p(file):
        try:
            with open(file, 'r') as archivo_json:
                data = json.load(archivo_json)
                
                if all(entry.get('Nombre') is not None and entry.get('Apellido') is not None for entry in data):
                  
                    names_and_surnames = [(entry['Nombre'], entry['Apellido']) for entry in data]
                    return names_and_surnames
                else:
                    print("El archivo JSON no tiene la estructura esperada (nombre y apellido).")
                    return []
        except FileNotFoundError:
            print(f"El archivo  no fue encontrado.")
            return []
        except Exception as e:
            print(f"Error al cargar el archivo JSON: {type(e).__name__}: {e}")
            return []
    
    json_path = os.path.join("proyecto-python","data","trainers.json")

    nombres_apellidos = nom_ap_p(json_path)

    for Nombre, Apellido in nombres_apellidos:
            print(f"{Nombre} {Apellido}")
def camp_bajo_rendimiento():
    print("Los campers con bajo rendimiento son:")
    def bajo_ren(file_path):
        try:
            with open(file_path, 'r') as archivo_json:
                data = json.load(archivo_json)

                if all(entry.get('Nombre') is not None and entry.get('Apellido') is not None and
                       entry.get('NotaT') is not None and entry.get('NotaP') is not None for entry in data):
                    # Obtén una lista de tuplas (Nombre, Apellido, NotaT, NotaP)
                    info_campers = [(entry['Nombre'], entry['Apellido'], entry['NotaT'], entry['NotaP']) for entry in data]
                    return info_campers
                else:
                    print("El archivo JSON no tiene la estructura esperada (Nombre, Apellido, NotaT, NotaP).")
                    return []
        except FileNotFoundError:
            print("El archivo no fue encontrado.")
            return []
        except Exception as e:
            print(f"Error al cargar el archivo JSON: {type(e).__name__}: {e}")
            return []

    json_path = os.path.join("proyecto-python", "data", "CampersData.json")

    info_campers = bajo_ren(json_path)

    for Nombre, Apellido, NotaT, NotaP in info_campers:
        promedio = (NotaT + NotaP) / 2
        if promedio < 60:
            print(f"{Nombre} {Apellido} - Promedio: {promedio}")
def camp_trainer():
    print("Menu rutas")

def camp_ap_rep_ruta():
    print("Menu rutas")

