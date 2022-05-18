#En este segundo ejercicio, tendréis que crear un programa que tenga una clase
# llamada Alumno que tenga como atributos su nombre y su nota. Deberéis de
# definir los métodos para inicializar sus atributos, imprimirlos y mostrar un
# mensaje con el resultado de la nota y si ha aprobado o no.


class Alumno:
    nombre = None
    nota = None

    def setNombre(self, nombre):
        self.nombre = nombre

    def setNota(self, nota):
        self.nota = nota

    def getNombre(self):
        print("Nombre: ", self.nombre)

    def getNota(self):
        print("Nota: ", self.nota)

    def aprobo(self):
        if (self.nota >= 3.0):
            print("Aprobo")
        else:
            print("No aprobo")

alumno = Alumno()

alumno.setNombre("Juliana")
alumno.setNota(3.0)
alumno.getNombre()
alumno.getNota()
alumno.aprobo()
