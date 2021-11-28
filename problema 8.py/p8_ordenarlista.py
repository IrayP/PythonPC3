def ordenar_lista(lista):
    for i in range(1,len(lista)):
        for j in range(0,len(lista)-i):
            if lista[j] > lista[j+1]:
                x = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = x
    print(lista)



if __name__ == "__ordenar_lista__":
    ordenar_lista()