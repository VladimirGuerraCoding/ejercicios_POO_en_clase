class laptop:
    def __init__(self, encender, apagar, actualizar):
        self.encender = encender
        self.apagar = apagar
        self.actualizar =actualizar

    def encender_pc(self):
        if not self.encender:
            self.encender = True
            print(f"la computadora esta encendida")
        else:
            print(f"la computadora ya esta encendida ")
    def apagar(self):

        if self.encender:
            self.encender = False
            print(f"la computadora esta apagada")
    
    def actualizar_ram(self, nueva_ram):
        if not self.encendida:
            print(
                "Por favor, encienda la computadora antes de actualizar la RAM para evitar daños  o bugs en la ram xd."
            )
            return
        if nueva_ram > self.ram:
            print(f"Actualizando RAM de {self.ram}GB a {nueva_ram}GB.")
            self.ram = nueva_ram
        else:
            print("La nueva RAM debe ser mayor que la actual.")


mi_computadora = laptop ("Dell", "Inspiron", 8)
mi_computadora.encender()
mi_computadora.actualizar_ram(16)
mi_computadora.apagar()
        
                      
    