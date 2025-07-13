


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
        if listaNotas:
            promedio = sum(listaNotas)/len(listaNotas)
            print(promedio)



while True:
    print("\nRegistrar nuevo estudiante")
    print("1.Ingrese nombre y apellido")
    nombre = input()
    print("2Ingrese carne")
    carne = input()
    print("Ingrese carrera")
    carrera = input()

    estudianteNuevo = Estudiantes(nombre,carne,carrera)
    listaEstudiantes.append(estudianteNuevo)

    estudianteNuevo.MostrarInformacino()


    while True:
        try:
            print(" ingrese la nota ")
            nota =float(input())
            listaNotas.append(nota)
            break
        except ValueError:
            print("ingrese un numero valido")

    print("Quiere ingresar otro alumno, (1.si) (2. no)")
    seleccion =int(input())

    if seleccion == 1:
        continue

    elif seleccion == 2:
            print("este es el listado de estudiante")
            for i in listaEstudiantes:
                i.MostrarInformacino()


            print(" este  es el prmedio de notas")
            listaEstudiantes[0].PromedioTotal()
            break

    else:
        print("opcion no valida")









