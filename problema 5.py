class Alumno:
    def __init__(self, nombre, num_registro) -> None:
        self.nombre = nombre
        self.num_registro = num_registro

    def display(self):
        print("El nombre del estudiante es {}.".format(self.nombre))
        print("Su número de registro es {}.".format(self.num_registro))

    def setage(self, edad):        
        print("Su edad es {}.".format(edad))
        #return edad
    def setnota(self, nota):
        print("Su nota es {}.".format(nota))
        #return nota

#demo
#estudiante1 = Alumno("Juan", 2526)
#estudiante1.display()
#edad_estudiante1 = estudiante1.setage(19)
#nota_estudiante1 = estudiante1.setnota(20)


#alumno1 = {"Nombre" : estudiante1.nombre, "N° de registro" : estudiante1.num_registro, 
           #"Edad" : edad_estudiante1, "Nota" : nota_estudiante1}
#print(alumno1)           