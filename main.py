
listaEstudiantes = []
listaNotas = []
class Estudiantes:
    def __init__(self,nombre,carne,carrera):
        self.nombre = nombre
        self.carne = carne
        self.carrera = carrera


    def MostrarInformacino(self ):
        print(self.nombre,self.carne,self.carrera)

    def PromedioTotal(self):
        print("Promedio es")


print("\nRegistrar nuevo estudiante")
print("Ingrese nombre y apellido")
nombre = input()
print("Ingrese carne")
carne = input()
print("Ingrese carrera")
carrera = input()



estudianteNuevo= Estudiantes(nombre,carne,carrera)

listaEstudiantes.append(estudianteNuevo)
estudianteNuevo.MostrarInformacino()

print("Ingrese nota final")
nota= input()

listaNotas.append(nota)
for item in listaNotas:
    print(item)


for i in range(len(listaNotas)):
    print(listaNotas[i])












