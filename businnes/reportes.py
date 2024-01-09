import json
import os
from commons.menus import menu_rutas
from commons.utils import limpiar_pantalla

def inscritos():
    print("Los campers inscritos son:")  
    def nom_ap(file):
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

def camp_ent_ruta1():
    def mostrar_campers_con_ruta(json_path):
        try:
            with open(json_path, 'r') as archivo_json:
                data = json.load(archivo_json)

                if all(entry.get('Nombre') is not None and entry.get('Apellido') is not None and
                    entry.get('Profesor') is not None and entry.get('Ruta') is not None for entry in data):
            
                    campers_nodejs = [(entry['Nombre'], entry['Apellido'], entry['Profesor']) for entry in data if entry['Ruta'] == 'NodeJS']

                    for Nombre, Apellido, Profesor in campers_nodejs:
                        print(f"Nombre: {Nombre}, Apellido: {Apellido}, Profesor: {Profesor}")

                else:
                    print("El archivo JSON no tiene la estructura esperada (Nombre, Apellido, profesor, Ruta).")
        except FileNotFoundError:
            print(f"El archivo '{json_path}' no fue encontrado.")
        except Exception as e:
            print(f"Error al cargar el archivo JSON: {type(e).__name__}: {e}")

    json_path = os.path.join("proyecto-python", "data", "CampersData.json")
    mostrar_campers_con_ruta(json_path)
def camp_ent_ruta2():
    def mostrar_campers_con_ruta(json_path):
        try:
            with open(json_path, 'r') as archivo_json:
                data = json.load(archivo_json)

                if all(entry.get('Nombre') is not None and entry.get('Apellido') is not None and
                    entry.get('Profesor') is not None and entry.get('Ruta') is not None for entry in data):
            
                    campers_nodejs = [(entry['Nombre'], entry['Apellido'], entry['Profesor']) for entry in data if entry['Ruta'] == 'Java']

                    for Nombre, Apellido, Profesor in campers_nodejs:
                        print(f"Nombre: {Nombre}, Apellido: {Apellido}, Profesor: {Profesor}")

                else:
                    print("El archivo JSON no tiene la estructura esperada (Nombre, Apellido, profesor, Ruta).")
        except FileNotFoundError:
            print(f"El archivo '{json_path}' no fue encontrado.")
        except Exception as e:
            print(f"Error al cargar el archivo JSON: {type(e).__name__}: {e}")

    json_path = os.path.join("proyecto-python", "data", "CampersData.json")
    mostrar_campers_con_ruta(json_path)
def camp_ent_ruta3():
    def mostrar_campers_con_ruta(json_path):
        try:
            with open(json_path, 'r') as archivo_json:
                data = json.load(archivo_json)

                if all(entry.get('Nombre') is not None and entry.get('Apellido') is not None and
                    entry.get('Profesor') is not None and entry.get('Ruta') is not None for entry in data):
            
                    campers_nodejs = [(entry['Nombre'], entry['Apellido'], entry['Profesor']) for entry in data if entry['Ruta'] == 'NetCore']

                    for Nombre, Apellido, Profesor in campers_nodejs:
                        print(f"Nombre: {Nombre}, Apellido: {Apellido}, Profesor: {Profesor}")

                else:
                    print("El archivo JSON no tiene la estructura esperada (Nombre, Apellido, profesor, Ruta).")
        except FileNotFoundError:
            print(f"El archivo '{json_path}' no fue encontrado.")
        except Exception as e:
            print(f"Error al cargar el archivo JSON: {type(e).__name__}: {e}")

    json_path = os.path.join("proyecto-python", "data", "CampersData.json")
    mostrar_campers_con_ruta(json_path)
def camp_trainer():
    limpiar_pantalla() 
    op=menu_rutas()
    if op ==1:
        camp_ent_ruta1()
    elif op==2:
        camp_ent_ruta2()
    elif op==3:
        camp_ent_ruta3()

def camp_ruta1():
    def mostrar_campers_con_ruta(json_path):
        try:
            with open(json_path, 'r') as archivo_json:
                data = json.load(archivo_json)

             
                if all(entry.get('Nombre') is not None and entry.get('Apellido') is not None and
                    entry.get('Profesor') is not None and entry.get('Ruta') is not None and
                    entry.get('NotaT') is not None and entry.get('NotaP') is not None for entry in data):

                    campers_nodejs = [(entry['Nombre'], entry['Apellido'], entry['NotaT'], entry['NotaP']) for entry in data if entry['Ruta'] == 'NodeJS']

                    for Nombre, Apellido, NotaT, NotaP in campers_nodejs:
              
                        nota_final = 0.3 * NotaT + 0.6 * NotaP
                 
                        estado = "Aprobado" if nota_final > 60 else "En Riesgo"

                        print(f"Nombre: {Nombre}, Apellido: {Apellido}, Nota Final: {nota_final:.2f}, Estado: {estado}")

                else:
                    print("El archivo JSON no tiene la estructura esperada (Nombre, Apellido, profesor, Ruta, NotaT, NotaP).")
        except FileNotFoundError:
            print(f"El archivo '{json_path}' no fue encontrado.")
        except Exception as e:
            print(f"Error al cargar el archivo JSON: {type(e).__name__}: {e}")
         
    json_path = os.path.join("proyecto-python", "data", "CampersData.json")

    mostrar_campers_con_ruta(json_path)
def camp_ruta2():
    def mostrar_campers_con_ruta(json_path):
            try:
                with open(json_path, 'r') as archivo_json:
                    data = json.load(archivo_json)

                
                    if all(entry.get('Nombre') is not None and entry.get('Apellido') is not None and
                        entry.get('Profesor') is not None and entry.get('Ruta') is not None and
                        entry.get('NotaT') is not None and entry.get('NotaP') is not None for entry in data):

                        campers_nodejs = [(entry['Nombre'], entry['Apellido'], entry['NotaT'], entry['NotaP']) for entry in data if entry['Ruta'] == 'Java']

                        for Nombre, Apellido, NotaT, NotaP in campers_nodejs:
                
                            nota_final = 0.3 * NotaT + 0.6 * NotaP
                    
                            estado = "Aprobado" if nota_final > 60 else "En Riesgo"

                            print(f"Nombre: {Nombre}, Apellido: {Apellido}, Nota Final: {nota_final:.2f}, Estado: {estado}")

                    else:
                        print("El archivo JSON no tiene la estructura esperada (Nombre, Apellido, profesor, Ruta, NotaT, NotaP).")
            except FileNotFoundError:
                print(f"El archivo '{json_path}' no fue encontrado.")
            except Exception as e:
                print(f"Error al cargar el archivo JSON: {type(e).__name__}: {e}")
            
    json_path = os.path.join("proyecto-python", "data", "CampersData.json")

    mostrar_campers_con_ruta(json_path)
def camp_ruta3():
    def mostrar_campers_con_ruta(json_path):
        try:
            with open(json_path, 'r') as archivo_json:
                data = json.load(archivo_json)

             
                if all(entry.get('Nombre') is not None and entry.get('Apellido') is not None and
                    entry.get('Profesor') is not None and entry.get('Ruta') is not None and
                    entry.get('NotaT') is not None and entry.get('NotaP') is not None for entry in data):

                    campers_nodejs = [(entry['Nombre'], entry['Apellido'], entry['NotaT'], entry['NotaP']) for entry in data if entry['Ruta'] == 'NetCore']

                    for Nombre, Apellido, NotaT, NotaP in campers_nodejs:
              
                        nota_final = 0.3 * NotaT + 0.6 * NotaP
                 
                        estado = "Aprobado" if nota_final > 60 else "En Riesgo"

                        print(f"Nombre: {Nombre}, Apellido: {Apellido}, Nota Final: {nota_final:.2f}, Estado: {estado}")

                else:
                    print("El archivo JSON no tiene la estructura esperada (Nombre, Apellido, Profesor, Ruta, NotaT, NotaP).")
        except FileNotFoundError:
            print(f"El archivo '{json_path}' no fue encontrado.")
        except Exception as e:
            print(f"Error al cargar el archivo JSON: {type(e).__name__}: {e}")
         
    json_path = os.path.join("proyecto-python", "data", "CampersData.json")

    mostrar_campers_con_ruta(json_path)
def camp_ap_rep_ruta():
    limpiar_pantalla() 
    op=menu_rutas()
    if op ==1:
        camp_ruta1()
    elif op==2:
        camp_ruta2()
    elif op==3:
        camp_ruta3()

