class Monitor:
    contador_monitores = 0

    def __init__(self, marca, tamaño):
        self.marca = marca
        self.tamaño = tamaño
        Monitor.contador_monitores += 1
        self.id_monitor = Monitor.contador_monitores

    def __str__(self):
        return f"ID: {self.id_monitor} | Marca: {self.marca} | Tamaño: {self.tamaño}"

if __name__ == "__main__":
    monitor1 = Monitor("Logitik", "1 pulgada")
    monitor2 = Monitor("Miniso", "2 pulgadas")
    print(monitor1, monitor2)