from Monitor import Monitor
from Dispositivos import Teclado, Raton
from Compu import Computadora

class Orden:
    contador_ordenes = 0

    def __init__(self):
        Orden.contador_ordenes += 1
        self.id_ordenes = Orden.contador_ordenes
        self.computadoras = []
    
    def __str__(self):
        salida = f"ID orden: {self.id_ordenes}\n"
        if not self.computadoras:
            return salida + "No hay computadoras en este orden."
        else:
            compus = ""
            for computadora in self.computadoras:
                compus += computadora.__str__() + "\n"
            return salida + compus
        
    def agregar_computadora(self):
        print("\t\t\t*** AGREGAR COMPUTADORA ***")
        monitor_marca = input("Ingrese la marca del monitor de su computadora: ")
        monitor_tamaño = input("Ingrese el tamaño del monitor de su computadora: ")
        monitor = Monitor(monitor_marca, monitor_tamaño)
        teclado_marca = input("Ingrese la marca del teclado de su computadora: ")
        teclado_entrada = input("Ingrese el tipo de entrada de su teclado: ")
        teclado = Teclado(teclado_marca, teclado_entrada)
        raton_marca = input("Ingrese la marca del raton de su computadora: ")
        raton_entrada = input("Ingrese el tipo de entrada de su raton: ")
        raton = Raton(raton_marca, raton_entrada)
        computadora = Computadora(monitor, teclado, raton)
        self.computadoras.append(computadora)
        print("\t\t\tSE AÑADIO LA COMPUTADORA A LA LISTA")

# orden1 = Orden()
# orden1.agregar_computadora()
# orden1.agregar_computadora()
# print(orden1)
