def filas_triangulo_pascal(n):
    lista1 = [1,1,1,1,2,1,1,3,3,1,1,4,6,4,1]
    if n == 1:
        print(lista1[0])
    elif n == 2:
        print(lista1[0])  
        print(lista1[1:3])
    elif n == 3:
        print(lista1[0])  
        print(lista1[1:3])
        print(lista1[3:6])
    elif n == 4:
        print(lista1[0])  
        print(lista1[1:3])
        print(lista1[3:6])
        print(lista1[6:10])
    else:
        print(lista1[0])  
        print(lista1[1:3])
        print(lista1[3:6])
        print(lista1[6:10])
        print(lista1[10:15])



filas_triangulo_pascal(4)
