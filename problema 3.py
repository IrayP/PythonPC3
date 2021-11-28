class Circulo:
    def __init__(self,radio) -> None:
        self.radio = radio

    def calcular_area(self):
        area = 3.14*(self.radio**2)
        print("El área del círculo es {} unds cuadradas.".format(area))


