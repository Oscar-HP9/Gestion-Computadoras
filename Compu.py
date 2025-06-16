class Computadora:
    contador_computadoras = 0

    def __init__(self, monitor, teclado, raton):
        Computadora.contador_computadoras += 1
        self.id_computadora = Computadora.contador_computadoras
        self.monitor = monitor
        self.teclado = teclado
        self.raton = raton
    
    def __str__(self):
        return f"Computadora ID: {self.id_computadora}\n\tMonitor: {self.monitor.__str__()}\n\tTeclado: {self.teclado.__str__()}\n\tRaton: {self.raton.__str__()}"

