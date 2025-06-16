class DispositivoEntrada:
    
    def __init__(self, marca, tipo_entrada):
        self._marca = marca
        self._tipo_entrada = tipo_entrada
    
    @property
    def marca(self):
        return self._marca
    
    @property
    def tipo_entrada(self):
        return self._tipo_entrada
    
class Raton(DispositivoEntrada):
    contador_ratones = 0
    
    def __init__(self, marca, tipo_entrada):
        super().__init__(marca, tipo_entrada)
        Raton.contador_ratones += 1
        self.id_raton = Raton.contador_ratones
    
    def __str__(self):
        return (f"ID: {self.id_raton} | Marca: {self.marca} | Tipo de entrada: {self.tipo_entrada}")

class Teclado(DispositivoEntrada):
    contador_teclados = 0
    
    def __init__(self, marca, tipo_entrada):
        super().__init__(marca, tipo_entrada)
        Teclado.contador_teclados += 1
        self.id_teclado = Teclado.contador_teclados
    
    def __str__(self):
        return (f"ID: {self.id_teclado} | Marca: {self.marca} | Tipo de entrada: {self.tipo_entrada}")

if __name__ == "__main__":
    raton1 = Raton("logitik", "XD")
    raton2 = Raton("Miniso", "XD2")
    teclado1 = Teclado("Verbatim", "Escritura")
    print(raton1)
    print(raton2)
    print(teclado1)