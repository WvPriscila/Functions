# Exemplo de lista
A = [-3,-2,1,2,3,5,6,7,9,11,23]


def Posicionar(elemento, lista):
    if len(lista) == 0:
        lista.append(elemento)
    else:
        for i in range(len(lista)):
            if elemento < lista[i]:
                lista.insert(i, elemento)
                break
        else:
            lista.append(elemento)
    print(lista)
    return lista
  

