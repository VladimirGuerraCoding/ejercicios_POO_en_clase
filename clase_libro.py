class Libro :
    def __init__(self, nombre, autor, codigo):
        self.nombre = nombre
        self.autor = autor
        self.codigo = codigo
        self.prestado = False
        self.prestado_a = None

    def prestar(self, nombre_usuario):
     if not self.prestado:
      self.prestado = True
      self.prestado_a = nombre_usuario
      print(f" el libro {self.nombre}, ha sido prestado a {nombre_usuario}")
     else :
       print(f"el libro {self.nombre}, se encuentra pretado a {self.prestado_a}")  

    def Devolver(self):
      if self.prestado:
        print(f"el libro {self.nombre}, ha sido devuelto por  {self.prestado_a} ")
        self.prestado = False
        self.prestado_a = None
      else:
        print(f"el libro {self.nombre}, ha sido prestado a {self.prestado_a} ")

    def estado(self):
      if self.prestado:
        print (f"a sido prestado a {self.prestado_a}")
      else:
        print (f"se encuentra DISPONIBLE")

    def codigo(self):
      print(f"el libro {self.nombre}, del autor {self.autor} con codigo {self.codigo} se encuentra en estado {self.estado}") 
class usuario:
    def __init__(self, nombre):
        self.nombre = nombre 
    def pedir_prestado_libro(self, libro):
        libro.prestar(self)

    def devolver_libro(self, libro):
        libro.devolver(self)

    def libros_prestados(self):
        if self.libros_prestados:
            print(f"el usuario {self.nombre} tienen los siguientes libros prestados")
            for libro in self.libros_prestados:
                print(f" - {libro.nombre}")
        else:
            print(f"el usuario {self.nombre} no tiene libros prestados " ) 


            
      
libro1 = Libro("el principito", "Antoine de Saint-Exupéry", "9788")
libro2 = Libro("el poder de las palbras", "mariano sigman", "9789")
usuario1 = usuario("jerson chara")
usuario2 = usuario("jose dilmer")
usuario3 = usuario("andrea sanabria")

usuario1 = usuario.pedir_prestado_libro(libro1)
usuario1 = usuario.pedir_prestado_libro(libro2)
usuario1 = usuario.devolver_libro(libro1)
usuario1 = usuario.libros_prestados()

usuario2 = usuario.pedir_prestado_libro(libro2)

usuario1 = usuario.devolver_libro(libro2)
usuario2 = usuario.pedir_prestado_libro(libro1)

usuario3 = usuario.libros_prestados

