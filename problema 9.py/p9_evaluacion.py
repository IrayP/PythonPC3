def evaluacion(numero):
    try:
        num = int(input("Introduce un número: "))
        if numero == num:
            print("Has ganado")
        elif numero > num:
            print("El número aleatorio es mayor al introducido")
            return evaluacion(numero)
        elif numero < num:
            print("El número aleatorio es menor al introducido")
            return evaluacion(numero)
        else:
            print("Comando no válido")
            return evaluacion(numero)
    except:
        print("Comando no válido")
        return evaluacion(numero)
    
if __name__ == "__evaluacion__":
    evaluacion()