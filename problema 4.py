class Rectangulo:
    def __init__(self,largo,ancho) -> None:
        self.largo = largo
        self.ancho = ancho

    def calcular_area(self):
        area = self.largo*self.ancho
        print("El área del rectángulo es {} unds cuadradas.".format(area))



