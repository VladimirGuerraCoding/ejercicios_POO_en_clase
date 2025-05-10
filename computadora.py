class Computadora:
    def __init__(self, marca, memoria, almacenamiento, procesador):
        self.marca = marca
        self.memoria = memoria
        self.almacenamiento = almacenamiento
        self.procesador = procesador
        print(f'El computador {self.marca} tiene memoria ram de {self.memoria} capacidad en disco de {self.almacenamiento} y un procesador {self.procesador} que garantiza su rendimiento.')
        
        
computador1 = Computadora('Dell', '8GB', '2TB', 'Intel-Core-i3-5005U-CPU-2.00GHz')
    
print(computador1)
    
    
            
        
        
    