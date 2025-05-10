class Laptop:
    def __init__(self, encender, apagar, actualizar):
        self.encender = encender
        self.apagar = apagar
        self.actualizar = actualizar
    
        self.encendido = False
        
    def encender(self):
        if not self.encendido:
            self.encendido = True
            print(f'la computadora esta encendida')
        else:
            print('la computadora esta apagada')    
        
        
    