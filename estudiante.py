class Estudiante:
    def _init_(self, nombre, edad, carrera, calificaciones=None):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
        self.calificaciones = calificaciones if calificaciones is not None else []

    def presentarse(self):
        return f"Hola, mi nombre es {self.nombre}, tengo {self.edad} años y estudio {self.carrera}."

    def calcular_promedio(self):
        if not self.calificaciones:
            return 0
        return sum(self.calificaciones) / len(self.calificaciones)

    def ingresar_nota(self, nota):
        self.calificaciones.append(nota)

    def eliminar_nota(self, nota):
        if nota in self.calificaciones:
            self.calificaciones.remove(nota)

estudiante1 = Estudiante("Andrés", 22, "Ingeniería de Sistemas", [85, 90, 78, 92])
estudiante2 = Estudiante("Laura", 21, "Matemáticas")  
estudiante3 = Estudiante("jerson", 29,"Programacion", (75, 88, 90, 92) )

print(estudiante1.presentarse())
print(f"Promedio: {estudiante1.calcular_promedio():.2f}\n")

print(estudiante2.presentarse())
print(f"Promedio: {estudiante2.calcular_promedio():.2f}")

print(estudiante3.presentarse())
print(f"promedio: {estudiante3.calcular_promedio():.2f}")