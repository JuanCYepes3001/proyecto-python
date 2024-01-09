from commons.utils import limpiar_pantalla
from commons.menus import menu_principal,menu_trainers,menu_campers,menu_matriculas,menu_aulas,menu_reportes
from businnes.cammpers import *
from businnes.reportes import *
from businnes.aulas import *
from businnes.matriculas import *
from businnes.trainers import *
def campers():      
    limpiar_pantalla()
    op=menu_campers()
    if op==1:
       crear_camper()
       input("Clic cualquier teclas [continuar]: ")
    if op==2:
       listar_campers()
       input("Clic cualquier teclas [continuar]: ")
    if op==3:
       modificar_campers()
       input("Clic cualquier teclas [continuar]: ")
def trainers():
    limpiar_pantalla()    
    op=menu_trainers()
    if op == 1:
        crearTrainer()
        input("Clic cualquier teclas [continuar]: ")
    if op == 2:
        buscarTrainer()
        input("Clic cualquier teclas [continuar]: ")
    if op == 3:
        modificarTrainer()
        input("Clic cualquier teclas [continuar]: ")
def matriculas():
    limpiar_pantalla()    
    op=menu_matriculas()
    if op == 1:
        crearmatricula()
        input("Clic cualquier teclas [continuar]: ")
    if op == 2:
        buscarMatricula()
        input("Clic cualquier teclas [continuar]: ")
    if op == 3:
        modificarMatricula()
        input("Clic cualquier teclas [continuar]: ")
def aulas():
    limpiar_pantalla()    
    op=menu_aulas()
    if op == 1:
        crearAulas()
        input("Clic cualquier teclas [continuar]: ")
    if op == 2:
        buscarAulas()
        input("Clic cualquier teclas [continuar]: ")
    if op == 3:
        modificarAulas()
        input("Clic cualquier teclas [continuar]: ")
def reportes():
    limpiar_pantalla()    
    op=menu_reportes()
    if op ==1:
        inscritos()
        input("Clic cualquier teclas [continuar]: ")
    elif op==2:
        aprobados()
        input("Clic cualquier teclas [continuar]: ")
    elif op==3:
        lista_trainers()
        input("Clic cualquier teclas [continuar]: ")
    elif op==4:
        camp_bajo_rendimiento()
        input("Clic cualquier teclas [continuar]: ")
    elif op==5:
        camp_trainer()
        input("Clic cualquier teclas [continuar]: ")
    elif op==6:
        camp_ap_rep_ruta()
        input("Clic cualquier teclas [continuar]: ")

    

#start
while True: 
   limpiar_pantalla()
   op=menu_principal()
   if  op==1:
       campers()
   elif op==2:
       trainers()
   elif op==3:
       matriculas()
   elif op==4:
       aulas()
   elif op==5:
       reportes()
   elif op==6:
       print("Saliendo")
       break
       