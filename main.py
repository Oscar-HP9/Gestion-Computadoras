from Monitor import Monitor
from Dispositivos import Teclado, Raton
from Compu import Computadora
from Orden import Orden

"""
Gestor de conjuntos de computadoras
Autor: Oscar Alejandro Hernández Pérez
Descripción: Programa de consola que permite crear, modificar, ver y eliminar conjuntos de computadoras con componentes (Monitor, Teclado, Ratón).
"""

ordenes = {}

def ver_conjuntos():
    if not ordenes:
        print("\tNo hay conjuntos que mostrar.")
    else:
        for _, orden in ordenes.items():
            print(orden)

def añadir_n_computadoras(orden):
    while True:
        try:
            cantidad_compus = int(input("¿Cuántas computadoras desea añadir a este conjunto? (número mayor o igual a cero): ").strip())
            if cantidad_compus < 0:
                print("Error: el número debe ser mayor o igual a cero.")
                continue
            break
        except ValueError:
            print("Error: no ingresaste un número válido.")
    
    if cantidad_compus > 0:
        for _ in range(cantidad_compus):
            orden.agregar_computadora()
        
        print("Se añadieron las computadoras al orden.")
    else:
        print("Sin computadoras que agregar.")

def borra_compu_por_id(id_borrar, conjunto_buscado):
    se_borro = False
    for compu in conjunto_buscado.computadoras:
        if compu.id_computadora == id_borrar:
            conjunto_buscado.computadoras.remove(compu)
            print(f"Se borro la computadora con ID {id_borrar}")
            se_borro = True
            break
    if not se_borro:
        print(f"No existe una computadora con ID {id_borrar}")

def añadir_conjunto():
    orden_n = Orden()
    añadir_n_computadoras(orden_n)
    ordenes[orden_n.id_ordenes] = orden_n

def borrar_conjunto(id_conjunto):
    while True:
        confirmacion = input(f"SE BORRARA EL CONJUNTO CON ID {id_conjunto}, ESTA SEGURO (SI/NO): ").strip().lower()
        if confirmacion == "si":
            del ordenes[id_conjunto]
            break
        elif confirmacion == "no":
            print("Volviendo al menu.")
            break
        else: 
            print("ERROR Ingrese si o no")


def conjunto_por_id(id_buscado):
    if id_buscado in ordenes:
        conjunto_buscado = ordenes[id_buscado]
        print(f"SE ENCONTRO EL CONJUNTO DE COMPUTADORAS CON ID {id_buscado}, MOSTRANDO OPCIONES:")
        while True:
            print("OPCIONES:")
            print("\t1. VER COMPUTADORAS.")
            print("\t2. AÑADIR COMPUTADORAS.")
            print("\t3. ELIMINAR COMPUTADORA POR ID.")
            print("\t4. BORRAR CONJUNTO.")
            print("\t5. VOLVER AL MENU DE CONJUNTOS.")
            opcion_com = input("ingrese la opcion a realizar: ").strip()

            if opcion_com == "1":
                if not conjunto_buscado.computadoras:
                    print("No hay computadoras en este conjunto.")
                else:
                    print("Las computadoras son:")
                    for compu in conjunto_buscado.computadoras:
                        print(compu)
            elif opcion_com == "2":
                añadir_n_computadoras(conjunto_buscado)
            elif opcion_com == "3":
                if not conjunto_buscado.computadoras:
                    print("No hay computadoras para borrar.")
                else:
                    while True:
                        try:
                            id_borrar = int(input("Ingrese el ID de la computadora que quiere borrar (para salir de la opcion ingrese un numero negativo): ").strip())
                            break
                        except ValueError:
                            print("Error: no ingresaste un número válido.")
                    if id_borrar < 0:
                        print("Saliendo de la opcion.")
                    else:
                        borra_compu_por_id(id_borrar, conjunto_buscado)
            elif opcion_com == "4":
                borrar_conjunto(id_buscado)
                break
            elif opcion_com == "5":
                print("Regresando al menu de conjuntos: ")
                break
            else:
                print("Opcion ingresado no valida, intentelo nuevamente.")
    else:
        print(f"No se encontro el conjunto con ID {id_buscado}")
                    

print("*** COMPUTADORAS ***")

while True:
    print("\n\t1. VER CONJUNTOS DE COMPUTADORAS.")
    print("\t2. AÑADIR NUEVO CONJUNTO DE COMPUTADORAS.")
    print("\t3. SELECCIONAR CONJUNTO POR ID.")
    print("\t4. SALIR DEL PROGRAMA.")
    opcion = input("Ingrese la opcion que quiere hacer (1-4): ").strip()

    if opcion == "1":
        ver_conjuntos()
    elif opcion == "2":
        añadir_conjunto()
    elif opcion == "3":
        if not ordenes:
            print("\tNo hay conjuntos que mostrar.")
        else:
            while True:
                try:
                    id_buscado = int(input("Ingrese el ID del conjunto que desea ver (para salir ingrese un numero negativo): "))
                    break
                except ValueError:
                    print("Error: no ingresaste un número válido.")
            if id_buscado < 0:
                print("Saliendo de la opcion.")
            else:
                conjunto_por_id(id_buscado)
    elif opcion == "4":
        print("Hasta luego :)")
        break
    else:
        print("Opción ingresada no válida, inténtelo nuevamente.")
