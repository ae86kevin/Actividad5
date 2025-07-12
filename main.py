
lista = []
lista = []
class Estudiantes:
    def __init__(self,nombre,carne,carrera,notafinal):
        self.nombre = nombre
        self.carne = carne
        self.carrera = carrera
        self.notafinal = notafinal

    def MostrarInformacino(self ):
        print(self.nombre,self.carne,self.carrera,self.notafinal)

    def PromedioTotal(self):
        print("Promedio es")


print("\nRegistrar nuevo estudiante")
print("Ingrese nombre y apellido")
nombre = input()
print("Ingrese carne")
carne = input()
print("Ingrese carrera")
carrera = input()
print("Ingrese nota final")
notafinal = input()


