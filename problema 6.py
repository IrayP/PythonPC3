def ingreso_calificaciones():
    try:
        calificaciones = input("Ingrese las calificaciones separadas por comas: ")
        lista1 = calificaciones.split(sep=",")
        lista2 = []
        for i in lista1:
                j = int(i)
                lista2.append(j)
        print(lista2)
    except:
        print("Valores introducidos no válidos.")
        return ingreso_calificaciones()

ingreso_calificaciones()
    

   








    