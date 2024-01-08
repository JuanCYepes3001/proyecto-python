import os
import json

json_path = os.path.join("proyecto-python","data", "Ingresos.json")
print("Ruta al archivo:", json_path)

try:
    with open(json_path, 'r') as archivo_json:
       lista_campers = archivo_json
       print("Listado de campers: ")
    for camper in lista_campers:
        print(camper)
except Exception as e:
    print(f"Error al cargar el archivo: {type(e).__name__}: {e}")
   
