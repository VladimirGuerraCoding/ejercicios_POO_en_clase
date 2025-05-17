class usuario:
    def __init__(self, nombre):
        self.nombre = nombre 
    def pedir_prestado_libro(self, libro):
        libro.prestar(self)

    def devolver_libro(self, libro):
        libro.devolver(self)

    def libros_prestados(self, ):
        if self.libros_prestados:
            print(f"el usuario {self.nombre} tienen los siguientes libros prestados")
            for libro in self.libros_prestados:
                print(f" - {libro.nombre}")
        else:
            print(f"el usuario {self.nombre} no tiene libros prestados " ) 

usuario1 = usuario("jerson chara bastidas")
usuario2 = usuario("jose dilmer")
usuario3 = usuario("jhon alejando") 


                    